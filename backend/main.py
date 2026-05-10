from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
import re
from .agent import ResearchAgent

# PDF Imports
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global agent instance
try:
    agent = ResearchAgent()
except Exception as e:
    print(f"Startup Warning: {e}")
    agent = None

class ResearchRequest(BaseModel):
    topic: str

@app.post("/research")
async def perform_research(request: ResearchRequest):
    if not agent:
        raise HTTPException(status_code=500, detail="API Key not configured in .env")
    
    try:
        report = agent.run_research(request.topic)
        
        # Save raw version for TXT export
        os.makedirs("research_exports", exist_ok=True)
        filename_base = "latest_report"
        txt_path = os.path.join("research_exports", f"{filename_base}.txt")
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(report)
            
        return {"report": report, "id": filename_base}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/export/txt/{report_id}")
async def export_txt(report_id: str):
    file_path = os.path.join("research_exports", f"{report_id}.txt")
    if os.path.exists(file_path):
        return FileResponse(path=file_path, filename=f"Research_Report.txt", media_type="text/plain")
    raise HTTPException(status_code=404, detail="Report not found")

@app.get("/export/pdf/{report_id}")
async def export_pdf(report_id: str):
    txt_path = os.path.join("research_exports", f"{report_id}.txt")
    pdf_path = os.path.join("research_exports", f"{report_id}.pdf")
    
    if not os.path.exists(txt_path):
        raise HTTPException(status_code=404, detail="Report not found")
        
    try:
        with open(txt_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Generate PDF
        doc = SimpleDocTemplate(pdf_path, pagesize=letter)
        styles = getSampleStyleSheet()
        
        # Custom styles
        body_style = ParagraphStyle('BodyStyle', parent=styles['Normal'], fontSize=11, leading=14, alignment=TA_JUSTIFY)
        header_style = ParagraphStyle('HeaderStyle', parent=styles['Heading2'], fontSize=14, spaceAfter=10)
        
        story = []
        story.append(Paragraph("<b>RESEARCH SYNTHESIS REPORT</b>", styles['Title']))
        story.append(Spacer(1, 12))
        
        # Process lines
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if not line:
                story.append(Spacer(1, 6))
                continue
            
            # 1. Strip any unwanted characters for a clean professional look
            line = line.replace('*', '').replace('"', '')
            
            # 2. Handle Headers (detect all-caps lines as headers if no # exists)
            if line.isupper() and len(line) > 5:
                story.append(Paragraph(f"<b>{line}</b>", header_style))
                continue
                
            if line.startswith('#'):
                clean_header = line.lstrip('#').strip()
                story.append(Paragraph(f"<b>{clean_header}</b>", header_style))
                continue
                
            # 3. Handle Lists
            if line.startswith('- '):
                line = "• " + line[2:]
                
            story.append(Paragraph(line, body_style))
        
        doc.build(story)
        
        return FileResponse(path=pdf_path, filename=f"Research_Report.pdf", media_type="application/pdf")
    except Exception as e:
        print(f"PDF ERROR: {e}")
        raise HTTPException(status_code=500, detail=f"PDF Generation Error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
