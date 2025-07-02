from tabulate import tabulate

from colorama import Fore, Style, init
init(autoreset=True)

from dao.employee_service import EmployeeService
from dao.payroll_service import PayrollService
from dao.tax_service import TaxService
from dao.financial_record_service import FinancialRecordService
from dao.report_generator import ReportGenerator
from dao.validation_service import ValidationService
from exception.exceptions import EmployeeNotFoundException
from util.DBConnUtil import get_connection
from datetime import datetime

emp_service = EmployeeService()
payroll_service = PayrollService()
tax_service = TaxService()
fin_service = FinancialRecordService()
report_gen = ReportGenerator()

def employee_menu():
    while True:
        print(Style.BRIGHT + Fore.MAGENTA +"\n--- Employee Management ---")
        print("1. View Employee by ID")
        print("2. View All Employees")
        print("3. Add Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Return to Main Menu")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            try:
                emp_id = int(input("Employee ID: "))
                print(emp_service.get_employee_by_id(emp_id))
            except EmployeeNotFoundException as e:
                print(e)

        elif choice == 2:
            print(Style.BRIGHT + Fore.BLUE + "------ Employee Details ------")
            employees = emp_service.get_all_employees()
            table_data = []
            headers = ["EmpID", "First Name", "Last Name", "DOB", "Gender", "Email", "Phone", "Address", "Position","Joining Date", "Termination Date"]
            for emp in employees:
                table_data.append([
                    emp[0], emp[1], emp[2], emp[3], emp[4], emp[5],
                    emp[6], emp[7], emp[8], emp[9], emp[10]
                ])
            print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

        elif choice == 3:
            emp_service.add_employee()

        elif choice == 4:
            emp_service.update_employee_by_choice()

        elif choice == 5:
            emp_id = int(input("Enter Employee ID to delete: "))
            emp_service.remove_employee(emp_id)

        elif choice == 6:
            break

        else:
            print(Fore.RED + "Invalid choice. Please enter a valid option.")

def payroll_menu():
    while True:
        print(Style.BRIGHT + Fore.MAGENTA + "\n--- Payroll Management ---")
        print("1. Generate Payroll")
        print("2. View Payroll by PayrollID")
        print("3. View Payrolls by EmployeeID")
        print("4. View Payrolls for Period")
        print("5. Return to Main Menu")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            eid = int(input("Enter Employee ID: "))
            start = input("Start Date(YYYY-MM-DD): ")
            end = input("End Date(YYYY-MM-DD): ")
            bs = float(input("Basic Salary: "))
            ot = float(input("Overtime Pay: "))
            ded = float(input("Deductions: "))
            payroll_service.generate_payroll(eid, start, end, bs, ot, ded)

        elif choice == 2:
            pid = int(input("Enter PayrollID: "))
            payroll = payroll_service.get_payroll_by_id(pid)
            if payroll:
                print(Style.BRIGHT + Fore.BLUE +"\n--- Payroll Details ---")
                for k, v in payroll.items():
                    print(f"{k} : {float(v) if isinstance(v, float) or 'Decimal' in str(type(v)) else v}")

        elif choice == 3:
            emp_id = int(input("Enter EmployeeID: "))
            payrolls = payroll_service.get_payrolls_for_employee(emp_id)
            for rec in payrolls:
                print(Fore.MAGENTA +"\n--- Payroll ---")
                print(f"Payroll ID     : {rec[0]}")
                print(f"Employee ID    : {rec[1]}")
                print(f"Start Date     : {rec[2]}")
                print(f"End Date       : {rec[3]}")
                print(f"Basic Salary   : {float(rec[4])}")
                print(f"Overtime Pay   : {float(rec[5])}")
                print(f"Deductions     : {float(rec[6])}")
                print(f"Net Salary     : {float(rec[7])}")

        elif choice == 4:
            start = input("Start Date(YYYY-MM-DD): ")
            end = input("End Date(YYYY-MM-DD): ")
            payrolls = payroll_service.get_payrolls_for_period(start, end)
            for rec in payrolls:
                print(rec)

        elif choice == 5:
            break

        else:
            print(Fore.RED + "Invalid choice. Please enter a valid option.")

