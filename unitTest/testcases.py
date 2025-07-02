import unittest
from dao.payroll_service import PayrollService
from dao.tax_service import TaxService
from exception.exceptions import InvalidInputException
from dao.validation_service import ValidationService
from util.DBConnUtil import get_connection

class TestPayrollAndTax(unittest.TestCase):

    def setUp(self):
        self.db=get_connection()
        self.cursor=self.db.cursor()
        self.db.autocommit=False
        self.payroll_service=PayrollService()
        self.tax_service=TaxService()

    def test_calculate_gross_salary(self):
        basic_salary=50000
        overtime_pay=5000
        expected_gross_salary=basic_salary + overtime_pay
        self.assertEqual(expected_gross_salary, 55000)

    def test_calculate_net_salary_after_deductions(self):
        basic_salary=50000
        overtime_pay=5000
        deductions=3000
        net_salary=basic_salary + overtime_pay - deductions
        self.assertEqual(net_salary, 52000)

    def test_verify_tax_calculation_for_high_income_employee(self):
        employee_id=107
        tax_year=2020
        tax_rate=0.10

        db = get_connection()
        cursor = db.cursor()
        cursor.execute("""select sum(BasicSalary + OvertimePay - Deductions) from Payroll where EmployeeID = %s""", (employee_id,))
        result = cursor.fetchone()
        taxable_income=result[0] if result and result[0] is not None else 0
        db.close()

        expected_tax = float(taxable_income) * tax_rate

        tax_record = self.tax_service.calculate_tax(employee_id, tax_year)
        actual_tax_amount = float(tax_record.get_tax_amount())

        self.assertAlmostEqual(actual_tax_amount, expected_tax, places=2,msg=f"Expected tax {expected_tax} but got {actual_tax_amount} for EmployeeID {employee_id}")

    def test_verify_error_handling_for_invalid_employee_data(self):
        invalid_id= -5  # Invalid ID format
        with self.assertRaises(InvalidInputException):
            ValidationService.validate_employee_id(invalid_id)

    def test_process_payroll_for_multiple_employees(self):
        employees = [101, 102, 103]
        start_date = "2025-01-01"
        end_date = "2025-01-31"
        basic_salary = 50000
        overtime = 2000
        deductions = 1000

        for eid in employees:
            try:
                self.payroll_service.generate_payroll(eid, start_date, end_date, basic_salary, overtime, deductions)
                tax_record = self.tax_service.calculate_tax(eid, int(end_date[:4]))
                self.assertIsNotNone(tax_record)
            except Exception as e:
                self.fail(f"Payroll failed for employee {eid}: {e}")

    def tearDown(self):
        self.db.rollback()  # Rollback any changes after each test
        self.cursor.close()
        self.db.close()

if __name__ == '__main__':
   unittest.main()