⚡ TORVAK

<p align="center">
  <img src="https://img.shields.io/badge/TORVAK-AI%20Operating%20System-8A2BE2?style=for-the-badge" alt="TORVAK">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/LLM-Powered-orange?style=for-the-badge" alt="LLM">
  <img src="https://img.shields.io/badge/RAG-Enabled-green?style=for-the-badge" alt="RAG">
</p>

<p align="center">
  <b>A modular AI Operating System designed to understand, remember, reason, and act.</b>
</p>

🧠 About

TORVAK is a modular AI Operating System being built to evolve into an intelligent personal AI assistant.

Instead of treating an LLM as just a chatbot, TORVAK is designed as a system where different capabilities work together:

             ┌─────────────────────┐
             │        USER         │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │     TORVAK CORE     │
             └──────────┬──────────┘
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
     ┌──────┐       ┌──────┐       ┌────────┐
     │ LLM  │       │ RAG  │       │ Memory │
     └──────┘       └──────┘       └────────┘
        │               │               │
        └───────────────┼───────────────┘
                        ▼
                  ┌───────────┐
                  │  Planner  │
                  └─────┬─────┘
                        │
                        ▼
                  ┌───────────┐
                  │   Tools   │
                  └───────────┘

The long-term vision is:

Understand → Remember → Reason → Plan → Act

✨ Features

🤖 LLM Integration

TORVAK uses an LLM as its reasoning and language layer while keeping the rest of the architecture modular.

The LLM layer is designed around a provider-independent interface so additional providers can be integrated later.

📚 Retrieval-Augmented Generation

TORVAK includes a modular RAG subsystem for working with external knowledge.

Documents
    ↓
Text Processing
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector Search
    ↓
Relevant Context
    ↓
LLM

🧠 Memory

TORVAK is being developed with both short-term and long-term memory.

Memory categories include:

Profile
Preferences
Facts
Projects
Goals
Tasks

The memory architecture is evolving from persistent storage toward intelligent memory extraction and semantic retrieval.

🧩 Modular Core

TORVAK is divided into independent components instead of putting the entire assistant inside a single file.

This makes the system easier to:

Extend

Test

Debug

Replace components

Integrate new AI capabilities

🛠️ Tools

The architecture supports integrating tools that allow TORVAK to move beyond generating text and eventually perform actions.

Planned capabilities include:

System Control
File Operations
Web Operations
Application Control
Automation
Custom Tools

🎙️ Voice

TORVAK includes the foundation for voice-based interaction through:

Speech Recognition
      ↓
     LLM
      ↓
Text-to-Speech

Wake-word support is also part of the voice architecture.

🏗️ Architecture

                         USER
                           │
                           ▼
                    ┌─────────────┐
                    │  Assistant  │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │    Router   │
                    └──────┬──────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
      ┌────────┐       ┌────────┐      ┌──────────┐
      │   LLM  │       │  RAG   │      │  Memory  │
      └────┬───┘       └────┬───┘      └─────┬────┘
           │                │                 │
           └────────────────┼─────────────────┘
                            │
                            ▼
                     ┌────────────┐
                     │   Planner  │
                     └─────┬──────┘
                           │
                           ▼
                     ┌────────────┐
                     │   Tools    │
                     └────────────┘

📁 Project Structure

TORVAK/
│
├── core/
│   ├── ai_engine.py
│   ├── assistant.py
│   ├── coding_engine.py
│   ├── command_router.py
│   ├── commands.py
│   ├── context_memory.py
│   ├── logger.py
│   ├── llm.py
│   ├── memory_engine.py
│   ├── memory_manager.py
│   ├── offline_ai.py
│   ├── online_ai.py
│   ├── router.py
│   ├── speech.py
│   ├── system_control.py
│   ├── tts.py
│   ├── wakeword.py
│   │
│   ├── memory/
│   │   ├── models.py
│   │   └── store.py
│   │
│   ├── rag/
│   │
│   └── tools/
│
├── memory/
│
├── .env
├── requirements.txt
└── README.md

🧠 Memory Architecture

The memory system is being designed around structured memory records rather than scattered data.

Conversation
     │
     ▼
Memory Extraction
     │
     ▼
MemoryRecord
     │
     ▼
Persistent Store
     │
     ▼
Semantic Retrieval
     │
     ▼
Relevant Memory

Example:

User:
"I'm building an AI assistant called TORVAK."

        ↓

Memory

Type: PROJECT
Content: User is building TORVAK
Importance: High

This allows future components such as the Planner to use memory as context when making decisions.

🗺️ Roadmap

Phase 1 — Knowledge

RAG foundation

Document processing

Embeddings

Vector retrieval

Phase 2 — Memory

Memory models

Persistent memory store

Intelligent memory extraction

Semantic memory retrieval

Memory manager

Memory consolidation

Phase 3 — Intelligence

Planner

Task decomposition

Context-aware reasoning

Agentic workflows

Phase 4 — Actions

Tool calling

Tool registry

Tool execution

Permission handling

Action planning

Phase 5 — Web

Web search

Web information retrieval

Search-aware reasoning

Phase 6 — Voice

Speech-to-text

Text-to-speech

Wake-word pipeline

Continuous voice interaction

Phase 7 — Interface

Desktop GUI

Memory visualization

Task dashboard

System controls

🛠️ Tech Stack

Technology

Purpose

Python

Core development

LLMs

Reasoning & language

RAG

Knowledge retrieval

Embeddings

Semantic representation

FAISS

Vector search

JSON

Initial persistent storage

Speech Recognition

Voice input

Text-to-Speech

Voice output

🚀 Installation

1. Clone the repository

git clone https://github.com/Hariom0605/TORVAK.git
cd TORVAK

2. Create a virtual environment

python -m venv venv

3. Activate the environment

Windows:

venv\Scripts\activate

Linux / macOS:

source venv/bin/activate

4. Install dependencies

pip install -r requirements.txt

5. Configure environment variables

Create a .env file:

GEMINI_API_KEY=your_api_key_here
LLM_PROVIDER=gemini
LLM_MODEL=gemini-2.5-flash
LLM_TEMPERATURE=0.2

6. Run TORVAK

python main.py

🎯 Design Principles

Modularity

Each subsystem has a clear responsibility.

Extensibility

New models, tools, and capabilities should be easy to integrate.

Context Awareness

The assistant should understand both current conversation and persistent context.

Provider Independence

The core architecture should not be tightly coupled to a single AI provider.

Incremental Development

Each subsystem is developed independently before being integrated into the complete system.

🔮 Vision

TORVAK is not being built as another simple chatbot.

The long-term objective is to create an AI system capable of:

             UNDERSTAND
                  │
                  ▼
              REMEMBER
                  │
                  ▼
               REASON
                  │
                  ▼
                PLAN
                  │
                  ▼
                 ACT
                  │
                  ▼
                LEARN

TORVAK aims to bring these capabilities together into one modular system.

📌 Project Status

🚧 TORVAK is actively under development.

The architecture and capabilities are evolving continuously as new subsystems are implemented.

👨‍💻 Author

Hariom Tiwari

Building TORVAK as an exploration into modular AI systems, agentic architectures, memory, RAG, and personal AI assistants.

⭐ Support

If you find the project interesting, consider giving the repository a ⭐.

Follow the development as TORVAK evolves from a modular AI assistant into a complete AI Operating System.
