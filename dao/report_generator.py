from util.DBConnUtil import get_connection
from datetime import datetime

from colorama import Fore, Style, init
init(autoreset=True)

class ReportGenerator:

    def generate_salary_report(self):
        try:
            start_date = input("Enter Start Date (YYYY-MM-DD): ").strip()
            end_date = input("Enter End Date (YYYY-MM-DD): ").strip()

            # Check if inputs are not empty
            if not start_date or not end_date:
                print(Style.BRIGHT + Fore.RED +"Start Date and End Date are required!")
                return

            # Validate date format
            try:
                datetime.strptime(start_date, "%Y-%m-%d")
                datetime.strptime(end_date, "%Y-%m-%d")
            except ValueError:
                print(Style.BRIGHT + Fore.RED +"Invalid date format. Please use YYYY-MM-DD.")
                return

            db = get_connection()
            cursor = db.cursor()
            cursor.execute("""
                        SELECT EmployeeID, NetSalary, PayPeriodStartDate, PayPeriodEndDate
                        FROM Payroll
                        WHERE PayPeriodStartDate >= %s AND PayPeriodEndDate <= %s
                    """, (start_date, end_date))

            records = cursor.fetchall()
            if records:
                print(Style.BRIGHT + Fore.BLUE +f"\n--- Salary Report from {start_date} to {end_date} ---")
                for row in records:
                    print(f"Employee ID  : {row[0]}")
                    print(f"Net Salary   : {float(row[1])}")
                    print(f"Start Date   : {row[2]}")
                    print(f"End Date     : {row[3]}")
                    print(Style.BRIGHT + Fore.BLUE +"---------------------------")
            else:
                print(Style.BRIGHT + Fore.LIGHTRED_EX +"No records found for this period.")
        except Exception as e:
            print(Style.BRIGHT + Fore.RED +f"Error generating salary report: {e}")

    def generate_tax_report(self):
        try:
            start_date = input("Enter Start Date (YYYY-MM-DD): ").strip()
            end_date = input("Enter End Date (YYYY-MM-DD): ").strip()

            if not start_date or not end_date:
                print(Style.BRIGHT + Fore.RED +"Start Date and End Date are required!")
                return

            try:
                datetime.strptime(start_date, "%Y-%m-%d")
                datetime.strptime(end_date, "%Y-%m-%d")
            except ValueError:
                print(Style.BRIGHT + Fore.RED +"Invalid date format. Use YYYY-MM-DD.")
                return

            db = get_connection()
            c = db.cursor()
            c.execute("""
                        SELECT TaxID, EmployeeID, TaxYear, TaxableIncome, TaxAmount
                        FROM Tax
                        WHERE TaxYear BETWEEN YEAR(%s) AND YEAR(%s)
                    """, (start_date, end_date))

            rows = c.fetchall()
            if rows:
                print(Style.BRIGHT + Fore.BLUE +f"\n--- Tax Report from {start_date} to {end_date} ---")
                for row in rows:
                    print(f"Tax ID         : {row[0]}")
                    print(f"Employee ID    : {row[1]}")
                    print(f"Tax Year       : {row[2]}")
                    print(f"Taxable Income : {float(row[3])}")
                    print(f"Tax Amount     : {float(row[4])}")
                    print(Style.BRIGHT + Fore.BLUE +"-----------------------------")
            else:
                print(Style.BRIGHT + Fore.LIGHTRED_EX +"No tax records found in this period.")
        except Exception as e:
            print(Style.BRIGHT + Fore.RED +f"Error generating tax report: {e}")

    def generate_financial_report(self):
        try:
            start_date = input("Enter Start Date (YYYY-MM-DD): ").strip()
            end_date = input("Enter End Date (YYYY-MM-DD): ").strip()

            if not start_date or not end_date:
                print(Style.BRIGHT + Fore.RED +"Start Date and End Date are required!")
                return

            try:
                datetime.strptime(start_date, "%Y-%m-%d")
                datetime.strptime(end_date, "%Y-%m-%d")
            except ValueError:
                print(Style.BRIGHT + Fore.RED +"Invalid date format. Use YYYY-MM-DD.")
                return

            db = get_connection()
            c = db.cursor()
            c.execute("""
                        SELECT RecordID, EmployeeID, RecordDate, Description, Amount
                        FROM FinancialRecord
                        WHERE RecordDate BETWEEN %s AND %s
                    """, (start_date, end_date))

            rows = c.fetchall()
            if rows:
                print(Style.BRIGHT + Fore.BLUE +f"\n--- Financial Records from {start_date} to {end_date} ---")
                for row in rows:
                    print(f"Record ID     : {row[0]}")
                    print(f"Employee ID   : {row[1]}")
                    print(f"Date          : {row[2]}")
                    print(f"Description   : {row[3]}")
                    print(f"Amount        : {float(row[4])}")
                    print(Style.BRIGHT + Fore.BLUE +"----------------------------")
            else:
                print(Style.BRIGHT + Fore.LIGHTRED_EX +"No financial records found in this period.")
        except Exception as e:
            print(Style.BRIGHT + Fore.RED +f"Error generating financial report: {e}")
