from util.DBConnUtil import get_connection
from exception.exceptions import TaxCalculationException
from dao.i_tax_service import ITaxService
from entity.tax import Tax
from decimal import Decimal

from colorama import Fore, Style, init
init(autoreset=True)


class TaxService(ITaxService):
    def calculate_tax(self, employee_id, tax_year):
        try:
            db=get_connection()
            c=db.cursor()

            c.execute("select sum(BasicSalary+OvertimePay-Deductions) as 'TaxableIncome' from Payroll where EmployeeID=%s",(employee_id,))
            result=c.fetchone()

            if result and result[0] is not None: #result(tuple) result[0] is the 1st value in that tuple
                taxable_income=result[0]
            else:
                taxable_income=0

            total_tax_amount=taxable_income*Decimal('0.10') #assuming tax rate as 10%

            c.execute("select max(TaxId) from tax")
            row=c.fetchone()
            new_tax_id=1 if row[0] is None else row[0]+1

            tax = Tax()
            tax.set_tax_id(new_tax_id)
            tax.set_employee_id(employee_id)
            tax.set_tax_year(tax_year)
            tax.set_taxable_income(taxable_income)
            tax.set_tax_amount(total_tax_amount)

            c.execute("""insert into tax(TaxID,EmployeeID,TaxYear,TaxableIncome,TaxAmount)
                      values
                      (%s,%s,%s,%s,%s)""",(new_tax_id,tax.get_employee_id(),tax.get_tax_year(),tax.get_taxable_income(),total_tax_amount)
                     )
            db.commit()
            db.close()
            print(Style.BRIGHT + Fore.GREEN +"Tax Calculated and Recorded Successfully")
            return tax

        except Exception as e:
            raise TaxCalculationException(Style.BRIGHT + Fore.RED +f"Failed to Calculate Tax {e}")

    def get_tax_by_id(self, tax_id):
        db=get_connection()
        c=db.cursor()
        c.execute("select * from tax where TaxID=%s",(tax_id,))
        return c.fetchone()

    def get_taxes_for_employee(self, employee_id):
        db =get_connection()
        c = db.cursor()
        c.execute("select * from tax where EmployeeID=%s",(employee_id,))
        return c.fetchall()

    def get_taxes_for_year(self, tax_year):
        db =get_connection()
        c = db.cursor()
        c.execute("select * from tax where TaxYear=%s", (tax_year,))
        return c.fetchall()

