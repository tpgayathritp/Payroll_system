# seed.py
from app.databasepostgre import SessionLocal
from app.models import Employee

def seed_employees():
    db = SessionLocal()

    employees = [
        Employee(emp_id=101, name="John Doe", salary=5000, hours=10, rate=50, multiplier=1.5, allowances=200, deductions=100),
        Employee(emp_id=102, name="Jane Smith", salary=6000, hours=5, rate=60, multiplier=2.0, allowances=300, deductions=150),
        Employee(emp_id=103, name="Michael Lee", salary=44500, hours=8, rate=40, multiplier=1.25, allowances=150, deductions=80),
    ]

    for emp in employees:
        exists = db.query(Employee).filter(Employee.emp_id == emp.emp_id).first()
        if not exists:
            db.add(emp)

    db.commit()
    db.close()
    print("Employees seeded successfully.")

if __name__ == "__main__":
    seed_employees()