# AI Research Assistant

An advanced AI-Powered Research Assistant that uses the Gemini API and MCP integration to generate structured, intelligent, and real-time research reports on user-provided topics. The system performs live web retrieval through MCP tools, processes contextual information using AI, and exports professional research reports in PDF and TXT formats.

The project combines modern AI reasoning, modular MCP architecture, real-time search retrieval, persistent research memory, and professional report generation into a unified end-to-end research workflow.

---

# FEATURES

## AI-Powered Research Generation
- Generates structured and detailed research reports
- Uses Google Gemini for intelligent reasoning and synthesis
- Supports deep technical and analytical content generation

## MCP Tool Integration
- MCP-compatible modular architecture
- Dynamic AI tool orchestration
- Real-time contextual information retrieval

## Real-Time Web Search
- Integrated DuckDuckGo search engine
- Multi-source information aggregation
- Live internet research capability

## Export System
- Export reports in:
  - PDF format
  - TXT format
- Local storage for generated reports

## Persistent Research Memory
- Save previous research sessions
- Read historical research files
- Reuse context from earlier reports

## Modern Frontend Workspace
- High-fidelity responsive UI
- Interactive research workflow
- Clean and professional interface

---

# SYSTEM ARCHITECTURE

```text
USER INPUT
     ↓
FRONTEND INTERFACE
     ↓
FASTAPI BACKEND
     ↓
RESEARCH AGENT
     ↓
GEMINI AI MODEL
     ↓
MCP TOOL SERVER
 ├── web_search()
 ├── save_research()
 ├── list_past_research()
 └── read_research_file()
     ↓
FINAL RESEARCH REPORT
     ↓
PDF / TXT EXPORT
```

---

# TECH STACK

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| FastAPI | API Server |
| Gemini API | AI Research Generation |
| MCP | Tool Orchestration |
| DuckDuckGo Search | Real-Time Search |
| HTML/CSS/JavaScript | Frontend UI |
| Uvicorn | ASGI Server |

---

# PROJECT PREVIEW

## Dashboard Interface
<img width="1896" height="995" alt="image" src="https://github.com/user-attachments/assets/61ec30fa-9743-4bfe-b776-c0875a8d6c37" />


<img width="1897" height="990" alt="image" src="https://github.com/user-attachments/assets/e2f6d5e9-0cf4-4c06-901f-cbcd745f9483" />

---

## Research Generation Workspace

<img width="1896" height="988" alt="image" src="https://github.com/user-attachments/assets/eab878fa-14a1-4f44-a92d-fb44b18548a2" />

<img width="1890" height="989" alt="image" src="https://github.com/user-attachments/assets/14049848-a7fb-4f3c-be98-0069e3868ee2" />

---

## Generated Research Output

<img width="1893" height="984" alt="image" src="https://github.com/user-attachments/assets/585e1d2d-f6d6-4291-83cc-2e0418052451" />

---

## PDF and TXT Export Feature

<img width="1899" height="998" alt="image" src="https://github.com/user-attachments/assets/0186831f-243a-4856-99bd-c81dbb3f9047" />

<img width="1918" height="997" alt="image" src="https://github.com/user-attachments/assets/c2d53b2d-a858-4a01-a20e-584106210c4a" />


---

# PROJECT STRUCTURE

```bash
research-assistant/
│
├── backend/
│   ├── main.py
│   ├── agent.py
│   ├── mcp_tools.py
│   ├── requirements.txt
│   └── utils/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── research_exports/
│
├── screenshots/
│
├── .env
├── README.md

```

---

# PREREQUISITES

Before running the project, ensure you have:

- Python 3.10 or higher
- Google Gemini API Key

---

# INSTALLATION

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/research-assistant.git

cd research-assistant
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r backend/requirements.txt
```

---

# ENVIRONMENT CONFIGURATION

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_actual_key_here
```

---

# RUNNING THE APPLICATION

## Start Backend Server

```bash
python -m uvicorn backend.main:app --reload
```

Backend Server:

```text
http://127.0.0.1:8000
```

---

## Launch Frontend Interface

Open:

```text
frontend/index.html
```

in any web browser.

---

# MCP TOOLS

The assistant includes multiple MCP-powered tools:

| Tool | Description |
|------|-------------|
| web_search | Performs live internet searches |
| save_research | Saves generated reports locally |
| list_past_research | Lists all previous reports |
| read_research_file | Reads saved research files |

---

# RESEARCH WORKFLOW

```text
Enter Research Topic
        ↓
AI Research Agent
        ↓
Gemini AI Processing
        ↓
MCP Tool Invocation
        ↓
Real-Time Web Retrieval
        ↓
Structured Report Generation
        ↓
PDF / TXT Export
```

---

# EXAMPLE RESEARCH TOPICS

- Artificial Intelligence in Healthcare
- Future of Renewable Energy
- Quantum Computing Applications
- Sustainable Smart Cities
- Blockchain in Finance
- Global Electric Vehicle Market
- Climate Technology Innovations

---

# EXPORT FEATURES

Generated reports can be exported in:

- Professional PDF Documents
- TXT Research Files

All generated reports are stored inside:

```text
research_exports/
```

---

# PERFORMANCE HIGHLIGHTS

- Real-time information retrieval
- Modular MCP architecture
- Persistent research memory
- Long-form AI report generation
- Scalable backend design
- Automated export pipeline

---

