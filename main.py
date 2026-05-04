from risk_engine import assess_risk
from agent_service import analyze_with_agent
from llm_service import generate_modern_code
from checklist import generate_checklist
from fastapi import HTTPException
from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI()

reports = {}

from pydantic import BaseModel, Field

class AnalyzeRequest(BaseModel):

    language: str = Field(..., min_length=1)
    module_name: str = Field(..., min_length=1)
    code_snippet: str = Field(..., min_length=1)

@app.get("/")
def home():

    return {
        "app": "AI Legacy Modernization Agent",
        "status": "RUNNING",
        "version": "1.0"
    }

@app.post("/analyze")
def analyze(request: AnalyzeRequest):

    snippet_id = str(uuid.uuid4())

    risk = assess_risk(request.code_snippet)

    llm_result = analyze_with_agent(request.code_snippet)

    response = {
        "snippet_id": snippet_id,
        "summary": llm_result["summary"],
        "identified_patterns": llm_result["identified_patterns"],
        "complexity_score": llm_result["complexity_score"],
        "language_detected": llm_result["language_detected"],
        "risk_assessment": risk
    }

    reports[snippet_id] = {
        "request": request.dict(),
        "analysis": response
    }

    return response

@app.post("/migrate/{snippet_id}")
def migrate(snippet_id: str):

    if snippet_id not in reports:
        raise HTTPException(
            status_code=404,
            detail="Snippet not found"
        )

    stored_data = reports[snippet_id]

    request_data = stored_data["request"]
    analysis_data = stored_data["analysis"]

    code = request_data["code_snippet"]

    modern_code = generate_modern_code(code)

    checklist = generate_checklist(code)

    risk_level = analysis_data["risk_assessment"]["risk_level"]

    if risk_level == "CRITICAL":
        migration_status = "BLOCKED"
    elif risk_level in ["HIGH", "MEDIUM"]:
        migration_status = "NEEDS_REVIEW"
    else:
        migration_status = "READY"

    report = {
        "snippet_id": snippet_id,
        "original_language": request_data["language"],
        "module_name": request_data["module_name"],
        "analysis": {
            "summary": analysis_data["summary"],
            "patterns": analysis_data["identified_patterns"],
            "complexity": analysis_data["complexity_score"]
        },
        "risk_assessment": analysis_data["risk_assessment"],
        "modernized_code": modern_code,
        "migration_checklist": checklist,
        "target_framework": "FastAPI",
        "migration_status": migration_status
    }

    reports[snippet_id]["migration_report"] = report

    return report

@app.get("/report/{snippet_id}")
def get_report(snippet_id: str):

    if snippet_id not in reports:
        raise HTTPException(
            status_code=404,
            detail="Snippet not found"
        )

    report = reports[snippet_id].get("migration_report")

    if not report:
        raise HTTPException(
            status_code=400,
            detail="Migration report not generated yet"
        )

    return report

@app.get("/patterns")
def get_patterns():

    return [
        {
            "name": "HARDCODED_CONFIG",
            "description": "Hardcoded credentials or connection strings"
        },
        {
            "name": "RAW_SQL",
            "description": "Direct SQL queries without parameterization"
        },
        {
            "name": "NO_ERROR_HANDLING",
            "description": "Missing exception handling logic"
        },
        {
            "name": "MAGIC_NUMBER",
            "description": "Hardcoded unexplained numeric values"
        },
        {
            "name": "TIGHT_COUPLING",
            "description": "Strong dependency between modules"
        }
    ]