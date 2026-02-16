# utils_output.py
import os
import csv
import logging
from datetime import datetime
from fpdf import FPDF

# -----------------------------
# Logging Setup
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

today = datetime.now().strftime("%Y-%m-%d")

info_logfile = os.path.join(LOG_DIR, f"payroll_{today}_info.log")
error_logfile = os.path.join(LOG_DIR, f"payroll_{today}_error.log")

logger = logging.getLogger("payroll")
logger.setLevel(logging.INFO)

info_handler = logging.FileHandler(info_logfile)
info_handler.setLevel(logging.INFO)

error_handler = logging.FileHandler(error_logfile)
error_handler.setLevel(logging.ERROR)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
info_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)

logger.addHandler(info_handler)
logger.addHandler(error_handler)


# -----------------------------
# PDF Generation
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAYSLIPS_DIR = os.path.join(BASE_DIR, "payslips")
os.makedirs(PAYSLIPS_DIR, exist_ok=True)

def generate_payslip_pdf(emp_id, name, result, timestamp=None):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.set_font("Arial", "B", 16)
    pdf.set_fill_color(230, 230, 230)
    pdf.cell(0, 12, "Employee Payslip", ln=True, align="C", fill=True)
    pdf.ln(5)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Employee Details", ln=True)
    pdf.set_font("Arial", size=11)

    pdf.cell(90, 8, f"Employee ID: {emp_id}", ln=False)
    pdf.cell(90, 8, f"Name: {name}", ln=True)
    pdf.ln(3)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Earnings", ln=True)
    pdf.set_font("Arial", size=11)

    pdf.cell(90, 8, f"Basic Salary: {result['base_salary']}", ln=False)
    pdf.cell(90, 8, f"Overtime: {result['overtime']}", ln=True)
    pdf.cell(90, 8, f"Allowances: {result['allowances']}", ln=True)
    pdf.ln(3)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Deductions", ln=True)
    pdf.set_font("Arial", size=11)

    pdf.cell(90, 8, f"Deductions: {result['deductions']}", ln=True)
    pdf.ln(3)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Summary", ln=True)
    pdf.set_font("Arial", size=11)

    pdf.cell(90, 8, f"Gross Salary: {result['gross']}", ln=False)
    pdf.cell(90, 8, f"Tax: {result['tax']}", ln=True)
    pdf.cell(90, 8, f"Super: {result['super']}", ln=False)
    pdf.cell(90, 8, f"Net Salary: {result['net']}", ln=True)
    pdf.ln(5)

    pdf.set_font("Arial", "I", 9)
    pdf.set_text_color(120, 120, 120)
    pdf.cell(0, 8, f"Pay run: {timestamp}", ln=True, align="C")
    pdf.cell(0, 8, "This is a system-generated payslip.", ln=True, align="C")

    filename = os.path.join(PAYSLIPS_DIR, f"payslip_{emp_id}.pdf")
    pdf.output(filename)
    logger.info(f"Generated payslip PDF: {filename}")


# -----------------------------
# CSV Summary Generation
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_summary_csv(summary_rows, timestamp=None):

    if timestamp is None:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


    filename = os.path.join(
        OUTPUT_DIR,
        f"payroll_summary_{timestamp.replace(':', '').replace(' ', '_')}.csv"
    )

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Emp ID", "Name",
            "Base Salary", "Hours", "Rate", "Multiplier",
            "Allowances", "Deductions",
            "Overtime", "Gross", "Tax", "Super", "Net"
        ])
        for row in summary_rows:
            writer.writerow([
                row["emp_id"],
                row["name"],
                row["base_salary"],
                row["hours"],
                row["rate"],
                row["multiplier"],
                row["allowances"],
                row["deductions"],
                row["overtime"],
                row["gross"],
                row["tax"],
                row["super"],
                row["net"]
            ])


    logger.info(f"Generated summary CSV: {filename}")