"""
SQLite wrapper for storing Human-in-the-loop sessions manually.
"""
import sqlite3
import json
import os
from typing import Dict, Optional, Any
from utils.config import settings
from langchain_core.messages import messages_to_dict, messages_from_dict

def _get_conn():
    os.makedirs(os.path.dirname(settings.hitl_db_path) or ".", exist_ok=True)
    conn = sqlite3.connect(settings.hitl_db_path, check_same_thread=False)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS hitl_sessions (
            thread_id TEXT PRIMARY KEY,
            hitl_question TEXT,
            state_json TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    return conn

def save_hitl_session(thread_id: str, hitl_question: str, state_dict: Dict[str, Any]):
    """Save HITL session to sqlite."""
    conn = _get_conn()
    str_state = {}
    for k, v in state_dict.items():
        if k == "messages" and v:
            str_state[k] = messages_to_dict(v)
        else:
            str_state[k] = v

    with conn:
        conn.execute(
            "INSERT OR REPLACE INTO hitl_sessions (thread_id, hitl_question, state_json) VALUES (?, ?, ?)",
            (thread_id, hitl_question, json.dumps(str_state))
        )
    conn.close()

def load_hitl_session(thread_id: str) -> Optional[Dict[str, Any]]:
    """Load HITL session state."""
    conn = _get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT state_json FROM hitl_sessions WHERE thread_id = ?", (thread_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        state = json.loads(row[0])
        if "messages" in state and state["messages"]:
            state["messages"] = messages_from_dict(state["messages"])
        return state
    return None

def delete_hitl_session(thread_id: str):
    """Delete HITL session after usage."""
    conn = _get_conn()
    with conn:
        conn.execute("DELETE FROM hitl_sessions WHERE thread_id = ?", (thread_id,))
    conn.close()
