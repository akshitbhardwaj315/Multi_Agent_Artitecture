let currentThreadId = null;
let isWaitingForHITL = false;
let abortController = null;

const messagesDiv = document.getElementById('messages');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');
const hitlOverlay = document.getElementById('hitl-overlay');
const hitlQuestion = document.getElementById('hitl-question');
const hitlInput = document.getElementById('hitl-input');
const hitlSubmit = document.getElementById('hitl-submit');
const newChatBtn = document.getElementById('new-chat-btn');
const threadList = document.getElementById('thread-list');

function generateThreadId() { return crypto.randomUUID(); }

function newChat() {
    if (abortController) abortController.abort();
    currentThreadId = generateThreadId();
    isWaitingForHITL = false;
    hitlOverlay.classList.add('hidden');
    messagesDiv.innerHTML = '';
    
    // Update active state
    document.querySelectorAll('.thread-item').forEach(el => el.classList.remove('active'));
    
    const th = document.createElement('div');
    th.className = 'thread-item active';
    th.textContent = 'Conversation • ' + currentThreadId.split('-')[0];
    threadList.appendChild(th);
}

function appendUserMessage(text) {
    const el = document.createElement('div');
    el.className = 'message msg-user';
    el.textContent = text;
    messagesDiv.appendChild(el);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

function appendBotMessageShell() {
    const el = document.createElement('div');
    el.className = 'message msg-bot';
    
    const contentWrap = document.createElement('div');
    contentWrap.className = 'bot-content-wrapper';
    contentWrap.innerHTML = '<div class="loader">Processing...</div>';
    
    const diagBar = document.createElement('div');
    diagBar.className = 'diagnostics-bar';
    
    el.appendChild(contentWrap);
    el.appendChild(diagBar);
    messagesDiv.appendChild(el);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
    
    return { el, contentWrap, diagBar };
}

async function processSSEStream(response, shell, startTime) {
    const reader = response.body.getReader();
    const decoder = new TextDecoder("utf-8");
    let currentEvent = null;
    let buffer = "";
    
    shell.contentWrap.innerHTML = '';
    let mdOutput = '';
    let retrievedDocs = [];

    while (true) {
        const { value, done } = await reader.read();
        if (done) break;
        
        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split('\n');
        buffer = lines.pop();

        for (const line of lines) {
            if (line.startsWith("event: ")) {
                currentEvent = line.substring(7).trim();
            } else if (line.startsWith("data: ")) {
                const dataStr = line.substring(6).trim();
                
                if (dataStr === "[DONE]") {
                    const latency = Date.now() - startTime;
                    const latPill = document.createElement('div');
                    latPill.className = 'stat-pill';
                    latPill.innerHTML = `⏱️ ${latency}ms`;
                    shell.diagBar.appendChild(latPill);
                    
                    if (retrievedDocs && retrievedDocs.length > 0) {
                        const acc = document.createElement('div');
                        acc.className = 'sources-accordion';
                        
                        const head = document.createElement('div');
                        head.className = 'sources-header';
                        head.innerHTML = `<span>📚 View Sources (${retrievedDocs.length})</span> <span>▼</span>`;
                        
                        const body = document.createElement('div');
                        body.className = 'sources-body';
                        retrievedDocs.forEach(d => {
                            const p = document.createElement('p');
                            p.textContent = d.text.substring(0, 300) + '...';
                            body.appendChild(p);
                        });
                        
                        head.onclick = () => body.classList.toggle('open');
                        acc.appendChild(head);
                        acc.appendChild(body);
                        shell.contentWrap.appendChild(acc);
                    }
                    messagesDiv.scrollTop = messagesDiv.scrollHeight;
                    return;
                }
                
                if (currentEvent === "token") {
                    const decoded = dataStr.startsWith('"') ? JSON.parse(dataStr) : dataStr;
                    mdOutput += decoded; 
                    shell.contentWrap.innerHTML = marked.parse(mdOutput);
                    messagesDiv.scrollTop = messagesDiv.scrollHeight;
                } else if (currentEvent === "meta") {
                    try {
                        const meta = JSON.parse(dataStr);
                        if(meta.intent) {
                            const iSpan = document.createElement('span');
                            iSpan.className = 'badge intent-' + meta.intent;
                            iSpan.textContent = meta.intent.toUpperCase();
                            shell.diagBar.appendChild(iSpan);
                        }
                        
                        if (meta.intent === 'rag') {
                            const confPct = (meta.confidence * 100).toFixed(0);
                            const cPill = document.createElement('div');
                            cPill.className = 'stat-pill';
                            cPill.innerHTML = `🎯 ${confPct}% Confidence`;
                            shell.diagBar.appendChild(cPill);
                        }
                        
                        if (meta.sources) {
                            retrievedDocs = meta.sources;
                        }
                    } catch(e) {}
                } else if (currentEvent === "hitl") {
                    isWaitingForHITL = true;
                    hitlOverlay.classList.remove('hidden');
                    hitlQuestion.textContent = dataStr;
                }
            }
        }
    }
}

async function sendMessage(text) {
    if (!text.trim() || isWaitingForHITL) return;
    
    appendUserMessage(text);
    userInput.value = '';
    const shell = appendBotMessageShell();
    const startTime = Date.now();
    
    abortController = new AbortController();
    try {
        const response = await fetch('/chat/stream', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: text, thread_id: currentThreadId, stream: true }),
            signal: abortController.signal
        });
        await processSSEStream(response, shell, startTime);
    } catch(e) {
        console.error(e);
        shell.contentWrap.textContent = "Error communicating with agent.";
    }
}

async function submitHITL() {
    const clarification = hitlInput.value;
    if (!clarification.trim()) return;
    
    hitlOverlay.classList.add('hidden');
    isWaitingForHITL = false;
    hitlInput.value = '';
    
    appendUserMessage(clarification);
    const shell = appendBotMessageShell();
    const startTime = Date.now();
    
    try {
        const response = await fetch('/hitl/resume', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_clarification: clarification, thread_id: currentThreadId }),
        });
        await processSSEStream(response, shell, startTime);
    } catch(e) {
        console.error(e);
    }
}

sendBtn.addEventListener('click', () => sendMessage(userInput.value));
userInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') sendMessage(userInput.value);
});

hitlSubmit.addEventListener('click', submitHITL);
hitlInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') submitHITL();
});

newChatBtn.addEventListener('click', newChat);
newChat();