def tax_menu():
    while True:
        print(Style.BRIGHT + Fore.MAGENTA +"\n--- Tax Management ---")
        print("1. Calculate Tax")
        print("2. View Tax by ID")
        print("3. View Taxes by EmployeeID")
        print("4. View Taxes by Year")
        print("5. Return to Main Menu")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            eid = int(input("Enter EmployeeID: "))
            year = int(input("Enter Tax Year: "))
            tax_service.calculate_tax(eid, year)

        elif choice == 2:
            tid = int(input("Enter TaxID: "))
            tax = tax_service.get_tax_by_id(tid)
            if tax:
                print(Style.BRIGHT + Fore.BLUE + f"\n--- Tax Details ---")
                print(f"Tax ID         : {tax[0]}")
                print(f"Employee ID    : {tax[1]}")
                print(f"Tax Year       : {tax[2]}")
                print(f"Taxable Income : {float(tax[3])}")
                print(f"Tax Amount     : {float(tax[4])}")
            else:
                print(Fore.RED + "No tax record found.")

        elif choice == 3:
            eid = int(input("Enter EmployeeID: "))
            db = get_connection()
            c = db.cursor()
            c.execute("SELECT * FROM Tax WHERE EmployeeID = %s", (eid,))
            taxes = c.fetchall()
            for t in taxes:
                print(Style.BRIGHT + Fore.MAGENTA +f"\n--- Tax Record ---")
                print(f"Tax ID         : {t[0]}")
                print(f"Employee ID    : {t[1]}")
                print(f"Tax Year       : {t[2]}")
                print(f"Taxable Income : {float(t[3])}")
                print(f"Tax Amount     : {float(t[4])}")

        elif choice == 4:
            year = int(input("Enter Tax Year: "))
            db = get_connection()
            c = db.cursor()
            c.execute("SELECT * FROM Tax WHERE TaxYear = %s", (year,))
            taxes = c.fetchall()
            for t in taxes:
                print(Fore.MAGENTA +f"\n--- Tax Record ---")
                print(f"Tax ID         : {t[0]}")
                print(f"Employee ID    : {t[1]}")
                print(f"Tax Year       : {t[2]}")
                print(f"Taxable Income : {float(t[3])}")
                print(f"Tax Amount     : {float(t[4])}")

        elif choice == 5:
            break
        else:
            print(Fore.RED + "Invalid choice. Please enter a valid option.")

def financial_menu():
    while True:
        print(Style.BRIGHT + Fore.MAGENTA +"\n--- Financial Record Management ---")
        print("1. Add Financial Record")
        print("2. View Record by RecordID")
        print("3. View Records for Employee")
        print("4. View Records by Date")
        print("5. Return to Main Menu")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            eid = int(input("Enter EmployeeID: "))
            desc = input("Enter Description: ")
            amt = float(input("Enter Amount: "))
            rtype = input("Enter Record Type: ")
            fin_service.add_financial_record(eid, desc, amt, rtype)

        elif choice == 2:
            rid = int(input("Enter RecordID: "))
            db = get_connection()
            c = db.cursor()
            c.execute("SELECT * FROM FinancialRecord WHERE RecordID = %s", (rid,))
            r = c.fetchone()
            if r:
                print(Fore.MAGENTA +f"\n--- Record ---\nRecord ID: {r[0]}\nEmployee ID: {r[1]}\nDate: {r[2]}\nDesc: {r[3]}\nAmount: {float(r[4])}")
            else:
                print(Fore.RED + "No record found.")

        elif choice == 3:
            eid = int(input("Enter EmployeeID: "))
            db = get_connection()
            c = db.cursor()
            c.execute("SELECT * FROM FinancialRecord WHERE EmployeeID = %s", (eid,))
            recs = c.fetchall()
            for r in recs:
                print(Fore.MAGENTA +f"\n--- Record ---\nRecord ID: {r[0]}\nDate: {r[2]}\nDesc: {r[3]}\nAmount: {float(r[4])}")

        elif choice == 4:
            date = input("Enter Date (YYYY-MM-DD): ")
            db = get_connection()
            c = db.cursor()
            c.execute("SELECT * FROM FinancialRecord WHERE RecordDate = %s", (date,))
            recs = c.fetchall()
            for r in recs:
                print(Fore.MAGENTA +f"\n--- Record ---\nRecord ID: {r[0]}\nEmployee ID: {r[1]}\nDesc: {r[3]}\nAmount: {float(r[4])}")

        elif choice == 5:
            break
        else:
            print(Fore.RED + "Invalid choice. Please enter a valid option.")

