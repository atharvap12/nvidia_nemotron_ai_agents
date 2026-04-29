# ai-agent-fundamentals

Hands-on examples covering AI agent fundamentals: a shopping agent, guardrails, and evaluation.

## Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager

## Setup

### 1. Clone the repo

```bash
git clone <repo-url>
cd ai-agent-fundamentals
```

### 2. Configure environment variables

```bash
cp sample.env .env
```

Open `.env` and fill in your API keys:

```
GROQ_API_KEY=<your groq key here>
LANGSMITH_API_KEY=<your langsmith key here>
```

| Key | Where to get it |
|-----|----------------|
| `GROQ_API_KEY` | [console.groq.com](https://console.groq.com)  |
| `LANGSMITH_API_KEY` | [smith.langchain.com](https://smith.langchain.com) |

### 3. Install dependencies

```bash
uv sync
```

### 4. Activate the virtual environment

**macOS / Linux:**
```bash
source .venv/bin/activate
```

**Windows (Command Prompt):**
```cmd
.venv\Scripts\activate.bat
```

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

## Running the examples

### 1. Shopping Agent

First, set up the database, then start the API server and agent:

```bash
# In another terminal — run the shopping agent
python 1_shopping_agent/shopping_agent.py
```

### 2. Guardrails

```bash
python 2_guardrails/guardrails.py
```

### 3. Evaluation

```bash
# Run functional evaluation
python 3_eval/func_eval.py

```

## Project structure

```
ai-agent-fundamentals/
├── 1_shopping_agent/     # Tool-calling agent with a product reviews API
├── 2_guardrails/         # Input/output guardrail patterns
├── 3_eval/               # Agent evaluation with LangSmith
├── sample.env            # Template for environment variables
└── pyproject.toml        # Project dependencies (managed by uv)
```
