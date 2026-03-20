const BASE_URL = "http://localhost:8000";
const SESSION_ID = crypto.randomUUID();

const chatList = document.getElementById("chat-list");
const userInput = document.getElementById("user-input");
const sendButton = document.getElementById("send-button");
const typingIndicator = document.getElementById("typing-indicator");
const hitlBanner = document.getElementById("hitl-banner");
const hitlInput = document.getElementById("hitl-input");
const hitlConfirm = document.getElementById("hitl-confirm");
const hitlCorrect = document.getElementById("hitl-correct");

let currentAgentMessage = null;
let accumulatedText = "";

function renderMarkdown(text) {
    return typeof marked !== 'undefined'
        ? marked.parse(text, { breaks: true, gfm: true })
        : text;
}

function addUserMessage(text) {
    const messageDiv = document.createElement("div");
    messageDiv.className = "message user";
    messageDiv.innerHTML = `<div class="message-bubble">${escapeHtml(text)}</div>`;
    chatList.appendChild(messageDiv);
    scrollToBottom();
}

function createAgentMessage(agentName) {
    const messageDiv = document.createElement("div");
    messageDiv.className = "message agent";
    
    const agentClass = agentName.toLowerCase().replace("agent", "");
    const badge = `<div class="agent-badge ${agentClass}">${agentName}</div>`;
    const bubble = `<div class="message-bubble"></div>`;
    
    messageDiv.innerHTML = badge + bubble;
    chatList.appendChild(messageDiv);
    scrollToBottom();
    
    return messageDiv.querySelector(".message-bubble");
}

function addDebugPanel(messageDiv, telemetry) {
    const timeClass = (ms) => ms < 1000 ? 'fast' : ms < 3000 ? 'medium' : 'slow';
    const agentClass = (a) => a?.toLowerCase().includes('weather') ? 'agent-weather' :
                              a?.toLowerCase().includes('hacker') ? 'agent-hackernews' : 'agent-chitchat';
    const rows = [
        ['⏱ Total Time',    `<span class="debug-row-value ${timeClass(telemetry.total_request_time_ms)}">${telemetry.total_request_time_ms?.toFixed(0) ?? '—'} ms</span>`],
        ['🤖 LLM Time',     `<span class="debug-row-value ${timeClass(telemetry.llm_response_time_ms)}">${telemetry.llm_response_time_ms?.toFixed(0) ?? '—'} ms</span>`],
        ['🧠 Agent',        `<span class="debug-row-value ${agentClass(telemetry.agent_name)}">${telemetry.agent_name ?? '—'}</span>`],
        ['📦 Model',        `<span class="debug-row-value">${telemetry.model_used ?? '—'}</span>`],
        ['🔁 Retries',      `<span class="debug-row-value">${telemetry.retry_count ?? 0}</span>`],
        ['🔐 HITL',         `<span class="debug-row-value ${telemetry.hitl_status === 'triggered' ? 'hitl-triggered' : ''}">${telemetry.hitl_status ?? 'none'}</span>`],
        ['🪙 Tokens',       `<span class="debug-row-value">${telemetry.token_count ?? 'N/A'}</span>`],
    ];
    
    const tableHTML = rows.map(([label, val]) =>
        `<span class="debug-row-label">${label}</span>${val}`
    ).join('');

    const details = document.createElement("details");
    details.className = "debug-panel";
    details.innerHTML = `
        <summary>📊 Debug Panel</summary>
        <div class="debug-table">${tableHTML}</div>
    `;
    
    messageDiv.appendChild(details);
}

function showTyping() {
    typingIndicator.classList.remove("hidden");
    scrollToBottom();
}

function hideTyping() {
    typingIndicator.classList.add("hidden");
}

function scrollToBottom() {
    chatList.scrollTop = chatList.scrollHeight;
}

function escapeHtml(text) {
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
}

function sendMessage(query) {
    if (!query.trim()) return;
    
    addUserMessage(query);
    userInput.value = "";
    showTyping();
    
    const eventSource = new EventSource(
        `${BASE_URL}/chat/stream?query=${encodeURIComponent(query)}&session_id=${SESSION_ID}`
    );
    
    let agentName = "Agent";
    currentAgentMessage = null;
    accumulatedText = "";
    
    eventSource.addEventListener("message", (event) => {
        hideTyping();
        
        if (!currentAgentMessage) {
            currentAgentMessage = createAgentMessage(agentName);
        }
        
        accumulatedText += event.data;
        currentAgentMessage.textContent = accumulatedText;
        scrollToBottom();
    });
    
    eventSource.addEventListener("telemetry", (event) => {
        const data = JSON.parse(event.data);
        agentName = data.agent_name || "Agent";
        
        if (currentAgentMessage) {
            currentAgentMessage.innerHTML = renderMarkdown(accumulatedText);
            const messageDiv = currentAgentMessage.parentElement;
            addDebugPanel(messageDiv, data.telemetry);
        }
        
        if (data.hitl_required) {
            hitlBanner.classList.remove("hidden");
        }
        
        eventSource.close();
    });
    
    eventSource.addEventListener("error", (event) => {
        hideTyping();
        
        if (!currentAgentMessage) {
            currentAgentMessage = createAgentMessage("Error");
        }
        
        currentAgentMessage.textContent = "⚠️ An error occurred. Please try again.";
        eventSource.close();
    });
}

function sendHITL(action, correction) {
    hitlBanner.classList.add("hidden");
    hitlInput.value = "";
    
    fetch(`${BASE_URL}/hitl/respond`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            session_id: SESSION_ID,
            action: action,
            correction: correction
        })
    })
    .then(res => res.json())
    .then(data => {
        const bubble = createAgentMessage("Agent");
        bubble.textContent = data.answer;
        addDebugPanel(bubble.parentElement, data.telemetry);
    })
    .catch(err => {
        const bubble = createAgentMessage("Error");
        bubble.textContent = "Failed to process HITL response.";
    });
}

sendButton.addEventListener("click", () => {
    sendMessage(userInput.value);
});

userInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
        sendMessage(userInput.value);
    }
});

hitlConfirm.addEventListener("click", () => {
    sendHITL("confirm", null);
});

hitlCorrect.addEventListener("click", () => {
    const correction = hitlInput.value.trim();
    if (correction) {
        sendHITL("correct", correction);
    }
});