# --- Main Menu ---
db = get_connection()
c = db.cursor()
c.execute("SELECT COUNT(*) FROM Employee")
total_emp = c.fetchone()[0]
c.execute("SELECT COUNT(*) FROM Payroll")
total_payrolls = c.fetchone()[0]
c.execute("SELECT COUNT(*) FROM Tax")
total_taxes = c.fetchone()[0]
print(Style.BRIGHT + Fore.CYAN +"------------------------------------------------------")
print(Fore.YELLOW +f"|| Total Employees: {total_emp} || Payrolls: {total_payrolls} || Taxes: {total_taxes} ||")
print(Style.BRIGHT + Fore.CYAN +"------------------------------------------------------")

while True:
    print(Style.BRIGHT + Fore.CYAN + "\n----- PayXpert Payroll Management System -----")
    print("1. Employee Management")
    print("2. Payroll Management")
    print("3. Tax Management")
    print("4. Financial Record Management")
    print("5. Reports")
    print("6. Exit")
    main_choice = int(input("Enter your choice: "))

    if main_choice == 1:
        employee_menu()
    elif main_choice == 2:
        payroll_menu()
    elif main_choice == 3:
        tax_menu()
    elif main_choice == 4:
        financial_menu()
    elif main_choice == 5:
        print(Style.BRIGHT + Fore.MAGENTA +"\n--- Reports ---")
        print("1. Salary Report")
        print("2. Tax Report")
        print("3. Financial Record Report")
        rep = int(input("Enter your choice: "))
        if rep == 1:
            report_gen.generate_salary_report()
        elif rep == 2:
            report_gen.generate_tax_report()
        elif rep == 3:
            report_gen.generate_financial_report()
    elif main_choice == 6:
        print(Style.BRIGHT + Fore.CYAN +"Thank you for using PayXpert!")
        break
    else:
        print(Fore.RED + "Invalid choice. Please enter a valid option.")






