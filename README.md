# Research Assistant

An AI-Powered Research Assistant that uses the Gemini API and MCP integration to generate structured and accurate research summaries on user-provided topics. The system fetches real-time contextual information through MCP servers and processes it intelligently using AI. The assistant also supports exporting research reports into .PDF and .TXT formats for documentation and sharing.

## Key Features
*   **Intelligence Synthesis**: Automated multi-source research generation.
*   **Real-time Integration**: Live data retrieval via Model Context Protocol (MCP).
*   **Export**: Professional document generation in PDF and TXT formats.
*   **Workspace**: High-fidelity user interface.

## Prerequisites
*   Python 3.10 or higher
*   Google Gemini API Key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/research-assistant.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```

3. Configure environment variables:
   *   Create a `.env` file in the root directory.
   *   Add your API key: `GEMINI_API_KEY=your_actual_key_here`

## Running the Application

1. Start the backend server:
   ```bash
   python -m uvicorn backend.main:app --reload
   ```

2. Launch the interface:
   *   Open `frontend/index.html` in any web browser.

## Project Structure
*   `backend/`: API server, research agent logic, and MCP tools.
*   `frontend/`: Institutional user interface assets (HTML, CSS, JS).
*   `research_exports/`: Local directory for saved research reports.
