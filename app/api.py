from fastapi import FastAPI,HTTPException
from app import models
from app.databasepostgre import Base, engine
from pydantic import BaseModel
from app.output import generate_payslip_pdf,generate_summary_csv
from datetime import datetime
from fastapi.responses import FileResponse,HTMLResponse
import os
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from fastapi.templating import Jinja2Templates


# Create tables in PostgreSQL
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



# Import your new SQLAlchemy-based functions
from app.crud import (
    get_employee_by_id,
    get_all_employees,
    create_payroll_run,
    update_payroll_run,
    save_payslip
)

from app.Payroll import calculate_payroll_for_employee

class PayrollRequest(BaseModel):
    emp_id: int


@app.post("/run-payroll")
def run_payroll(request: PayrollRequest):
    emp_id = request.emp_id
    emp_row = get_employee_by_id(emp_id)

    if not emp_row:
        raise HTTPException(status_code=404, detail="Employee not found")


    emp_id, name, result = calculate_payroll_for_employee(emp_row)
    run_id = create_payroll_run()
    save_payslip(run_id, emp_id, result)

    generate_payslip_pdf(emp_id, name, result)

    total_employees = 1
    total_gross = result["gross"]
    total_net = result["net"]

    update_payroll_run(run_id, total_employees, total_gross, total_net)

    return {
        "status": "success",
        "run_id": run_id,
        "emp_id": emp_id,
        "name": name,
        "payslip": result
    }


@app.post("/run-payroll/all")
def run_payroll_all():
    employees = get_all_employees()

    if not employees:
        return {"error": "No employees found"}

    run_id = create_payroll_run()

    total_employees = 0
    total_gross = 0
    total_net = 0
    payslips = []
    summary_list = []

    for emp_row in employees:
        emp_id, name, result = calculate_payroll_for_employee(emp_row)
        save_payslip(run_id, emp_id, result)
        generate_payslip_pdf(emp_id, name, result)

        total_employees += 1
        total_gross += result["gross"]
        total_net += result["net"]

        payslips.append({
            "emp_id": emp_id,
            "name": name,
            "payslip": result
        })

        summary_list.append({
              "emp_id": emp_id,
              "name": name,
    	      "base_salary": result["base_salary"],
              "hours": result["hours"],
              "rate": result["rate"],
              "multiplier": result["multiplier"],
              "allowances": result["allowances"],
              "deductions": result["deductions"],
              "overtime": result["overtime"],
              "gross": result["gross"],
              "tax": result["tax"],
              "super": result["super"],
              "net": result["net"]
        })

      
    update_payroll_run(run_id, total_employees, total_gross, total_net)
    generate_summary_csv(summary_list)


    return {
        "status": "success",
        "run_id": run_id,
        "total_employees": total_employees,
        "total_gross": total_gross,
        "total_net": total_net,
        "payslips": payslips
    }


@app.get("/download-payslip/{emp_id}")
def download_payslip(emp_id: int):
    payslip_dir = "payslips"
    files = os.listdir(payslip_dir)

    # Find the latest payslip for this employee
    matching = [f for f in files if f.startswith(f"payslip_{emp_id}")]
    if not matching:
        raise HTTPException(status_code=404, detail="Payslip not found")

    # Pick the latest file
    latest = sorted(matching)[-1]
    filepath = os.path.join(payslip_dir, latest)

    return FileResponse(
        filepath,
        media_type="application/pdf",
        filename=latest
    )


@app.get("/download-summary")
def download_summary():
    output_dir = "output"
    files = os.listdir(output_dir)

    matching = [f for f in files if f.startswith("payroll_summary_")]
    if not matching:
        raise HTTPException(status_code=404, detail="Summary file not found")

    latest = sorted(matching)[-1]
    filepath = os.path.join(output_dir, latest)

    return FileResponse(
        filepath,
        media_type="text/csv",
        filename=latest
    )
