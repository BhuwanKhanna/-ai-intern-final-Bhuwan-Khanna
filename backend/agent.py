import os
import google.generativeai as genai
from dotenv import load_dotenv
import traceback

# Import our MCP Tool Logic
from .mcp_tools import web_search, save_research, list_past_research, read_research_file

load_dotenv()

class ResearchAgent:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY is missing from .env")
        
        genai.configure(api_key=api_key)
        
        # Defining the toolset (MCP-Compliant)
        self.tools = [web_search, save_research, list_past_research, read_research_file]
        
        self.model = genai.GenerativeModel(
            model_name='gemini-3.1-flash-lite',
            tools=self.tools
        )

    def run_research(self, topic: str):
        try:
            print(f"Agent starting deep-dive research: {topic}")
            
            # Start chat with automatic tool calling
            chat = self.model.start_chat(enable_automatic_function_calling=True)
            
            prompt = f"""
            Please conduct an ULTIMATE, ultra-deep research on: '{topic}'. 
            
            STRICT FORMATTING RULES:
            - DO NOT use asterisks (*) for any reason. 
            - DO NOT use double quotes (") anywhere in the report.
            - For headers, use ALL CAPS and a clear line break.
            - For bullet points, use a simple dash (-) or a bullet symbol (•).
            
            REPORT REQUIREMENTS:
            - This must be an extremely long and exhaustive report (minimum 3000 words to fill 3-5 pages).
            - Include deep technical data, global statistics, multi-industry impacts, and 5-year projections.
            - Sections: EXECUTIVE SUMMARY, HISTORICAL CONTEXT, TECHNICAL LANDSCAPE, MAJOR CHALLENGES, GLOBAL IMPACT, FUTURE PROJECTIONS, CASE STUDIES, CONCLUSION.
            
            Format the output clearly and professionally without any markdown-style asterisks.
            """
            
            response = chat.send_message(prompt)
            return response.text
            
        except Exception as e:
            print(f"AGENT ERROR: {e}")
            print(traceback.format_exc())
            return f"Research failed due to a system error: {str(e)}"
