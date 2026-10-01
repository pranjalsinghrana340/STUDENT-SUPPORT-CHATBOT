#!/usr/bin/env python3
"""
Studentsupport_botProject — Startup Runner
ABES Engineering College, Ghaziabad (AKTU Code: 032)
"""

import sys
import os
import uvicorn

def main():
    print("\n" + "="*75)
    print("🎓  Studentsupport_botProject — ABES Engineering College (Code 032)")
    print("="*75)
    print("📍  Campus: 19th KM Stone, NH-09, Ghaziabad, UP 201009")
    print("🌐  Local Web App: http://localhost:8000")
    print("📚  Swagger API Docs: http://localhost:8000/docs")
    print("📖  ReDoc Docs: http://localhost:8000/redoc")
    print("="*75)
    print("💡  Press Ctrl + C anytime to stop the server\n")

    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )

if __name__ == "__main__":
    main()
