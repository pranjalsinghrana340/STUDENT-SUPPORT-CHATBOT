"""
Studentsupport_botProject — Official Academic & ERP AI Desk
ABES Engineering College, Ghaziabad (AKTU Code: 032)
FastAPI Main Application
"""

import os
from typing import List, Optional, Dict, Any
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from core.engine import StudentSupportEngine
from core.tools import StudentToolsService
from core.auth import AuthService
from data.abes_dataset import (
    COLLEGE_METADATA,
    LEADERSHIP,
    ANTI_RAGGING_COMMITTEE,
    ADMISSION_GUIDELINES,
    FACULTY_DIRECTORY,
    PLACEMENT_AND_CRC,
    CAMPUS_FACILITIES_EXTENDED,
    CAMPUS_PHOTOS,
    CAMPUS_BUILDING_BLOCKS,
    SPORTS_GROUNDS_DETAILED,
    FEE_INFORMATION,
    NOTICES,
    FAQS
)

app = FastAPI(
    title="Studentsupport_botProject — ABES Engineering College",
    description="Official AI Academic and Student Support Desk for ABES EC, Ghaziabad",
    version="2.2.0"
)

# Enable CORS for local testing and cross-origin tools
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static assets directory
static_dir = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")


# Pydantic Request Models
class ChatRequest(BaseModel):
    query: str
    context: Optional[List[dict]] = None

class StudyPlanRequest(BaseModel):
    subjects: List[str]
    exam_date: Optional[str] = "2026-05-15"
    daily_hours: Optional[float] = 3.0
    target_score: Optional[str] = "85%+ in Sessional & End-Sem"

class SummarizeRequest(BaseModel):
    filename: Optional[str] = "Lecture_Notes.pdf"
    content: str

class QuizRequest(BaseModel):
    subject: Optional[str] = "Data Structures & Algorithms"
    topic: Optional[str] = "Trees and Graphs"
    difficulty: Optional[str] = "Medium"
    count: Optional[int] = 4

class AssignmentRequest(BaseModel):
    subject: str
    question: str
    level: Optional[str] = "guided"

class ExamPrepRequest(BaseModel):
    subject: str
    exam_type: Optional[str] = "sessional"

class AuthLoginRequest(BaseModel):
    email: str
    password: str

class ERPLoginRequest(BaseModel):
    identifier: str
    password: str
    captcha_input: str
    captcha_token: str

class AuthSignupRequest(BaseModel):
    name: str
    email: str
    student_id: str
    department: str
    semester: int
    role: Optional[str] = "student"

class PublishNoticeRequest(BaseModel):
    title: str
    department: str
    category: str
    details: str
    badge: Optional[str] = "Notice"


