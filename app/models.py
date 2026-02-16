from sqlalchemy import Column, Integer, String, Float, DateTime,ForeignKey
from sqlalchemy.sql import func
from app.databasepostgre import Base

class Employee(Base):
    __tablename__ = "employees"

    emp_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    salary = Column(Float)
    hours  = Column(Float)
    rate   = Column(Float)
    multiplier = Column(Float)
    allowances = Column(Float)
    deductions = Column(Float)


class PayrollRun(Base):
    __tablename__ = "payroll_runs"

    run_id = Column(Integer, primary_key=True, index=True)
    run_date = Column(DateTime(timezone=True), server_default=func.now())
    total_employees = Column(Integer, default=0)
    total_gross = Column(Float, default=0.0)
    total_net = Column(Float, default=0.0)


class Payslip(Base):
    __tablename__ = "payslips"

    slip_id = Column(Integer, primary_key=True, index=True)
    run_id = Column(Integer, ForeignKey("payroll_runs.run_id"))
    emp_id = Column(String)

    base_salary = Column(Float)
    overtime = Column(Float)
    allowances = Column(Float)
    deductions = Column(Float)
    gross = Column(Float)
    tax = Column(Float)
    super = Column(Float)
    net = Column(Float)

