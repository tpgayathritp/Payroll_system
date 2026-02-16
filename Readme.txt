Payroll Processing System — FastAPI + PostgreSQL
A complete, production‑style payroll processing system built with FastAPI, PostgreSQL, and Python, featuring payroll calculations, PDF payslip generation, CSV summary exports, and a simple web frontend for running and downloading payroll outputs.

Features
  Payroll Engine
      - Calculates:
      - Base salary
      - Hours × rate × multiplier
      - Allowances
      - Deductions
      - Overtime
      - Gross pay
      - Tax
      - Superannuation
      - Net pay
   Database Integration (PostgreSQL)
      - Employee data stored in PostgreSQL
      - SQLAlchemy ORM
      - Clean CRUD structure
   PDF Payslip Generation
      - Automatically generates a PDF payslip for each employee
      - Timestamped filenames
      - Stored in /payslips/
   CSV Summary Export
      - Generates a full payroll summary CSV
      - Includes all payroll components
      - Stored in /output/
   Download Endpoints
      - /download-payslip/{emp_id} → Download latest payslip
      - /download-summary → Download latest summary CSV
   Simple Frontend UI
      - Run payroll for all employees
      - Download summary
      - Download payslip by employee ID
      - Served via FastAPI templates

Technical



Project Structure

Payroll_app_postgreSQL/
│
├── api.py                 # FastAPI routes
├── crud.py                # Database operations
├── models.py              # SQLAlchemy models
├── output.py              # PDF + CSV generation
├── utils_output.py        # Helper functions
│
├── payslips/              # Generated PDF payslips
├── output/                # Generated CSV summaries
├── logs/                  # Payroll logs
│
├── templates/
│     └── index.html       # Frontend UI
│
└── static/                # CSS/JS assets


How to run this project

  Install dependencies
    pip install -r requirements.txt

  Start PostgreSQL and create database
    CREATE DATABASE payroll_db;

  Run FastAPI server
    uvicorn api:app --reload

  Open the frontend
    http://127.0.0.1:8000/

API Endpoints
   Run Payroll
   POST /run-payroll/all
  
   Download Payslip
   GET /download-payslip/{emp_id}


   Download Summary CSV
   GET /download-summary

   Frontend UI
   GET /

Example Output Files
    PDF Payslip
    payslip_101.pdf


    CSV Summary
    payroll_summary_2026-02-13_11-25-10.csv

    Log Files
    payroll_2026-02-13_error.log
    payroll_2026-02-13_info.log


Future Enhancements
- Add authentication 
- Add employee management UI
- Add Excel (.xlsx) export
- Deploy to Azure App Service
- Add CI/CD pipeline (GitHub Actions / Azure DevOps)
