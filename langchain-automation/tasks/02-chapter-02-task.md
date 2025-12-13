# Task: Write Chapter 2 - Technical Architecture Blueprint

**Chapter Title:** Blueprint Kiến Trúc Kỹ Thuật Cho Solo Founder
**Objective:** Define the concrete technical stack and architecture for a scalable, automated AI education business.

## Detailed Outline & Requirements

### 1. The "Brain-Body" Architecture
-   **Story Hook:** A founder trying to glue 10 different no-code tools together vs. one building a cohesive code-based system.
-   **Blueprint:**
    -   **Body (Frontend/App):** Next.js (Vercel). Fast, SEO-friendly, great UI.
    -   **Memory (Database):** Supabase (PostgreSQL + pgvector). The "Long-term Memory" for Agents.
    -   **Brain (Logic):** LangChain (Python/JS). The reasoning engine.
-   **Why this stack?** Perfect balance of speed, cost, and scalability for a Solo Founder.

### 2. Best Practices về Dữ liệu (Data Strategy)
-   **Concept:** RAG (Retrieval-Augmented Generation) is the heart of personalized education.
-   **Implementation:** How to structure data in Supabase for efficient retrieval. Chunking strategies for textbooks/courses.

### 3. Serverless vs Edge
-   **Decision:** When to use Edge Functions (fast, low latency) vs Serverless (heavy lifting).
-   **Recommendation:** Edge for UI/Streaming, Serverless (Python) for heavy LangChain processing.

### 4. Dự báo: Local-first AI & SLMs
-   **Trend:** Small Language Models (Llama 3 8B, Phi-3) running on the user's device or local edge.
-   **Future-proofing:** Designing the architecture to swap Cloud Models for Local Models later to save costs.

## Tone & Style
-   **Prescriptive:** Don't just list options; recommend the *best* path for this specific audience.
-   **Visual:** Describe diagrams (e.g., "Imagine a diagram showing...").

## Deliverables
-   Create folder: `e:\Books\langchain-automation\chapter-02`
-   File: `e:\Books\langchain-automation\chapter-02\01-architecture-blueprint.md`