# from dao.employee_service import EmployeeService
# from dao.payroll_service import PayrollService
# from dao.tax_service import TaxService
# from dao.financial_record_service import FinancialRecordService
# from entity.employee import Employee
# from dao.report_generator import ReportGenerator
# from exception.exceptions import EmployeeNotFoundException
# from dao.validation_service import ValidationService
# from util.DBConnUtil import get_connection
#
# from datetime import datetime
#
# emp_service=EmployeeService()
# payroll_service=PayrollService()
# fin_service=FinancialRecordService()
# tax_service=TaxService()
# report_gen=ReportGenerator()
#
# while True:
#     print("\n----- PayXpert Payroll Management System -----")
#     print()
#     print("----- Employee -----")
#     print("1. To View Employee by EmployeeID")
#     print("2. To View All Employees")
#     print("3. To Add Employee")
#     print("4. To Update Employee")
#     print("5. To Delete Employee")
#     print()
#     print("----- Payroll -----")
#     print("6. To Generate Payroll")
#     print("7. To View Payroll by PayrollID")
#     print("8. To View Payrolls for Employee by EmployeeID")
#     print("9. To View Payrolls for Period")
#     print()
#     print("----- Tax -----")
#     print("10. To Calculate Tax")
#     print("11. To View Tax by ID")
#     print("12. To View Taxes for Employee")
#     print("13. To View Taxes for Year")
#     print()
#     print("----- Financial Record ------")
#     print("14. To Add Financial Record")
#     print("15. To View Financial Record by RecordID")
#     print("16. To View Financial Records for Employee by EmployeeID")
#     print("17. To View Financial Records by Date")
#     print()
#     print("----- Reports ------")
#     print("18. To Generate Salary Report")
#     print("19. To Generate Tax Report")
#     print("20. To Generate Financial Record Report")
#     print()
#     print("21. Exit")
#     print()
#
#     choice=int(input("Enter Your Choice: "))
#
#     if choice==1:
#         try:
#             emp_id=int(input("Employee ID: "))
#             print(emp_service.get_employee_by_id(emp_id))
#         except EmployeeNotFoundException as e:
#             print(e)
#
#     elif choice==2:
#         print("------ Employee Details ------")
#         employees=emp_service.get_all_employees()
#         for i in employees:
#             print(i)
#
#     elif choice==3:
#         emp_service.add_employee()
#
#
#     elif choice == 4:
#         eid = int(input("Employee ID to update: "))
#         try:
#             emp = emp_service.get_employee_by_id(eid)
#             print("\nWhich field do you want to update?")
#             print("1. First Name")
#             print("2. Last Name")
#             print("3. Date of Birth")
#             print("4. Gender")
#             print("5. Email")
#             print("6. Phone Number")
#             print("7. Address")
#             print("8. Position")
#             print("9. Joining Date")
#             print("10. Termination Date")
#             field = int(input("Enter your choice: "))
#
#             if field == 1:
#                 emp.set_first_name(input("New First Name: "))
#             elif field == 2:
#                 emp.set_last_name(input("New Last Name: "))
#             elif field == 3:
#                 emp.set_dob(input("New DOB (YYYY-MM-DD): "))
#             elif field == 4:
#                 emp.set_gender(input("New Gender: "))
#             elif field == 5:
#                 new_email = input("New Email: ")
#                 ValidationService.validate_email(new_email)
#                 emp.set_email(new_email)
#             elif field == 6:
#                 new_phone = input("New Phone Number: ")
#                 ValidationService.validate_phone(new_phone)
#                 emp.set_phone_number(new_phone)
#             elif field == 7:
#                 emp.set_address(input("New Address: "))
#             elif field == 8:
#                 emp.set_position(input("New Position: "))
#             elif field == 9:
#                 emp.set_joining_date(input("New Joining Date (YYYY-MM-DD): "))
#             elif field == 10:
#                 emp.set_termination_date(input("New Termination Date (YYYY-MM-DD) or leave blank: ") or None)
#             else:
#                 print("Invalid choice.")
#             # Save to DB
#             emp_service.update_employee(emp)
#         except Exception as e:
#             print(f"Error: {e}")
#
#     elif choice==5:
#         eid=int(input("Enter Employee ID to delete: "))
#         emp_service.remove_employee(eid)
#
#     elif choice==6:
#         eid = int(input("Enter Employee ID: "))
#         start = input("Start Date(YYYY-MM-DD): ")
#         end = input("End Date(YYYY-MM-DD): ")
#         bs = float(input("Basic Salary: "))
#         ot = float(input("Overtime Pay: "))
#         ded = float(input("Deductions: "))
#
#         payroll_service.generate_payroll(eid, start, end, bs, ot, ded)
#
#
#     elif choice == 7:
#         payroll_id = int(input("Enter PayrollID: "))
#         try:
#             payroll = payroll_service.get_payroll_by_id(payroll_id)
#             print("------ Payroll Details ------")
#             print(f"Payroll ID     : {payroll['PayrollID']}")
#             print(f"Employee ID    : {payroll['EmployeeID']}")
#             print(f"Start Date     : {payroll['StartDate']}")
#             print(f"End Date       : {payroll['EndDate']}")
#             print(f"Basic Salary   : {float(payroll['BasicSalary'])}")
#             print(f"Overtime Pay   : {float(payroll['OvertimePay'])}")
#             print(f"Deductions     : {float(payroll['Deductions'])}")
#             print(f"Net Salary     : {float(payroll['NetSalary'])}")
#         except Exception as e:
#             print(f"Error: {e}")
#
#     elif choice == 8:
#         emp_id = int(input("Enter EmployeeID: "))
#         try:
#             payrolls = payroll_service.get_payrolls_for_employee(emp_id)
#             if payrolls:
#                 print(f"--- Payroll Records for Employee ID: {emp_id} ---")
#                 for rec in payrolls:
#                     print("--- Payroll ---")
#                     print(f"Payroll ID     : {rec[0]}")
#                     print(f"Employee ID    : {rec[1]}")
#                     print(f"Start Date     : {rec[2]}")
#                     print(f"End Date       : {rec[3]}")
#                     print(f"Basic Salary   : {float(rec[4])}")
#                     print(f"Overtime Pay   : {float(rec[5])}")
#                     print(f"Deductions     : {float(rec[6])}")
#                     print(f"Net Salary     : {float(rec[7])}")
#             else:
#                 print("No payroll records found for this employee.")
#         except Exception as e:
#             print(f"Error: {e}")
#
#     elif choice==9:
#         start=input("Start Date(YYYY-MM-DD): ")
#         end=input("End Date(YYYY-MM-DD): ")
#         results=payroll_service.get_payrolls_for_period(start,end)
#         for res in results:
#             print(res)
#
#     elif choice==10:
#         eid=int(input("Enter EmployeeID: "))
#         year=int(input("Enter Tax Year: "))
#         tax_service.calculate_tax(eid, year)
#
#
#     elif choice == 11:
#         tax_id = int(input("Enter TaxID: "))
#         tax = tax_service.get_tax_by_id(tax_id)  # returns tuple like (319, 111, 2025, Decimal(...), Decimal(...))
#         if tax:
#             print("\n--- Tax Details ---")
#             print(f"Tax ID        : {tax[0]}")
#             print(f"Employee ID   : {tax[1]}")
#             print(f"Tax Year      : {tax[2]}")
#             print(f"Taxable Income: {float(tax[3])}")
#             print(f"Tax Amount    : {float(tax[4])}")
#         else:
#             print("No record found for given Tax ID.")
#
#     elif choice == 12:
#         emp_id = int(input("Enter EmployeeID: "))
#         db = get_connection()
#         c= db.cursor()
#         c.execute("SELECT * FROM Tax WHERE EmployeeID = %s", (emp_id,))
#         records = c.fetchall()
#         if records:
#             for rec in records:
#                 print("\n--- Tax Record ---")
#                 print(f"Tax ID         : {rec[0]}")
#                 print(f"Employee ID    : {rec[1]}")
#                 print(f"Tax Year       : {rec[2]}")
#                 print(f"Taxable Income : {float(rec[3])}")
#                 print(f"Tax Amount     : {float(rec[4])}")
#         else:
#             print("No tax records found for this employee.")
#
#     elif choice == 13:
#         year = int(input("Enter Tax Year: "))
#         db = get_connection()
#         c= db.cursor()
#         c.execute("SELECT * FROM Tax WHERE TaxYear = %s", (year,))
#         tax_records = c.fetchall()
#         if tax_records:
#             print(f"\n--- Tax Report for Year {year} ---")
#             for record in tax_records:
#                 print("\n--- Tax Record ---")
#                 print(f"Tax ID         : {record[0]}")
#                 print(f"Employee ID    : {record[1]}")
#                 print(f"Tax Year       : {record[2]}")
#                 print(f"Taxable Income : {float(record[3])}")
#                 print(f"Tax Amount     : {float(record[4])}")
#         else:
#             print(f"No tax records found for the year {year}.")
#
#     elif choice==14:
#         eid=int(input("Enter EmployeeID: "))
#         desc=input("Enter Description: ")
#         amt=float(input("Enter Amount: "))
#         rtype=input("Enter Record Type: ")
#         fin_service.add_financial_record(eid, desc, amt, rtype)
#
#
#     elif choice == 15:
#         record_id = int(input("Enter RecordID: "))
#         db = get_connection()
#         c= db.cursor()
#         c.execute("SELECT * FROM FinancialRecord WHERE RecordID = %s", (record_id,))
#         record = c.fetchone()
#         if record:
#             print("\n--- Financial Record ---")
#             print(f"Record ID     : {record[0]}")
#             print(f"Employee ID   : {record[1]}")
#             print(f"Record Date   : {record[2]}")
#             print(f"Description   : {record[3]}")
#             print(f"Amount        : {float(record[4])}")
#         else:
#             print(f"No record found for RecordID {record_id}")
#
#     elif choice == 16:
#         emp_id = int(input("Enter EmployeeID: "))
#         db = get_connection()
#         c= db.cursor()
#         c.execute("SELECT * FROM FinancialRecord WHERE EmployeeID = %s", (emp_id,))
#         records = c.fetchall()
#
#         if records:
#             print(f"\n--- Financial Records for Employee ID {emp_id} ---")
#             for record in records:
#                 print("\n--- Financial Record ---")
#                 print(f"Record ID     : {record[0]}")
#                 print(f"Record Date   : {record[2]}")
#                 print(f"Description   : {record[3]}")
#                 print(f"Amount        : {float(record[4])}")
#         else:
#             print(f"No financial records found for EmployeeID {emp_id}")
#
#     elif choice == 17:
#         record_date = input("Enter Record Date (YYYY-MM-DD): ")
#         db = get_connection()
#         c= db.cursor()
#         c.execute("SELECT * FROM FinancialRecord WHERE RecordDate = %s", (record_date,))
#         records = c.fetchall()
#         if records:
#             print(f"\n--- Financial Records on {record_date} ---")
#             for record in records:
#                 print("\n--- Financial Record ---")
#                 print(f"Record ID     : {record[0]}")
#                 print(f"Employee ID   : {record[1]}")
#                 print(f"Description   : {record[3]}")
#                 print(f"Amount        : {float(record[4])}")
#         else:
#             print(f"No financial records found on {record_date}")
#
#     elif choice ==18:
#         report_gen.generate_salary_report()
#
#     elif choice ==19:
#         report_gen.generate_tax_report()
#
#     elif choice==20:
#         report_gen.generate_financial_report()
#
#     elif choice==21:
#         print("THANK YOU!")
#         break
#
#     else:
#         print("Invalid choice.Please Enter a Valid Choice.")