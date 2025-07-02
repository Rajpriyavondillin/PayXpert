from util.DBConnUtil import get_connection
from dao.i_payroll_service import IPayrollService
from exception.exceptions import PayrollGenerationException
from dao.validation_service import ValidationService
from dao.tax_service import TaxService

from colorama import Fore, Style, init
init(autoreset=True)

class PayrollService(IPayrollService):


    def generate_payroll(self,employee_id,pay_period_start_date,pay_period_end_date,basic_salary,overtime_pay,deductions):
        try:
            net_salary = basic_salary + overtime_pay - deductions

            ValidationService.validate_employee_id(employee_id)
            ValidationService.validate_salary_inputs(basic_salary, overtime_pay, deductions)

            db = get_connection()
            c = db.cursor()

            # Generate new PayrollID
            c.execute("SELECT MAX(PayrollID) FROM payroll")
            row = c.fetchone()
            new_payroll_id = 1 if row[0] is None else row[0] + 1

            # Insert into Payroll table
            c.execute("""
                        INSERT INTO Payroll 
                        (PayrollID, EmployeeID, PayPeriodStartDate, PayPeriodEndDate,
                         BasicSalary, OvertimePay, Deductions, NetSalary)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (new_payroll_id, employee_id, pay_period_start_date, pay_period_end_date,
            basic_salary, overtime_pay, deductions, net_salary))

            db.commit()
            c.close()
            db.close()

            print(Style.BRIGHT + Fore.GREEN +"Payroll Generated Successfully")

            tax_service=TaxService()
            tax_service.calculate_tax(employee_id, int(pay_period_end_date[:4]))

        except Exception as e:
            raise PayrollGenerationException(Style.BRIGHT + Fore.RED +f"Failed to generate payroll: {e}")

    def get_payroll_by_id(self, payroll_id):
        db=get_connection()
        c=db.cursor()
        c.execute("select * from payroll where PayrollID=%s",(payroll_id,))
        row=c.fetchone()
        columns = ['PayrollID', 'EmployeeID', 'StartDate', 'EndDate', 'BasicSalary', 'OvertimePay', 'Deductions',
                   'NetSalary']
        if row:
            return dict(zip(columns,row))
        else:
            return None

    def get_payrolls_for_employee(self, employee_id):
        db =get_connection()
        c = db.cursor()
        c.execute("select * from payroll where EmployeeID=%s", (employee_id,))
        return c.fetchall()

    def get_payrolls_for_period(self, pay_period_start_date, pay_period_end_date):
        db =get_connection()
        c = db.cursor()
        c.execute("select * from payroll where PayPeriodStartDate>= %s AND PayPeriodEndDate<= %s", (pay_period_start_date,pay_period_end_date))
        return c.fetchall()


