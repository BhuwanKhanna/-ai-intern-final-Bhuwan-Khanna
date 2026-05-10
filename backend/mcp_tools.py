import os
from mcp.server.fastmcp import FastMCP
from duckduckgo_search import DDGS
import json

# Initialize FastMCP Server
mcp = FastMCP("ResearchAssistantTools")

@mcp.tool()
def web_search(query: str) -> str:
    """
    Performs a web search using DuckDuckGo and returns the results as a string.
    Use this to fetch real-time information on any research topic.
    """
    print(f"DEBUG: Searching web for: {query}")
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=10))
            if not results:
                return "No results found."
            
            formatted_results = []
            for r in results:
                formatted_results.append(f"Title: {r['title']}\nLink: {r['href']}\nSnippet: {r['body']}\n")
            
            return "\n---\n".join(formatted_results)
    except Exception as e:
        return f"Error performing search: {str(e)}"

@mcp.tool()
def save_research(filename: str, content: str) -> str:
    """
    Saves the research content to the local filesystem.
    Filenames should end in .txt or .md.
    """
    print(f"DEBUG: Saving research to: {filename}")
    try:
        os.makedirs("research_exports", exist_ok=True)
        filepath = os.path.join("research_exports", filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Successfully saved research to {filepath}"
    except Exception as e:
        return f"Error saving file: {str(e)}"

@mcp.tool()
def list_past_research() -> str:
    """
    Returns a list of all previously saved research report filenames.
    Use this to see what topics have already been researched.
    """
    try:
        if not os.path.exists("research_exports"):
            return "No past research found."
        files = [f for f in os.listdir("research_exports") if f.endswith(('.txt', '.md'))]
        if not files:
            return "No past research files found."
        return "Past Research Files: " + ", ".join(files)
    except Exception as e:
        return f"Error listing files: {str(e)}"

@mcp.tool()
def read_research_file(filename: str) -> str:
    """
    Reads the content of a specific past research report.
    Use this to gain context from previous work.
    """
    try:
        filepath = os.path.join("research_exports", filename)
        if not os.path.exists(filepath):
            return "File not found."
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"

if __name__ == "__main__":
    mcp.run()
