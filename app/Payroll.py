def calculate_tax(gross):
    if gross <= 18200:
        return 0
    elif gross <= 45000:
        return (gross - 18200) * 0.19
    elif gross <= 120000:
        return 5092 + (gross - 45000) * 0.325
    elif gross <= 180000:
        return 29467 + (gross - 120000) * 0.37
    else:
        return 51667 + (gross - 180000) * 0.45


def calculate_payroll_for_employee(emp_row):
    """
    emp_row is a SQLAlchemy Employee object:
    emp_row.emp_id
    emp_row.name
    emp_row.salary
    emp_row.hours
    emp_row.rate
    emp_row.multiplier
    emp_row.allowances
    emp_row.deductions
    """

    overtime = emp_row.hours * emp_row.rate * emp_row.multiplier
    gross = emp_row.salary + overtime + emp_row.allowances
    tax = calculate_tax(gross)
    super_amt = gross * 0.095
    net = gross - tax - emp_row.deductions

    result = {
        "base_salary": emp_row.salary,
        "hours": emp_row.hours,
        "rate": emp_row.rate,
        "multiplier": emp_row.multiplier,
        "allowances": emp_row.allowances,
        "deductions": emp_row.deductions,
        "overtime": overtime,
        "gross": gross,
        "tax": tax,
        "super": super_amt,
        "net": net,
    }

    return emp_row.emp_id, emp_row.name, result