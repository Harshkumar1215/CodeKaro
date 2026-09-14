# CODEKARO Repository Database & Statistics System

This directory contains the persistent statistical records for the CODEKARO platform.

## 📁 Files

- `stats.json`: The core JSON statistics file storing the global count of students who have joined and practiced.
- `counter_server.py`: A lightweight, production-ready Python backend / microservice for atomic read/write updates to `stats.json` when self-hosted or deployed on Python-capable hosting.

---

## 🔒 Security Architecture (GitHub Pages & Public Web)

1. **Static Frontend Separation**:
   GitHub Pages hosts only static files (`HTML/CSS/JS`). Browser JavaScript cannot directly write to a GitHub repository file without exposing secret credentials (which is strictly prohibited).
   
2. **Global Atomic Counter**:
   The frontend communicates with a secure, atomic serverless endpoint (`api/counter.js` or global CounterAPI proxy). No GitHub Personal Access Tokens or secret keys are ever exposed in client-side code.

3. **Concurrency & Race Conditions**:
   The counter operates atomically to ensure concurrent student submissions (e.g. Student A, Student B, and Student C simultaneously) increment the count accurately without overwrite conflicts.

4. **Privacy**:
   Student names are saved strictly in the student's browser `localStorage` for their personalized greeting. Student names are never sent to or stored in `stats.json`.
