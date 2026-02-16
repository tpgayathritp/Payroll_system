Payroll Processing System
--------------------------------------
FastAPI • Docker • PostgreSQL • Jenkins CI/CD

A complete, production‑style Payroll Processing System built using FastAPI, containerized with Docker, backed by PostgreSQL, and automated using a fully functional Jenkins CI/CD pipeline.
This project demonstrates backend engineering, DevOps automation, and application design.

Project Overview
-------------------------------------
This system calculates payroll for employees, generates payslips (PDF), produces payroll summaries (CSV), and stores payroll history in a PostgreSQL database.
The entire application runs inside Docker containers and is deployed automatically using Jenkins CI/CD.

Key Features
------------------------------------

1. FastAPI 

   - REST API endpoints for payroll processing
   - Auto‑generated Swagger UI
   - Clean, modular Python code
   - PDF and CSV file generation

2. Payroll Engine
   Calculates:
   - Basic salary
   - Net salary
   - Tax
   - Super
   - Overtime

   Supports:
   - Single employee payroll
   - Full payroll run for all employees

3. Database (PostgreSQL)
   - Employee master table
   - Payroll run history
   - Payslips details
   - Managed via pgAdmin

4. Dockerized Architecture
   - FastAPI container
   - PostgreSQL container
   - pgAdmin container
   - Persistent volumes

5. Jenkins CI/CD Pipeline
   - Automated build
   - Automated deployment
   - Docker container orchestration
   - Success/failure reporting


Project Structure
------------------------------------

Payroll_app_Docker/
 ── app/
     ── api.py
     ── payroll_logic.py
     ── database.py
     ── models.py
     ── utils/
     ── output/ 


── Dockerfile
── docker-compose.yml
── requirements.txt
── Jenkinsfile
── README







