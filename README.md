# Sambot — A personal intelligence system for thinking, learning, building, and getting things done.

Sambot is the foundation of a long-term personal intelligence system: a single, extensible assistant designed to eventually understand my work, automate my decisions, and act on my behalf across every project I run — from product architecture to community operations.

## The Idea

I build and run multiple things at once — a startup, community, technical education. A personal intelligence is the connective layer: one assistant that can eventually query my codebases, summarize my network's activity, draft strategy, and reason over everything I'm working on, instead of context-switching between five disconnected tools.

Sambot is step one: prove the architecture can scale from "simulated responses" to "autonomous agent" without a rewrite.

---

## What's Built

- Chat interface with session-level conversation context
- Modular design — the interface, conversation logic, and AI backend are fully decoupled, so any layer can be swapped without touching the others
- Automated tests and code quality checks from day one
- A provider-agnostic architecture ready to plug in any AI backend (local or cloud) via configuration, not code changes

## Engineering Principles

- **Separation of concerns** — interface, logic, and intelligence evolve independently
- **Configuration over hardcoding** — swap AI providers without rewriting the app
- **Testable by design** — core logic verified with zero live AI dependency
- **Incremental growth** — every capability earns its place; no premature complexity

---

## Roadmap

| Phase                     | Focus                                        | Status         |
| ------------------------- | -------------------------------------------- | -------------- |
| 1 — Foundation            | Core app, conversation handling, testing     | ✅ Complete    |
| 2 — Real AI Integration   | Local + cloud model connections              | 🔜 In progress |
| 3 — Smarter Assistant     | Context management, natural interaction      | Planned        |
| 4 — Production Readiness  | Containerized deployment, CI/CD              | Planned        |
| 5 — Advanced Intelligence | RAG, multi-step reasoning, autonomous agents | Planned        |

---

## Why It Matters

This is a deliberate, end-to-end build of the same kind of system powering production AI products today: solid foundations first, intelligence and autonomy layered in with intent. The long-term goal is a personal intelligence that scales with everything I build next.
