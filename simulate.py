#!/usr/bin/env python3
"""Simulate agent calls to test Harmonia tracking."""
import json
import sqlite3
import time
from pathlib import Path
from datetime import datetime

DB_PATH = Path.home() / ".harmonia" / "harmonia.db"

# Session we created
session_id = "ddcc31d7"

# Simulated agent calls — like an agent doing reflection loop
calls = [
    {"model": "groq/llama-3.1-8b-instant", "prompt": "Write a Python script for web scraping", "response": "Here's a web scraper...", "tokens": 340, "dur": 1200},
    {"model": "auto/best-chat", "prompt": "Improve this scraper: add error handling and retries", "response": "Added retry logic...", "tokens": 520, "dur": 2100},
    {"model": "auto/best-chat", "prompt": "Fix the error handling — it should catch ConnectionError too", "response": "Fixed error handling...", "tokens": 280, "dur": 1500},
    {"model": "groq/llama-3.1-8b-instant", "prompt": "Add async support to the scraper", "response": "Converted to async...", "tokens": 620, "dur": 3400},
    {"model": "auto/best-chat", "prompt": "Review the async code for bugs", "response": "Found race condition...", "tokens": 450, "dur": 1900},
    {"model": "groq/llama-3.1-8b-instant", "prompt": "Fix race condition with asyncio.Lock", "response": "Added lock...", "tokens": 310, "dur": 1300},
    {"model": "auto/best-reasoning", "prompt": "Is the scraper production-ready? Analyze", "response": "Needs tests...", "tokens": 780, "dur": 5100},
    {"model": "auto/best-chat", "prompt": "Write unit tests for the scraper", "response": "Created 5 tests...", "tokens": 560, "dur": 2500},
]

conn = sqlite3.connect(str(DB_PATH))
c = conn.cursor()

for i, call in enumerate(calls):
    prompt_hash = hash(call["prompt"])
    c.execute("""
        INSERT INTO calls (session_id, model, prompt_preview, response_preview,
                          total_tokens, duration_ms, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (session_id, call["model"], call["prompt"], call["response"],
          call["tokens"], call["dur"], datetime.now().isoformat()))

conn.commit()
conn.close()

print(f"Inserted {len(calls)} simulated calls into session {session_id}")
