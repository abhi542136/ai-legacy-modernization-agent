# AI Legacy Modernization Agent

An AI-powered backend system designed to analyze legacy enterprise code, detect migration risks, generate modernized code, and produce structured migration reports through REST APIs.

Built as part of a real-world modernization assessment focused on enterprise migration workflows, AI-assisted code analysis, and backend engineering.

---

# Project Overview

Many enterprise systems still rely on legacy technologies such as:

- VB6
- Classic ASP
- COBOL
- Java EE

These systems often contain:
- Hardcoded credentials
- Raw SQL queries
- Tight coupling
- Missing error handling
- No documentation
- High migration risk

This project provides an automated modernization pipeline that:

1. Accepts legacy code snippets
2. Analyzes them using AI
3. Detects anti-patterns
4. Assesses migration risks
5. Generates modernized code
6. Produces migration checklists and reports

---

# Key Features

## Legacy Code Analysis
- Accepts legacy code snippets via REST API
- Supports multiple legacy technologies
- AI-generated plain-English summaries
- Complexity scoring and pattern detection

## Migration Risk Assessment
Rule-based deterministic risk engine for:
- Hardcoded credentials
- Raw SQL detection
- Missing error handling
- Unsafe coding patterns

## AI-Powered Code Modernization
Generates modern backend code using:
- FastAPI
- Modern coding practices
- Exception handling
- Inline improvement comments

## Migration Checklist Generation
Automatically generates actionable migration tasks such as:
- Replace hardcoded credentials
- Add exception handling
- Use parameterized queries
- Add unit tests
- Improve logging and monitoring

## REST APIs
Interactive APIs with automatic Swagger documentation.

---

# Architecture

```text
Client Request
      ↓
FastAPI REST Controller
      ↓
+-----------------------+
|   LLM Analysis Layer  |
+-----------------------+
      ↓
+-----------------------+
|    Risk Engine        |
| (Rule-Based Logic)    |
+-----------------------+
      ↓
+-----------------------+
| Modern Code Generator |
+-----------------------+
      ↓
+-----------------------+
| Checklist Builder     |
+-----------------------+
      ↓
Migration Report Response
```

---

# Tech Stack

| Component | Technology |
|---|---|
| Backend Framework | FastAPI |
| Language | Python |
| AI Integration | OpenRouter / Claude |
| API Documentation | Swagger UI |
| Validation | Pydantic |
| Environment Management | python-dotenv |
| HTTP Server | Uvicorn |

---

# Project Structure

```text
migration-agent/

├── main.py
├── llm_service.py
├── risk_engine.py
├── checklist.py
├── requirements.txt
├── .env
├── README.md
└── .gitignore
```

---

# Setup Instructions

## 1. Clone Project

```bash
git clone <repository-url>
cd migration-agent
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### PowerShell Fix (If Needed)

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

Then activate again:

```powershell
.\venv\Scripts\Activate.ps1
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file in project root:

```env
API_KEY=your_openrouter_api_key
BASE_URL=https://openrouter.ai/api/v1
MODEL=anthropic/claude-3-haiku
```

---

## 5. Run Application

```bash
uvicorn main:app --reload
```

Application will start at:

```text
http://127.0.0.1:8000
```

---

# Swagger API Documentation

FastAPI automatically provides interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## 1. Analyze Legacy Code

### POST `/analyze`

Analyzes legacy code and returns:
- AI summary
- Detected patterns
- Complexity score
- Risk assessment

### Sample Request

```json
{
  "language": "VB6",
  "module_name": "LoanProcessor",
  "code_snippet": "SELECT * FROM USERS WHERE PWD='123'"
}
```

### Sample Response

```json
{
  "snippet_id": "12345",
  "summary": "Legacy SQL query with hardcoded password.",
  "identified_patterns": [
    "RAW_SQL",
    "HARDCODED_CREDENTIALS"
  ],
  "complexity_score": 2,
  "language_detected": "SQL",
  "risk_assessment": {
    "risk_level": "HIGH",
    "risk_reasons": [
      "HARDCODED_CREDENTIALS",
      "RAW_SQL"
    ]
  }
}
```

---

## 2. Generate Migration Report

### POST `/migrate/{snippet_id}`

Generates:
- Modernized code
- Migration checklist
- Full migration report

---

## 3. Retrieve Migration Report

### GET `/report/{snippet_id}`

Returns previously generated migration report.

---

## 4. Get Detectable Patterns

### GET `/patterns`

Returns supported anti-patterns and descriptions.

---

# Detectable Anti-Patterns

| Pattern | Description |
|---|---|
| HARDCODED_CONFIG | Hardcoded credentials or configs |
| RAW_SQL | Direct SQL queries without parameterization |
| NO_ERROR_HANDLING | Missing exception handling |
| MAGIC_NUMBER | Unexplained hardcoded values |
| TIGHT_COUPLING | Strong dependency between modules |

---

# Error Handling

The application handles:
- Invalid requests
- Empty payloads
- Missing fields
- Invalid snippet IDs
- LLM failures
- JSON parsing issues

All validation errors return structured HTTP responses.

---

# Design Decisions

## Why FastAPI?
FastAPI enables rapid backend development with:
- Automatic validation
- Built-in Swagger documentation
- Lightweight architecture
- High development speed

## Why Rule-Based Risk Assessment?
Migration risk classification is intentionally deterministic instead of AI-driven because:
- Risk assessment must remain auditable
- Critical decisions should not depend on probabilistic AI outputs
- Rule engines provide predictable enterprise behavior

## Why In-Memory Storage?
For this MVP assessment:
- Simplicity and speed were prioritized
- In-memory storage reduces setup overhead
- Storage layer can later be replaced with PostgreSQL or MongoDB

---

# Future Improvements

Potential enhancements:
- Database integration
- Authentication & authorization
- Docker support
- CI/CD pipeline
- Unit testing
- Retry & fallback strategies
- Frontend dashboard
- Multi-model AI support
- Async background processing

---

# Example Use Cases

- Enterprise legacy modernization
- Migration planning
- Risk analysis automation
- Technical debt assessment
- AI-assisted refactoring
- Code audit workflows

---

# Testing the APIs

After starting the server:

```bash
uvicorn main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## Sample Test Case 1 — VB6 Database Call

### Request

```json
{
  "language": "VB6",
  "module_name": "LoanProcessingModule",
  "code_snippet": "SELECT * FROM USERS WHERE PWD='123'"
}
```

### Expected Result

- Detect raw SQL
- Detect hardcoded credentials
- Generate migration checklist
- Return modernization report

---

## Sample Test Case 2 — Validation Error

### Request

```json
{
  "language": "",
  "module_name": "",
  "code_snippet": ""
}
```

### Expected Result

```http
422 Unprocessable Entity
```

---

## Migration Flow

1. Call POST `/analyze`
2. Copy returned `snippet_id`
3. Call POST `/migrate/{snippet_id}`
4. Retrieve report using GET `/report/{snippet_id}`

---

# Author

Developed as part of an enterprise modernization coding assessment using Python, FastAPI, and AI-assisted code analysis.