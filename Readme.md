Payroll Processing System
--------------------------------------
FastAPI ,Docker ,PostgreSQL, Jenkins CI/CD

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
   - Python code
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
   
5. Jenkins CI/CD Pipeline
   - Automated build
   - Automated deployment
   - Docker container orchestration
   - Success/failure reporting

The CI/CD pipeline intentionally does not run payroll.  
Payroll execution is a business operation and is triggered manually via API, not during deployment.

Project Structure
------------------------------------

Payroll_app_Docker/
 ── app/
     ── api.py                   # FastAPI routes and endpoints
     ── payroll.py               # Payroll engine
     ── databasepostgre.py       # PostgreSQL connection and session management
     ── models.py                # SQLAlchemy
     ── crud.py                  # Database operations
     ── output.py                # PDF/CSV generation/logs


── Dockerfile                    # FastAPI Docker image
── docker-compose.yml            # Orchestrates API, PostgreSQL, pgAdmin
── requirements.txt              # Python dependencies
── Jenkinsfile                   # CI/CD pipeline definition
── README                        # Project documentation


Running the Application (Docker)
-------------------------------------

Build and start containers
   docker compose up -d --build

Access the FastAPI documentation
  http://127.0.0.1:8000/docs

Access pgAdmin
  http://127.0.0.1:5050


API End Points
------------------------------------

Run Payroll for all employees
Run Payroll for a single employee
Download Payslip
Download payroll summary(csv)


Jenkins CI/CD Pipelines
-----------------------------------

Build Stage
- Pulls latest code from GitHub
- Installs dependencies
- Prepares environment

Deployment Stage
- Runs Docker containers
- Deploys FastAPI backend
- Verifies service health

Post Deployment
- Prints success message

Pipeline Output
  Finished: SUCCESS
  Deployment successful!

NOTE :
The CI/CD pipeline does not run payroll automatically — this is intentional.
Payroll is a business operation, not a deployment step.

Project flow
-----------------------------

- Developer pushes code to GitHub
- Jenkins pulls latest code
- Jenkins builds and deploys Docker containers
- FastAPI app becomes available at localhost:8000
- User triggers payroll manually via API
- System generates:
- PDF payslips
- CSV summary
- Database entries
- Log/error files

NOTE :Employee records are added manually through pgAdmin. 
The system does not use a seed_employees script.


Future Enhancements
------------------------------

- API key authentication
- Scheduled payroll runs
- Email notification
- Password protected payslips




