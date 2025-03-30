#!/usr/bin/env python
import sys
import warnings
from fastapi import FastAPI, UploadFile, File, Form, Body
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, Dict
import uvicorn
from datetime import datetime
from resume_optimisation.crew import ResumeCrew
from resume_optimisation.utils.extract_document import extract_text
import ast, os, shutil


warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

app = FastAPI(
    title="Resume Optimization API",
    description="API for analyzing resumes and job descriptions with customizable weights",
    version="1.0.0"
)

UPLOAD_DIR = "uploads"  
os.makedirs(UPLOAD_DIR, exist_ok=True) 

class WeightageInput(BaseModel):
    skill_match_weight: Optional[float] = None
    experience_weight: Optional[float] = None
    education_weight: Optional[float] = None
    certifications_weight: Optional[float] = None
    achievements_weight: Optional[float] = None
    projects_weight: Optional[float] = None
    location_weight: Optional[float] = None
    industry_weight: Optional[float] = None
    professional_activities_weight: Optional[float] = None
    publications_weight: Optional[float] = None


from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from typing import Optional
import shutil
import os
import json
import ast

app = FastAPI()

UPLOAD_DIR = "uploads"  # Directory for saving files
os.makedirs(UPLOAD_DIR, exist_ok=True)  # Ensure directory exists

@app.post("/analyze-resume")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: UploadFile = File(...),
    weights: Optional[str] = Form(None)
):
    try:
        resume_path = os.path.join(UPLOAD_DIR, resume.filename)
        jd_path = os.path.join(UPLOAD_DIR, job_description.filename)

        with open(resume_path, "wb") as buffer:
            shutil.copyfileobj(resume.file, buffer)
        with open(jd_path, "wb") as buffer:
            shutil.copyfileobj(job_description.file, buffer)

        # Default weights dictionary
        default_weights = {
            "weights_context": "Default weight distribution based on hiring preferences.",
            "skill_match_weight": 25,
            "experience_weight": 20,
            "education_weight": 15,
            "certifications_weight": 10,
            "achievements_weight": 5,
            "projects_weight": 10,
            "location_weight": 5,
            "industry_weight": 5,
            "professional_activities_weight": 3,
            "publications_weight": 2
        }
        
        # Copy default weights to custom_weights
        custom_weights = default_weights.copy()
        
        # Update with user-provided weights if any
        if weights:
            try:
                if weights.startswith("{") and weights.endswith("}"):  
                    user_weights = json.loads(weights)
                else:
                    user_weights = ast.literal_eval(weights)
                
                # Update only the keys provided in user_weights
                for k, v in user_weights.items():
                    if v is not None and k in custom_weights:
                        custom_weights[k] = f"{v}"
                    
            except (json.JSONDecodeError, SyntaxError, ValueError):
                return JSONResponse(
                    content={"status": "error", "message": "Invalid weights format"},
                    status_code=400
                )

        # Extract text from resume and job description
        resume_text = extract_text(resume_path)
        jd_text = extract_text(jd_path)

        # Cleanup files after extraction
        os.unlink(resume_path)
        os.unlink(jd_path)

        # Prepare input with resume, job description and weights
        base_input = {"resume_content": resume_text, "job_description_content": jd_text}
        input = base_input | custom_weights

        # Initialize CrewAI processing
        crew = ResumeCrew().resume_optimisation_crew()
        result = crew.kickoff(
            inputs=input
        )

        return JSONResponse(
            content={"status": "success", "data": result, "message": "Analysis completed successfully"},
            status_code=200
        )

    except Exception as e:
        return JSONResponse(
            content={"status": "error here", "message": str(e)},
            status_code=500
        )





@app.get("/health")
async def health_check():
    return {"status": "healthy"}

def run_api():
    """
    Run the FastAPI server
    """
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    run_api()