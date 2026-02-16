from sqlalchemy.orm import Session
from app.databasepostgre import SessionLocal
from app.models import Employee, PayrollRun, Payslip


# -----------------------------
# Helper: Get DB session
# -----------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -----------------------------
# EMPLOYEE QUERIES
# -----------------------------
def get_employee_by_id(emp_id: int):
    db = SessionLocal()
    employee = db.query(Employee).filter(Employee.emp_id == emp_id).first()
    db.close()
    return employee


def get_all_employees():
    db = SessionLocal()
    employees = db.query(Employee).all()
    db.close()
    return employees


# -----------------------------
# PAYROLL RUNS
# -----------------------------
def create_payroll_run():
    db = SessionLocal()
    payroll_run = PayrollRun()
    db.add(payroll_run)
    db.commit()
    db.refresh(payroll_run)
    db.close()
    return payroll_run.run_id


def update_payroll_run(run_id, total_employees, total_gross, total_net):
    db = SessionLocal()
    payroll_run = db.query(PayrollRun).filter(PayrollRun.run_id == run_id).first()

    if payroll_run:
        payroll_run.total_employees = total_employees
        payroll_run.total_gross = total_gross
        payroll_run.total_net = total_net
        db.commit()

    db.close()


# -----------------------------
# PAYSLIPS
# -----------------------------
def save_payslip(run_id, emp_id, result):
    db = SessionLocal()

    payslip = Payslip(
        run_id=run_id,
        emp_id=emp_id,
        base_salary=result["base_salary"],
        overtime=result["overtime"],
        allowances=result["allowances"],
        deductions=result["deductions"],
        gross=result["gross"],
        tax=result["tax"],
        super=result["super"],
        net=result["net"]
    )

    db.add(payslip)
    db.commit()
    db.close()