# Task: Write Chapter 8 - Practical Setup & Infrastructure

**Chapter Title:** Thiết Lập Thực Tế: Hybrid AI & GitHub Copilot Ecosystem
**Objective:** Provide a concrete, cost-effective, and scalable setup guide for the modern solo founder.

## Detailed Outline & Requirements

### 1. Mô hình Hybrid Orchestration
-   **Concept:** "Think Locally, Act Globally".
-   **Setup:**
    -   **Local:** Run `Ollama` or `LM Studio` with Llama 3 8B / NVIDIA ToolOrchestra.
    -   **Role:** This local model acts as the router/classifier. It decides if a task is "easy" (handle locally) or "hard" (send to cloud).

### 2. GitHub Copilot là Trung Tâm (Hub)
-   **Tool:** GitHub Copilot CLI (`gh copilot`).
-   **Feature:** GitHub Models (Marketplace). Access to GPT-4o, Claude 3.5 Sonnet via API/SDK often with generous free tiers for dev/startups.
-   **Workflow:** Using Copilot to write the code *and* using the Models API to power the agents.

### 3. Hạ tầng & Triển khai (Infrastructure & Deployment)
-   **Docker:**
    -   *Why:* "It works on my machine" isn't enough.
    -   *How:* Dockerfile for the Agent service. `docker-compose` for local DB + Agent + UI.
-   **Cloudflared Tunnel:**
    -   *Why:* Exposing a local webhook (e.g., for a Slack bot) to the internet securely without opening router ports.
    -   *How:* `cloudflared tunnel run`.
-   **Scaling Path:**
    -   Stage 1: Local PC + Tunnel (MVP/Dev).
    -   Stage 2: VPS (DigitalOcean/Hetzner) with Docker Compose.
    -   Stage 3: Serverless (Vercel/Supabase Functions) or K8s for massive scale.

### 4. Chiến lược tối ưu chi phí (Cost Optimization)
-   **Matrix:**
    -   Low Latency / Low Intelligence -> Local SLM.
    -   High Intelligence / Low Frequency -> GPT-4o (Cloud).
    -   High Volume / Medium Intelligence -> GPT-4o-mini or Llama 3 70B (Groq).

## Tone & Style
-   **Hacker/Maker:** Very hands-on, "get your hands dirty" vibe.
-   **Pragmatic:** Focus on saving money and time.

## Deliverables
-   Create folder: `e:\Books\langchain-automation\chapter-08`
-   File: `e:\Books\langchain-automation\chapter-08\01-practical-setup.md`