# =========================================================================
# 1. ROOT WEB INTERFACE ROUTE (SERVES ABES ERP & BOT UI)
# =========================================================================
@app.api_route("/", methods=["GET", "HEAD"], response_class=HTMLResponse)
async def serve_index():
    index_path = os.path.join(static_dir, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return HTMLResponse("<h1>Studentsupport_botProject is running! Please check static/index.html</h1>")


# =========================================================================
# 2. CHATBOT API (FOCUSED ABES ACADEMIC REASONING ENGINE)
# =========================================================================
@app.post("/api/chat")
async def chat_endpoint(req: ChatRequest):
    """
    Main chat endpoint. Resolves admissions, director, COE, proctor,
    faculty, placements, library, canteens, hostels, fees, and coursework.
    """
    current_session = AuthService.get_current_session()
    actor_email = current_session["email"] if current_session else "guest.student@abes.ac.in"
    AuthService.log_security_event(
        "QUERY_PROCESSED",
        actor_email,
        f"Query: '{req.query[:45]}' -> {response_data.get('category')}"
    )
    return response_data


# =========================================================================
# 3. STUDENT ACADEMIC & FINANCIAL TOOLS (FORMS & PROCESSING)
# =========================================================================
@app.get("/api/tools/fee-calculator")
async def fee_calculator_endpoint(
    course: str = "B.Tech",
    year: int = 1,
    hostel_type: str = "none",
    bus_route: str = "none"
):
    """Calculates official tuition, exam fee, and optional hostel/bus fees."""
    return StudentToolsService.calculate_fees(course, year, hostel_type, bus_route)

@app.post("/api/tools/planner")
async def planner_endpoint(req: StudyPlanRequest):
    """Generates day-by-day revision schedule for AKTU examinations."""
    return StudentToolsService.generate_study_plan(req.subjects, req.exam_date, req.daily_hours, req.target_score)

@app.post("/api/tools/summarize")
async def summarize_endpoint(req: SummarizeRequest):
    """Extracts summary, key points, definitions, and 3D flashcards."""
    return StudentToolsService.summarize_notes(req.filename or "Notes", req.content)

@app.get("/api/tools/quiz")
async def quiz_endpoint(
    subject: str = "Data Structures & Algorithms",
    topic: str = "Trees and Graphs",
    difficulty: str = "Medium",
    count: int = 4
):
    """Returns practice MCQs with instant explanations and scoring."""
    return StudentToolsService.generate_quiz(subject, topic, difficulty, count)

@app.post("/api/tools/assignment")
async def assignment_endpoint(req: AssignmentRequest):
    """Deconstructs assignment questions into step-by-step guided instructions."""
    return StudentToolsService.solve_assignment(req.subject, req.question, req.level)

@app.post("/api/tools/exam-prep")
async def exam_prep_endpoint(req: ExamPrepRequest):
    """Generates high-yield exam preparation package with Quantum insights."""
    return StudentToolsService.generate_exam_prep(req.subject, req.exam_type)


# =========================================================================
# 4. UNIVERSITY INFORMATION & DATASET
# =========================================================================
@app.get("/api/info/dataset")
async def dataset_endpoint():
    """Returns comprehensive ABES Engineering College official dataset."""
    return {
        "metadata": COLLEGE_METADATA,
        "leadership": LEADERSHIP,
        "anti_ragging": ANTI_RAGGING_COMMITTEE,
        "admissions": ADMISSION_GUIDELINES,
        "faculty": FACULTY_DIRECTORY,
        "placements": PLACEMENT_AND_CRC,
        "facilities": CAMPUS_FACILITIES_EXTENDED,
        "building_blocks": CAMPUS_BUILDING_BLOCKS,
        "sports_grounds": SPORTS_GROUNDS_DETAILED,
        "photos": CAMPUS_PHOTOS,
        "fee_info": FEE_INFORMATION,
        "notices": NOTICES,
        "faqs": FAQS
    }

@app.get("/api/info/faculty")
async def faculty_endpoint(department: Optional[str] = None):
    """Returns faculty directory, optionally filtered by department."""
    if department:
        filtered = [f for f in FACULTY_DIRECTORY if f["dept_code"].lower() == department.lower()]
        return {"faculty": filtered}
    return {"faculty": FACULTY_DIRECTORY}

@app.get("/api/info/placements")
async def placements_endpoint():
    """Returns CRC placement stats, marquee recruiters, and training ecosystem."""
    return PLACEMENT_AND_CRC

@app.get("/api/info/campus-life")
async def campus_life_endpoint():
    """Returns library, canteens, sports grounds, building blocks, hostels, clubs, fests, and photo gallery."""
    return {
        "facilities": CAMPUS_FACILITIES_EXTENDED,
        "building_blocks": CAMPUS_BUILDING_BLOCKS,
        "sports_grounds": SPORTS_GROUNDS_DETAILED,
        "photos": CAMPUS_PHOTOS
    }

@app.get("/api/info/building-blocks")
async def building_blocks_endpoint():
    """Returns all campus building blocks with real photos, facilities, and departments."""
    return {"building_blocks": CAMPUS_BUILDING_BLOCKS}

@app.get("/api/info/sports-grounds")
async def sports_grounds_endpoint():
    """Returns all sports grounds, stadium, floodlit courts, gymnasiums, and swimming pool."""
    return {"sports_grounds": SPORTS_GROUNDS_DETAILED}

@app.get("/api/info/admissions")
async def admissions_endpoint():
    """Returns complete B.Tech, MCA, and MBA admission guidelines and documents."""
    return ADMISSION_GUIDELINES


# =========================================================================
# 5. AUTHENTICATION & ADMIN GOVERNANCE
# =========================================================================
@app.get("/api/auth/captcha")
async def get_captcha_endpoint():
    """Generates a secure 4-character anti-bot captcha code and token."""
    return AuthService.generate_captcha()

@app.post("/api/auth/erp-login")
async def erp_login_endpoint(req: ERPLoginRequest):
    """Secure ABES SIMS ERP Login with Roll Number, Password, and Captcha."""
    return AuthService.erp_login(req.identifier, req.password, req.captcha_input, req.captcha_token)

@app.get("/api/auth/profile")
async def get_profile_endpoint():
    """Returns active student ERP profile, or guest state."""
    session = AuthService.get_current_session()
    if session:
        return {"is_authenticated": True, "user": session}
    return {"is_authenticated": False, "user": None, "message": "Guest student session"}

@app.post("/api/auth/logout")
async def logout_endpoint():
    """Terminates active SIMS session."""
    return AuthService.logout()

@app.get("/api/admin/metrics")
async def admin_metrics_endpoint():
    """Admin dashboard stats, query counts, and security audit trail."""
    return {
        "total_students": 5420,
        "active_today": 3410,
        "satisfaction": "98.4%",
        "recent_logs": AuthService.get_logs()
    }

@app.post("/api/admin/publish-notice")
async def publish_notice_endpoint(req: PublishNoticeRequest):
    """Adds a real-time notice to the active college notice board."""
    new_notice = {
        "id": f"not-user-{len(NOTICES) + 1}",
        "title": req.title,
        "date": "2026-04-01",
        "department": req.department,
        "category": req.category,
        "badge": req.badge or "Notice",
        "details": req.details
    }
    NOTICES.insert(0, new_notice)
    AuthService.log_security_event("NOTICE_PUBLISHED", "admin.desk@abes.ac.in", f"Published: {req.title}")
    return {"success": True, "notice": new_notice, "all_notices": NOTICES}


# =========================================================================
# 6. STANDALONE RUNNER
# =========================================================================
if __name__ == "__main__":
    import uvicorn
    print("\n" + "="*70)
    print("🎓 Studentsupport_botProject — ABES EC Official AI Academic Desk")
    print("="*70)
    print("🚀 Starting Server on: http://localhost:8000")
    print("📚 API Documentation: http://localhost:8000/docs")
    print("="*70 + "\n")
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
