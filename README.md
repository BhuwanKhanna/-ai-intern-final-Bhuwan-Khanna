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
- 
The assistant includes multiple MCP-powered tools:

| Tool | Description |
|------|-------------|
| web_search | Performs live internet searches |
| save_research | Saves generated reports locally |
| list_past_research | Lists all previous reports |
| read_research_file | Reads saved research files |

## Real-Time Web Search
- Integrated DuckDuckGo search engine
- Multi-source information aggregation
- Live internet research capability

## Export System
- Export reports in:
  - PDF format
  - TXT format
- Local storage for generated reports

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
![Preview](Screenshot%202026-05-11%20120645.png)

---

![Dashboard](Screenshot%202026-05-11%20103010.png)

---

## Research Generation Workspace
![Workspace](Screenshot%202026-05-11%20120702.png)

![Research Output](Screenshot%202026-05-11%20120828.png)


---



---

## Generated Research Output

![System](Screenshot%202026-05-11%20120851.png)
---

## PDF and TXT Export Feature

![Export](Screenshot%202026-05-11%20120919.png)

---

![System](Screenshot%202026-05-11%20121008.png)

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
├── screenshots/
│
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


# EXPORT FEATURES

Generated reports can be exported in:

- Professional PDF Documents
- TXT Research Files


