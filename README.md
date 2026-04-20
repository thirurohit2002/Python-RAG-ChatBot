# Medical AI Chatbot with Prompt Guardrails & RAG System

## Overview

A sophisticated **multi-layered AI orchestration system** designed for medical professionals to safely query drug information. This project demonstrates advanced LLM engineering techniques including **prompt guardrailing, intent classification, retrieval-augmented generation (RAG), and iterative prompt optimization**.

The system implements a **two-stage security model** that filters potentially harmful or out-of-scope queries before routing them to specialized classifiers, ensuring responsible AI deployment in sensitive healthcare domains.

---

## Key Features & Technical Achievements

### 🔒 **Intelligent Security Layer (Drug Chat Orchestrator)**
- **Prompt Guardrailing System**: LLM-powered security filter that detects and blocks 6 threat categories:
  - Prompt injection attacks & role-playing exploits
  - Harmful intent and deceptive requests
  - Patient self-diagnosis attempts
  - Out-of-scope or irrelevant queries
  - Probing/jailbreaking attempts

- **Medical Intent Classification**: Two-stage pipeline that classifies approved queries into 6 medical categories:
  - Side Effects & Adverse Reactions
  - Dosage & Administration
  - Contraindications & Drug Interactions
  - Mechanism of Action
  - General Medical Information
  - Invalid/Nonsensical Queries

### 📊 **Automated Prompt Optimization (Guardrail Refinement Loop)**
- **Iterative Self-Refinement Engine**: Automatically generates, evaluates, and improves security prompts over 25+ iterations
- **Dynamic Test Case Generation**: Creates adversarial test suites with positive (legitimate) and negative (malicious) queries
- **Accuracy Tracking & Early Stopping**: Monitors improvement metrics and halts optimization when diminishing returns occur
- **Failure Analysis Feedback Loop**: Uses detailed failure analysis to guide prompt refinement

### 🤖 **Retrieval-Augmented Generation (RAG) System**
- **Semantic Vector Search**: Integrates with Pinecone vector database for efficient document retrieval
- **OpenAI Embeddings**: Uses text-embedding-3-small for high-quality semantic representations
- **Context-Aware Response Generation**: Retrieves top-4 relevant documents and provides source attribution
- **Agent-Based Orchestration**: Implements LangChain agents for flexible tool integration

### 📈 **Comprehensive KPI Measurement**
- **Guard Accuracy Metrics**: Measures classification correctness with detailed statistics
- **False Positive/Negative Rates**: Critical security metrics showing false alarms and missed threats
- **Classifier Performance Tracking**: Measures intent classification accuracy on allowed queries
- **Test Suite Validation**: 10-query test dataset with expected outcomes for performance benchmarking

### 🎨 **Interactive User Interface**
- **Streamlit Web Application**: Real-time visual feedback with two-stage analysis display
- **Progress Indicators**: Spinner animations and clear status updates
- **Error Handling & User Feedback**: Graceful error handling with informative messages

---

## Technology Stack

**Language & Runtime:**
- Python 3.13

**Core AI/LLM Libraries:**
- OpenAI API (via OpenRouter for cost optimization)
- LangChain (agents, tools, embeddings)
- LangChain Hub (prompt management)

**Vector Database & Retrieval:**
- Pinecone Vector Database
- LangChain Pinecone Integration

**Data Processing & Analysis:**
- Pandas (data analysis & KPI reporting)
- tqdm (progress visualization)
- JSON (structured data handling)

**Web Framework:**
- Streamlit (interactive UI)
- FastAPI + Uvicorn (API server)

**Additional Tools:**
- FireCrawl (web scraping)
- Tavily (search & content extraction)
- LangSmith (LLM monitoring & debugging)

---

## Project Structure
langchain-project/ ├── drug_chat.py # Main Streamlit app with two-stage security orchestrator ├── drug_chat_loop.py # Iterative prompt refinement engine ├── core.py # RAG pipeline with vector retrieval ├── measure_kpis_drug_chat.py # KPI measurement & performance analysis ├── test_dataset.py # 10-query test suite for validation ├── ingestion.py # Document pipeline & vector indexing (archived) ├── logger.py # Logging utilities (archived) ├── Pipfile # Dependency management └── pycache/ # Python bytecode cache

---

## How It Works

### **Stage 1: Prompt Guardrail (Security Filter)**
1. User submits a question about Acetaminophen
2. Guard AI analyzes query against 5 security criteria
3. Returns JSON decision: `{result: "ALLOW|BLOCK", threat_category: "...", reasoning: "..."}`
4. Blocks malicious/irrelevant queries with explanation

### **Stage 2: Medical Intent Classification**
1. If query passes guard, classifier processes question
2. Analyzes question intent across 6 medical categories
3. Returns classification for downstream processing
4. Enables specialized handling based on intent

### **Optimization Loop (Self-Refinement)**
1. Generates initial guard prompt from core requirements
2. Creates diverse test cases (positive & negative)
3. Evaluates guard accuracy on test set
4. Provides detailed failure analysis
5. Iteratively refines prompt based on feedback
6. Tracks best version and halts on convergence

### **RAG Pipeline**
1. User query processed through semantic search
2. Retrieves top-4 most relevant documents from Pinecone
3. Generates contextualized answer with source citations
4. Returns both answer and source documents

---

## Key Performance Indicators (KPIs)

The system tracks critical metrics:
- **Guard Accuracy**: % of correct allow/block decisions
- **False Positive Rate (FPR)**: % of legitimate queries incorrectly blocked
- **False Negative Rate (FNR)**: % of malicious queries incorrectly allowed ⚠️ Critical
- **Classifier Accuracy**: % of correct intent classifications
- **Iterative Improvement**: Accuracy gains per optimization cycle

---

Technical Highlights
Advanced Prompt Engineering
Iterative refinement with feedback loops
Adversarial test case generation
Multi-criteria decision making in single prompt
Robust Error Handling
Authentication error detection
JSON validation & parsing
Graceful degradation with informative feedback
Scalable Architecture
Modular design separating concerns
Reusable components (guard, classifier, RAG)
Cloud-ready with Pinecone integration
Production-Ready Security
Temperature=0 for deterministic security decisions
Temperature=0.65 for balanced generation
Strict output format validation
 
Real-World Applications
✅ Medical Information Systems (Doctors only) ✅ Drug Interaction Verification ✅ Clinical Decision Support Tools ✅ Secure Medical AI Chatbots ✅ Adversarial AI Testing & Robustness Evaluation ✅ Prompt Engineering Research & Development
 
Learning Outcomes Demonstrated
LLM Orchestration: Multi-stage pipelines with specialized agents
Prompt Engineering: Iterative optimization & self-refinement
Security & Safety: Guardrailing harmful outputs & detecting attacks
Vector Search & RAG: Semantic document retrieval & context integration
LLM Evaluation: Comprehensive KPI measurement & failure analysis
Full-Stack AI: From backend LLM operations to interactive UI

Future Enhancements
  Multi-drug support beyond Acetaminophen
  User authentication & role-based access
  Persistent conversation history
  Advanced analytics dashboard
  CI/CD pipeline for automated testing
  Containerization (Docker) for deployment

## Quick Start

### Prerequisites
- Python 3.13+
- Pipenv for dependency management
- API Keys: OpenAI/OpenRouter, Pinecone

### Installation
```bash
pipenv install
pipenv shell

Environment Setup
  OPENROUTER_API_KEY=your_key_here
  PINECONE_API_KEY=your_key_here
  OPENAI_API_KEY=your_key_here
