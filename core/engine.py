r"""
Studentsupport_botProject — Core AI Reasoning & Institutional RAG Engine
ABES Engineering College, Ghaziabad (AKTU Code 032)
"""

import re
import json
from typing import Dict, Any, List, Optional
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

class StudentSupportEngine:
    """
    Intelligent student assistance engine providing focused, accurate, 
    and institution-specific answers for ABES Engineering College.
    """

    @classmethod
    def get_focused_response(cls, query: str, context: Optional[List[Dict[str, str]]] = None) -> Dict[str, Any]:
        """
        Processes a student query and generates an authoritative, focused response.
        """
        q = query.strip().lower()

        # -------------------------------------------------------------
        # 1. ADMISSION PROCESS & ELIGIBILITY (UPTAC, JEE MAIN, DIRECT)
        # -------------------------------------------------------------
        if any(w in q for w in ["admission", "addmission", "admit", "counseling", "uptac", "management quota", "direct admission", "how to join", "eligibility"]):
            doc_list = "\n".join([f"* 📄 {doc}" for doc in ADMISSION_GUIDELINES["documents_required"][:6]])
            return {
                "category": "Admissions & Counseling",
                "answer": (
                    "### 🎓 Official B.Tech Admission Process — ABES Engineering College (AKTU Code: 032)\n\n"
                    "ABES Engineering College offers B.Tech, MCA, and MBA admissions through two official channels:\n\n"
                    "---\n\n"
                    "#### 1️⃣ **Channel 1: UPTAC Counseling (85% Total Seats)**\n"
                    "* **Eligibility:** Valid **JEE Main** score/rank.\n"
                    "* **Procedure:**\n"
                    "  1. Register on the official UPTAC counseling portal (`uptac.admissions.nic.in`).\n"
                    "  2. In choice filling, select **`ABES Engineering College, Ghaziabad (College Code: 032)`** as top preference.\n"
                    "  3. After seat allotment, download the provisional allotment letter and report to campus for document verification and fee payment.\n\n"
                    "#### 2️⃣ **Channel 2: Direct Admission / Management Quota (15% Seats)**\n"
                    "* **Eligibility Criteria:** Passed 10+2 examination with minimum **45% aggregate** (40% for SC/ST category) in Physics and Mathematics as compulsory subjects, plus one optional subject (Chemistry / Computer Science / IT / Biology).\n"
                    "* **Procedure:**\n"
                    "  1. Apply online via the official portal: [https://erp.abes.ac.in/onlineregistration/](https://erp.abes.ac.in/onlineregistration/)\n"
                    "  2. Or visit the **Admission Cell physically** in Bhabha Block Room 002.\n"
                    "  3. Appear for the institutional technical screening assessment and personal interview.\n"
                    "  4. Confirm seat by depositing the initial admission registration fee.\n\n"
                    "---\n\n"
                    "#### 📋 Key Documents Required at Reporting:\n"
                    f"{doc_list}\n"
                    "* *(Plus Transfer Certificate, Migration, Medical Fitness & 6 Passport photos).*\n\n"
                    "📞 **Admission Helpdesk:** Ground Floor, Bhabha Block (Room 002) | Phone: `+91-120-7135111 / 7135112` | Mobile: `+91-9999889341` | Email: `admissions@abes.ac.in`"
                ),
                "suggested_actions": ["B.Tech Fee Structure", "Hostel Fees", "Online Registration Link", "Placement Records"]
            }

        # -------------------------------------------------------------
        # 2. DIRECTOR & EXECUTIVE LEADERSHIP
        # -------------------------------------------------------------
        if any(w in q for w in ["director", "director name", "principal", "head of college", "director general", "shri neeraj goel", "shashwat goel"]):
            dir_info = LEADERSHIP["director"]
            return {
                "category": "College Administration",
                "answer": (
                    "### 🏛️ Executive Leadership & Directorate — ABES Engineering College\n\n"
                    f"#### 🎓 **Director of the College:**\n"
                    f"* **Name:** **{dir_info['name']}**\n"
                    f"* **Designation:** {dir_info['designation']}\n"
                    f"* **Academic Qualifications:** {dir_info['qualification']}\n"
                    f"* **Experience:** {dir_info['experience']}\n"
                    f"* **Office Location:** {dir_info['office']}\n"
                    f"* **Official Email:** `{dir_info['email']}`\n\n"
                    "---\n\n"
                    "#### 🌟 **Governing Society Leadership:**\n"
                    f"* **Chairman (SEE):** **{LEADERSHIP['chairman']['name']}** — {LEADERSHIP['chairman']['message']}\n"
                    f"* **General Secretary:** **{LEADERSHIP['general_secretary']['name']}** — {LEADERSHIP['general_secretary']['message']}\n\n"
                    "---\n\n"
                    "#### 👥 **Key Administrative Officers:**\n"
                    f"* **Controller of Examinations (COE):** **{LEADERSHIP['controller_of_examinations']['name']}** (Ramanujan Block Room 104)\n"
                    f"* **Chief Proctor:** **{LEADERSHIP['chief_proctor']['name']}** (Aryabhatta Block Room 004)\n"
                    f"* **Registrar:** **{LEADERSHIP['registrar']['name']}** (Ramanujan Block 1st Floor)\n"
                    f"* **Head of CRC (Placements):** {LEADERSHIP['head_crc']['office']}\n"
                ),
                "suggested_actions": ["Controller of Examination Details", "Chief Proctor & Anti-Ragging", "Faculty Directory", "Accounts Office"]
            }

        # -------------------------------------------------------------
        # 3. CONTROLLER OF EXAMINATIONS (COE) & EXAM CELL
        # -------------------------------------------------------------
        if any(w in q for w in ["controller of examination", "examination controller", "coe", "exam controller", "examination head", "exam cell"]):
            coe = LEADERSHIP["controller_of_examinations"]
            return {
                "category": "Examinations & Governance",
                "answer": (
                    "### 📝 Controller of Examinations (COE) — ABES Engineering College\n\n"
                    f"* **Name:** **{coe['name']}**\n"
                    f"* **Designation:** {coe['designation']}\n"
                    f"* **Qualification:** {coe['qualification']}\n"
                    f"* **Experience:** {coe['experience']}\n"
                    f"* **Office:** {coe['office']}\n"
                    f"* **Email:** `{coe['email']}`\n\n"
                    "#### 🎯 Key Examination Responsibilities:\n"
                    "* Superintends the smooth conduct of AKTU End-Semester theory & practical examinations.\n"
                    "* Oversees internal Sessional Tests (ST-1, ST-2) and Pre-University Exams (PUE).\n"
                    "* Generation and distribution of AKTU examination admit cards and attendance verification.\n"
                    "* Processing of Carry Over Papers (COP) and scrutiny challenge evaluation forms.\n\n"
                    "📍 **Exam Cell Counter:** Ground Floor, Ramanujan Block (Ext. 115)."
                ),
                "suggested_actions": ["Sessional Exam Pattern", "AKTU COP Process", "Attendance 75% Rule"]
            }

        # -------------------------------------------------------------
        # 4. ANTI-RAGGING COMMITTEE & CHIEF PROCTOR
        # -------------------------------------------------------------
        if any(w in q for w in ["anti ragging", "antiragging", "ragging", "harassment", "chief proctor", "proctor", "discipline"]):
            ar = ANTI_RAGGING_COMMITTEE
            return {
                "category": "Discipline & Student Safety",
                "answer": (
                    "### 🛡️ Anti-Ragging Committee & Proctorial Board (ABES EC)\n\n"
                    f"* **Head of Anti-Ragging Committee & Chief Proctor:** **{ar['head']}**\n"
                    f"* **Campus Proctor Office:** Aryabhatta Block, Ground Floor (Room 003/004)\n"
                    f"* **Campus Emergency Desk:** `{ar['campus_helpline']}`\n"
                    f"* **Official Anti-Ragging Email:** `{ar['email']}`\n"
                    f"* **National Anti-Ragging 24x7 Toll-Free Helpline:** `{ar['national_helpline_toll_free']}`\n\n"
                    "---\n\n"
                    "> 🚨 **STRICT ZERO TOLERANCE POLICY:**\n"
                    "> In strict compliance with Hon'ble Supreme Court directives and AICTE regulations, **ragging is a non-bailable cognizable criminal offense**. "
                    "Any student found guilty faces immediate suspension, expulsion from hostel, cancellation of AKTU admission, and registration of a police FIR.\n\n"
                    "#### 📝 Mandatory Online Affidavit:\n"
                    f"Every student and parent must fill the annual anti-ragging undertaking at [www.antiragging.in](https://www.antiragging.in) and submit the reference number to the Proctor Office."
                ),
                "suggested_actions": ["Submit Medical Slip", "Attendance Criteria", "Campus Security"]
            }

        # -------------------------------------------------------------
        # 5. CORPORATE RESOURCE CENTRE (CRC) & PLACEMENTS
        # -------------------------------------------------------------
        if any(w in q for w in ["placement", "placements", "crc", "companies", "highest package", "average package", "package", "ctc", "recruiters", "training", "crt", "cpd", "hcl", "amazon"]):
            crc = PLACEMENT_AND_CRC
            stats = crc["key_statistics"]
            rec_rows = "\n".join([f"| **{r['company']}** | {r['ctc']} | {r['role']} |" for r in crc["marquee_recruiters"][:6]])
            
            return {
                "category": "Corporate Resource Centre (Placements)",
                "answer": (
                    "### 💼 Corporate Resource Centre (CRC) & Campus Placements\n\n"
                    "The Corporate Resource Centre (CRC) at ABES EC leads campus recruitment, student readiness, and industry alliances:\n\n"
                    f"* 🏆 **Highest Package:** **{stats['highest_package']}**\n"
                    f"* 📈 **Average Package:** **{stats['average_package']}** | **Median:** {stats['median_package']}\n"
                    f"* 🎯 **Total Offers:** **{stats['total_offers']}** from **{stats['visiting_companies']}**\n"
                    f"* 🌟 **Super Dream Offers ($\\ge$ 10 LPA):** **{stats['super_dream_offers']}**\n"
                    f"* 📊 **Overall Placement Rate:** **{stats['overall_placement_rate']}**\n\n"
                    "---\n\n"
                    "#### 🏢 Marquee Visiting Companies & CTC Packages:\n"
                    "| Recruiter | Package Range | Core Designation |\n"
                    "|---|---|---|\n"
                    f"{rec_rows}\n\n"
                    "---\n\n"
                    "#### 🚀 How Faculty & CRC Train and Encourage Students:\n"
                    f"1. **{crc['training_ecosystem']['crt_program']}**\n"
                    f"2. **{crc['training_ecosystem']['cpd_program']}**\n"
                    f"3. **{crc['training_ecosystem']['coding_bootcamps']}**\n"
                    f"4. **{crc['training_ecosystem']['faculty_mentoring']}**\n\n"
                    "📍 **CRC Office:** 2nd Floor, Aryabhatta Block | Email: `crchead@abes.ac.in`"
                ),
                "suggested_actions": ["Generate Technical Quiz", "Study Planner", "HCL Drive Details", "Campus Hub"]
            }

        # -------------------------------------------------------------
        # 6. FACULTY & DEPARTMENT LEADERSHIP DIRECTORY
        # -------------------------------------------------------------
        if any(w in q for w in ["faculty", "professors", "teachers", "hod", "who teaches", "department staff", "experience"]):
            fac_cards = []
            for f in FACULTY_DIRECTORY:
                fac_cards.append(
                    f"#### 👨‍🏫 **{f['name']}** — {f['department']}\n"
                    f"* **Designation:** {f['designation']}\n"
                    f"* **Qualifications:** {f['qualification']} | **Experience:** {f['experience']}\n"
                    f"* **Subjects Taught:** {', '.join(f['subjects'])}\n"
                    f"* **Research Specialization:** {f['research_area']}\n"
                    f"* **Office:** {f['room']} | ✉️ `{f['email']}`\n"
                )
            
            return {
                "category": "Faculty Directory",
                "answer": (
                    "### 👥 ABES EC Distinguished Department Heads & Faculty\n\n"
                    "Here are the senior academic leaders and department heads across our engineering divisions:\n\n"
                    + "\n".join(fac_cards) +
                    "\n> *Faculty members maintain daily student mentoring consultation hours between 3:30 PM and 4:30 PM.*"
                ),
                "suggested_actions": ["Campus Hub", "Central Library", "Controller of Examinations", "Director Info"]
            }

        # -------------------------------------------------------------
        # 7. CENTRAL LIBRARY, BOOK BANK & E-RESOURCES
        # -------------------------------------------------------------
        if any(w in q for w in ["library", "books", "book bank", "library timing", "ieee", "delnet", "reading hall"]):
            lib = CAMPUS_FACILITIES_EXTENDED["central_library"]
            return {
                "category": "Library & Academic Resources",
                "answer": (
                    f"### 📚 {lib['name']} — ABES Engineering College\n\n"
                    "![Central Library](https://images.unsplash.com/photo-1521587760476-6c12a4b040da?auto=format&fit=crop&w=1000&q=80)\n\n"
                    f"* 📍 **Location:** {lib['location']}\n"
                    f"* ⏰ **Regular Hours:** {lib['timings']}\n"
                    f"* 📖 **Exam Extended Hours:** Open till **11:00 PM** during Sessional and End-Sem exams!\n"
                    f"* 📊 **Physical Holdings:** {lib['collection_size']}\n\n"
                    "---\n\n"
                    "#### 🎁 **Free Semester Book Bank Scheme:**\n"
                    f"{lib['book_bank_scheme']}\n\n"
                    "#### 💻 **Digital Library & International E-Resources:**\n"
                    f"* {lib['digital_resources']}\n"
                    "* High-speed multimedia terminals and automated RFID book issue kiosks.\n"
                    f"* {lib['reading_capacity']}\n\n"
                    f"📞 **Helpdesk:** {lib['librarian_helpdesk']}"
                ),
                "suggested_actions": ["Download Quantum Series", "Campus Facilities", "Study Planner", "Wi-Fi Portal"]
            }

        # -------------------------------------------------------------
        # 8. CANTEENS, FOOD COURT & FOOD OUTLETS
        # -------------------------------------------------------------
        if any(w in q for w in ["canteen", "cafeteria", "food", "nescafe", "amul", "lunch", "snacks", "chatori gali"]):
            dining = CAMPUS_FACILITIES_EXTENDED["canteens_and_dining"]
            cards = []
            for d in dining:
                cards.append(
                    f"#### 🍽️ **{d['name']}** ({d['location']})\n"
                    f"* **Hours:** {d['timings']}\n"
                    f"* **Popular Menu:** {d['menu']}\n"
                )

            return {
                "category": "Dining & Campus Life",
                "answer": (
                    "### 🍕 Canteens, Cafeterias & Food Spots at ABES EC\n\n"
                    "![Campus Dining](https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=1000&q=80)\n\n"
                    "ABES EC offers multiple vibrant hygienic dining destinations on campus:\n\n"
                    + "\n".join(cards) +
                    "\n> *All campus food outlets operate under strict FSSAI quality inspections and maintain cashless UPI payment counters.*"
                ),
                "suggested_actions": ["Hostel Mess Menu", "Sports Facilities", "Campus Map", "Library Timings"]
            }

        # -------------------------------------------------------------
        # 9. HOSTELS, MESS MENU & RESIDENCE RULES
        # -------------------------------------------------------------
        if any(w in q for w in ["hostel", "mess", "warden", "room", "food in hostel", "curfew", "night pass", "hostels"]):
            h = CAMPUS_FACILITIES_EXTENDED["hostels_and_mess"]
            sched = h["mess_schedule"]
            return {
                "category": "Hostel Life & Mess",
                "answer": (
                    "### 🏠 ABES EC Hostels, Dining & Mess Services\n\n"
                    "![Hostel Living](https://images.unsplash.com/photo-1555854877-bab0e564b8d5?auto=format&fit=crop&w=1000&q=80)\n\n"
                    "* **Boys Hostels:** Dayanand Bhawan and Vivekanand Bhawan.\n"
                    "* **Girls Hostels:** Saraswati Bhawan and Kasturba Bhawan.\n"
                    f"* ⏰ **Curfew & In-Campus Entry:** **{h['curfew_timings']}**\n"
                    f"* ⚡ **Amenities:** {h['amenities']}\n\n"
                    "---\n\n"
                    "#### 🍱 Daily 4-Meal Mess Schedule:\n"
                    f"* 🍳 **Breakfast (7:30 AM – 9:00 AM):** {sched['breakfast']}\n"
                    f"* 🍛 **Lunch (12:30 PM – 2:00 PM):** {sched['lunch']}\n"
                    f"* ☕ **Evening Snacks (5:00 PM – 6:00 PM):** {sched['evening_tea']}\n"
                    f"* 🍲 **Dinner (8:00 PM – 9:30 PM):** {sched['dinner']}\n"
                    f"* 🍨 **{sched['sunday_special']}**\n\n"
                    "#### 🚪 Night Out Pass Procedure:\n"
                    "Submit application 24 hours in advance on the **ABES ERP Hostel Portal**. Pass is issued automatically upon parent SMS confirmation."
                ),
                "suggested_actions": ["Fee Calculator (Hostel)", "Canteen Outlets", "Chief Warden Office", "Campus Sports"]
            }

        # -------------------------------------------------------------
        # 9B. CAMPUS BUILDING BLOCKS DIRECTORY (REAL PHOTOS & NAMES)
        # -------------------------------------------------------------
        if any(w in q for w in ["block", "blocks", "building", "buildings", "bhabha", "aryabhatta", "ramanujan", "kalpana chawla", "vishwakarma", "campus map"]):
            blocks_text = "\n\n".join([
                f"#### 🏛️ **{b['name']}**\n"
                f"![{b['name']}]({b['image']})\n"
                f"* **Departments & Offices:** {b['departments']}\n"
                f"* **Key Facilities:** {', '.join(b['key_facilities'])}\n"
                f"* **Summary:** {b['description']}"
                for b in CAMPUS_BUILDING_BLOCKS
            ])
            return {
                "category": "Campus Infrastructure & Building Blocks",
                "answer": (
                    "### 🏛️ Official Building Blocks of ABES Engineering College\n\n"
                    "ABES EC campus is organized into distinct state-of-the-art academic, administrative, and research blocks:\n\n"
                    f"{blocks_text}"
                ),
                "suggested_actions": ["Sports Grounds", "Central Library", "Hostels & Mess", "Admissions 2026"]
            }

        # -------------------------------------------------------------
        # 9C. SPORTS GROUNDS, STADIUM & RECREATION AREA
        # -------------------------------------------------------------
        if any(w in q for w in ["ground", "grounds", "cricket ground", "cricket stadium", "stadium", "sports ground", "football ground", "basketball court", "tennis court", "running track", "play ground"]):
            grounds_text = "\n\n".join([
                f"#### ⚽ **{g['name']}** ({g['category']})\n"
                f"![{g['name']}]({g['image']})\n"
                f"* **Dimensions & Surface:** {g['dimensions']}\n"
                f"* **Highlights:** {'; '.join(g['features'])}\n"
                f"* ⏰ **Timings:** {g['timings']}"
                for g in SPORTS_GROUNDS_DETAILED
            ])
            return {
                "category": "Sports Grounds & Stadiums",
                "answer": (
                    "### 🏟️ ABES EC Sports Grounds, Floodlit Stadium & Outdoor Arenas\n\n"
                    "ABES Engineering College offers premier sports infrastructure across 15+ acres, encouraging physical fitness, university tournaments, and inter-branch leagues:\n\n"
                    f"{grounds_text}\n\n"
                    "---\n"
                    "🏆 **Annual Flagship Event:** *Chakravyuh* — The annual inter-college sports festival hosting 50+ universities across NCR in cricket, football, basketball, and athletics."
                ),
                "suggested_actions": ["Cricket Stadium Schedule", "Gymnasium Timings", "Building Blocks", "Annual Fests"]
            }

        # -------------------------------------------------------------
        # 9D. AKTU ONEVIEW PORTAL & RESULTS INTENT (WORKING SOLUTION)
        # -------------------------------------------------------------
        if any(w in q for w in ["oneview", "one view", "aktu result", "result", "results", "marksheet", "grade card", "sgpa", "cgpa"]):
            return {
                "category": "University Examinations & Results",
                "answer": (
                    "### 🎓 AKTU OneView Portal & Examination Results Access\n\n"
                    "#### ⚠️ Note on 403 Forbidden Access Denied Error:\n"
                    "If you encounter **403 Forbidden: Access is denied** when clicking AKTU OneView, it is because Microsoft IIS web servers block direct root directory access at `https://oneview.aktu.ac.in`.\n\n"
                    "✅ **Official Working Link:** Access the exact ASPX endpoint directly:\n"
                    "* 🌐 **Direct OneView URL:** [https://oneview.aktu.ac.in/WebPages/AKTU/OneView.aspx](https://oneview.aktu.ac.in/WebPages/AKTU/OneView.aspx)\n\n"
                    "---\n\n"
                    "#### 📋 Step-by-Step Instructions to View Your Results:\n"
                    "1. Click the verified link: [AKTU OneView Portal](https://oneview.aktu.ac.in/WebPages/AKTU/OneView.aspx).\n"
                    "2. Enter your **13-digit University Roll Number** (e.g., `210032010xxxx` / `220032010xxxx`).\n"
                    "3. Enter the security captcha shown on the screen.\n"
                    "4. Click **Search / View Result** to display your semester-wise marks, SGPA, CGPA, and total credits earned.\n\n"
                    "💡 **Internal Sessional Results:** For internal test scores and pre-university test (PUT) marks, please check the **ABES SIMS ERP Portal** inside the student dashboard!"
                ),
                "suggested_actions": ["Open Working AKTU OneView", "ABES SIMS ERP", "COE Office Details", "Fee Clearance"]
            }

        # -------------------------------------------------------------
        # 10. CLUBS, SPORTS, AUDITORIUM & ANNUAL FESTS
        # -------------------------------------------------------------
        if any(w in q for w in ["club", "clubs", "sports", "fest", "genero", "technovacion", "chakravyuh", "auditorium", "cricket", "gym", "swimming pool", "dance", "music"]):
            aud = CAMPUS_FACILITIES_EXTENDED["auditorium"]
            sp = CAMPUS_FACILITIES_EXTENDED["sports_and_fitness"]
            clubs = CAMPUS_FACILITIES_EXTENDED["student_clubs"]
            fests = CAMPUS_FACILITIES_EXTENDED["annual_festivals"]

            club_list = "\n".join([f"* 🎭 **{c['name']}** ({c['category']}): {c['focus']}" for c in clubs[:5]])
            fest_list = "\n".join([f"* 🎪 **{f['name']}** ({f['type']}): {f['description']}" for f in fests])

            return {
                "category": "Extracurriculars, Sports & Clubs",
                "answer": (
                    "### 🏟️ Campus Life: Clubs, Sports, Auditorium & Festivals\n\n"
                    "![Auditorium](https://images.unsplash.com/photo-1511578314322-379afb476865?auto=format&fit=crop&w=1000&q=80)\n\n"
                    f"#### 🏛️ **{aud['name']}**\n"
                    f"* **Capacity:** {aud['capacity']} | Centrally air-conditioned with Dolby acoustics.\n"
                    f"* **Events Hosted:** {aud['events']}\n\n"
                    "---\n\n"
                    "#### ⚽ **Sports Infrastructure:**\n"
                    f"* **Outdoor:** {sp['outdoor_sports']}\n"
                    f"* **Indoor & Fitness:** {sp['indoor_sports']}\n"
                    f"* **Gymnasiums:** {sp['gymnasiums']}\n"
                    f"* **Aquatics:** {sp['swimming_pool']}\n\n"
                    "---\n\n"
                    "#### 🎨 **Active Student Clubs:**\n"
                    f"{club_list}\n\n"
                    "#### 🎆 **Annual Flagship Festivals:**\n"
                    f"{fest_list}\n"
                ),
                "suggested_actions": ["Auditorium Schedule", "Canteen Outlets", "Campus Facilities", "Faculty Directory"]
            }

        # -------------------------------------------------------------
        # 11. FEE SUBMISSION & ACCOUNTS INTENT (EXACT INSTITUTIONAL DATES)
        # -------------------------------------------------------------
        if any(w in q for w in ["fee", "fees", "fine", "tuition", "due date", "last date", "deadline", "pay fee", "late fee"]):
            if any(w in q for w in ["last date", "deadline", "submit", "submission", "due", "when"]):
                return {
                    "category": "Fees & Accounts",
                    "answer": (
                        "### 📅 Official Fee Submission Deadlines — ABES Engineering College (Code 032)\n\n"
                        "Here are the official cutoff dates for academic and hostel fee deposit for the current academic session:\n\n"
                        "---\n\n"
                        "#### 1️⃣ **Odd Semester (1st, 3rd, 5th, 7th Semesters)**\n"
                        "* **Without Late Fee:** **July 31, 2025**\n"
                        "* **With Late Fee (Phase 1):** August 01 - August 10, 2025 (Late fee of ₹50/- per day)\n"
                        "* **With Late Fee (Phase 2):** August 11 - August 25, 2025 (Late fee of ₹100/- per day)\n"
                        "* ⚠️ **Strict Debarment Cutoff:** August 26, 2025 (Names struck off roll list / attendance debarred)\n\n"
                        "#### 2️⃣ **Even Semester (2nd, 4th, 6th, 8th Semesters)**\n"
                        "* **Without Late Fee:** **January 20, 2026**\n"
                        "* **With Late Fee (Phase 1):** January 21 - January 31, 2026 (Late fee of ₹50/- per day)\n"
                        "* **With Late Fee (Phase 2):** February 01 - February 15, 2026 (Late fee of ₹100/- per day)\n"
                        "* ⚠️ **Strict Debarment Cutoff:** February 16, 2026 (Debarment from Sessional Tests)\n\n"
                        "---\n\n"
                        "### 💳 How to Pay Your Fees:\n"
                        "1. **Online via ABES ERP Portal (Recommended):**\n"
                        "   * Visit: [https://erp.abes.ac.in](https://erp.abes.ac.in) or [https://abes.webapps.net.in](https://abes.webapps.net.in)\n"
                        "   * Log in using your **College Admission Number / Student Roll Number** and ERP password.\n"
                        "   * Navigate to **Fee Management $\\rightarrow$ Online Fee Payment** to pay via Debit Card, Credit Card, or Net Banking.\n"
                        "2. **Via RTGS / NEFT (Direct Bank Transfer):**\n"
                        "   * **Bank Name:** Punjab National Bank (PNB)\n"
                        "   * **Branch:** Navyug Market, Ghaziabad\n"
                        "   * **Account Name:** ABES Engineering College\n"
                        "   * **Account Number:** `0674009300045934`\n"
                        "   * **IFSC Code:** `PUNB0067400`\n"
                        "   * *(After transfer, submit the UTR slip at the Accounts Office, Bhabha Block Room 004).*\n\n"
                        "---\n\n"
                        "> 🚨 **CRITICAL COLLEGE WARNING — CASH & CHEQUE STRICTLY PROHIBITED:**  \n"
                        "> In accordance with ABES EC financial regulations, **cash and cheque payments are not accepted**. "
                        "Depositing cash directly at the bank counter incurs a **penalty fine of ₹10,000/-**.\n\n"
                        "📞 **Accounts Office Helpdesk:** Ground Floor, Bhabha Block (Room 004) | Email: `accounts@abes.ac.in` | Intercom: Ext. 104 / 105\n"
                    ),
                    "suggested_actions": ["B.Tech Fee Breakdown", "Hostel Fee Details", "Open ABES ERP Portal", "Fee Calculator Tool"]
                }
            
            # General Fee Breakdown
            return {
                "category": "Fees & Accounts",
                "answer": (
                    "### 💰 ABES Engineering College — B.Tech Annual Fee Structure\n\n"
                    "| Component | 1st Year (New Admission) | 2nd, 3rd & 4th Year |\n"
                    "|---|---|---|\n"
                    "| **Tuition Fee** | ₹1,10,000/- | ₹1,10,000/- |\n"
                    "| **Career Planning & Development (CPD)** | ₹36,000/- | ₹36,000/- |\n"
                    "| **Technology & Digital Learning** | ₹6,000/- | ₹6,000/- |\n"
                    "| **University Exam & Enrollment Fee** | ₹9,600/- | ₹9,600/- |\n"
                    "| **Caution Money (Refundable)** | ₹5,000/- | *Nil* |\n"
                    "| **Total Annual Academic Fee** | **₹1,66,600/-** | **₹1,61,600/-** |\n\n"
                    "*(Note: Optional Hostel Fee ranges from ₹1,00,000/- to ₹1,30,000/-, and Bus pass from ₹26,000/- to ₹34,000/- based on route).*\n\n"
                    "Payment must be made online via [https://erp.abes.ac.in](https://erp.abes.ac.in) or PNB NEFT/RTGS (`0674009300045934`)."
                ),
                "suggested_actions": ["Last Date of Fee Submission", "Hostel Fee Tiers", "Fee Calculator Tool", "Accounts Office Contact"]
            }

        # -------------------------------------------------------------
        # 12. ATTENDANCE & PROCTORIAL REGULATIONS
        # -------------------------------------------------------------
        if any(w in q for w in ["attendance", "shortage", "debar", "medical slip", "medical certificate"]):
            return {
                "category": "Academic Regulations",
                "answer": (
                    "### 📊 Attendance Rules & Medical Concession Policy (AKTU & ABES EC)\n\n"
                    "1. **Mandatory Minimum Attendance:**\n"
                    "   * As per AKTU Ordinance and ABES regulations, every student must maintain a minimum of **75.0% attendance** in each registered theory and practical subject.\n\n"
                    "2. **Medical Leave Relaxation (Up to 10%):**\n"
                    "   * A relaxation of up to **10% (lowering threshold to 65%)** is granted strictly on medical grounds.\n"
                    "   * The medical certificate and doctor prescription from a registered medical practitioner (MBBS minimum) must be **submitted in person to the Proctor Office (Aryabhatta Block Room 004)**.\n"
                    "   * ⚠️ **Strict Deadline:** Must be submitted within **3 working days** of recovering and resuming classes.\n\n"
                    "3. **Consequences of Debarment:**\n"
                    "   * Attendance $< 75\\%$ without approved medical slip results in debarment from **Sessional Tests** (loss of internal 30 marks) and withholding of AKTU Semester Admit Card.\n\n"
                    "📍 **Chief Proctor:** Prof. (Dr.) Rati Ranjan Panda | Aryabhatta Block Room 004 | Email: `proctor@abes.ac.in`"
                ),
                "suggested_actions": ["Check ERP Attendance", "Sessional Test Guidelines", "Contact Proctor Office"]
            }

        # -------------------------------------------------------------
        # 13. SESSIONAL TESTS & AKTU EXAMINATIONS
        # -------------------------------------------------------------
        if any(w in q for w in ["sessional", "st-1", "st-2", "st 1", "st 2", "pue", "internal exam", "quantum", "exam scheme"]):
            return {
                "category": "Examinations",
                "answer": (
                    "### 📝 Sessional Exam Pattern & Internal Evaluation Scheme\n\n"
                    "* **Scheme of Sessional Tests:**\n"
                    "  * **ST-1:** Covers Units 1 and 2 (Duration: 90 Minutes, Max Marks: 30 / 50 scaled).\n"
                    "  * **ST-2:** Covers Units 3 and 4 (Duration: 90 Minutes, Max Marks: 30 / 50 scaled).\n"
                    "  * **Pre-University Exam (PUE):** Full 5 Units syllabus (Duration: 3 Hours, replica of AKTU end-sem format).\n"
                    "* **Internal Marks Calculation:**\n"
                    "  * The best **2 out of 3 sessionals** are considered for the internal theory component (30 Marks total).\n"
                    "* **AKTU Quantum Preparation Strategy:**\n"
                    "  * Past 5-year AKTU Quantum Series questions carry $>70\\%$ recurring conceptual weightage in Section B and Section C (10-mark questions).\n\n"
                    "🔗 Download question papers & date sheets on the [ABES Exam Cell Portal](https://erp.abes.ac.in)."
                ),
                "suggested_actions": ["Study Planner Tool", "Exam Prep Tool", "Generate Quiz for Sessional"]
            }

        # -------------------------------------------------------------
        # 14. CAMPUS WI-FI & INTERNET SETUP
        # -------------------------------------------------------------
        if any(w in q for w in ["wifi", "wi-fi", "internet", "cyberoam", "172.16", "login page", "captive portal"]):
            return {
                "category": "IT & Infrastructure",
                "answer": (
                    "### 📶 How to Connect to ABES Student Campus Wi-Fi\n\n"
                    "1. Connect your laptop or smartphone to the Wi-Fi network SSID: **`ABES-STUDENT`**.\n"
                    "2. Open Google Chrome, Firefox, or Safari and navigate to the local captive portal:\n"
                    "   * 🌐 **Captive Portal URL:** `http://172.16.0.1:8090/`\n"
                    "3. Enter your login credentials:\n"
                    "   * **Username:** Your College Student Roll Number (e.g., `2100320100xxx` or your assigned roll number)\n"
                    "   * **Password:** Your default ERP Wi-Fi Password (provided during registration)\n"
                    "4. Keep the authentication tab open in the background to sustain session connectivity.\n\n"
                    "🔧 **Support Desk:** IT Cell & Server Room, Ramanujan Block Room 102 (Ext. 120)."
                ),
                "suggested_actions": ["Open Wi-Fi Login Portal", "Contact IT Cell", "Campus Facilities"]
            }

        # -------------------------------------------------------------
        # 15. ACADEMIC & TECHNICAL QUERIES (DSA, ALGORITHMS, SYSTEM DESIGN)
        # -------------------------------------------------------------
        if any(w in q for w in ["dijkstra", "graph", "tree", "dynamic programming", "binary search", "sorting", "complexity"]):
            return {
                "category": "Computer Science & Engineering",
                "answer": (
                    "### ⚡ Dijkstra's Shortest Path Algorithm\n\n"
                    "Dijkstra's Algorithm finds the shortest path from a single source node to all other vertices in a weighted graph with **non-negative edge weights**.\n\n"
                    "#### 📐 Mathematical & Complexity Formulations:\n"
                    "* **Greedy Choice Property:** At each step, selects the unvisited vertex $u$ with minimum tentative distance.\n"
                    "* **Edge Relaxation Formula:**\n"
                    r"  $$\text{dist}[v] = \min(\text{dist}[v], \text{dist}[u] + \text{weight}(u, v))$$" + "\n"
                    "* **Time Complexity:**\n"
                    r"  * Using Min-Heap / Priority Queue: $\mathcal{O}((V + E) \log V)$" + "\n"
                    r"  * Using Adjacency Matrix: $\mathcal{O}(V^2)$" + "\n"
                    r"* **Space Complexity:** $\mathcal{O}(V)$ for distance table and priority queue." + "\n\n"
                    "#### 💻 Python Implementation Snippet:\n"
                    "```python\n"
                    "import heapq\n\n"
                    "def dijkstra(graph, start):\n"
                    "    distances = {node: float('inf') for node in graph}\n"
                    "    distances[start] = 0\n"
                    "    pq = [(0, start)]  # (distance, node)\n\n"
                    "    while pq:\n"
                    "        curr_dist, u = heapq.heappop(pq)\n"
                    "        if curr_dist > distances[u]:\n"
                    "            continue\n"
                    "        for v, weight in graph[u]:\n"
                    "            new_dist = curr_dist + weight\n"
                    "            if new_dist < distances[v]:\n"
                    "                distances[v] = new_dist\n"
                    "                heapq.heappush(pq, (new_dist, v))\n"
                    "    return distances\n"
                    "```\n\n"
                    "💡 **AKTU Exam Tip:** In sessional and end-sem exams, always illustrate the step-by-step trace table showing vertices, tentative distances, and predecessor nodes."
                ),
                "suggested_actions": ["Generate DSA Quiz", "Explain Simpler", "Give Another Example", "Assignment Assistant"]
            }

        # -------------------------------------------------------------
        # 16. GENERAL / FALLBACK ACADEMIC GUIDANCE
        # -------------------------------------------------------------
        return {
            "category": "Academic Guidance",
            "answer": (
                f"### 🎓 Studentsupport_bot (ABES EC Student Desk)\n\n"
                f"Thank you for your question: *\"{query}\"*\n\n"
                "Here is an engineering-focused synthesis to assist your study:\n\n"
                "1. **Core Academic Overview:** In the AKTU engineering curriculum, break systems into inputs, algorithmic transformations, and verifiable outputs.\n"
                "2. **Mathematical Precision:** Quantify computational efficiency using asymptotic notation (e.g., $\\mathcal{O}(n)$, $\\mathcal{O}(n \\log n)$).\n"
                "3. **Practical Application:** These fundamental principles recur in technical interviews conducted at ABES by recruiters like HCL, TCS, and Infosys.\n\n"
                "👉 *Use the interactive tools in the sidebar (Admission Guide, Study Planner, Faculty Directory, Central Library, Notes Summarizer, Fee Calculator) to explore further!*"
            ),
            "suggested_actions": [
                "Admission Process",
                "Director & Leadership",
                "Placement Statistics",
                "Central Library Details",
                "Faculty Directory"
            ]
        }
