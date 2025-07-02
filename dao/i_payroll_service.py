from abc import ABC,abstractmethod
from entity.payroll import Payroll

class IPayrollService(ABC):

    @abstractmethod
    def generate_payroll(self, employee_id, pay_period_start_date, pay_period_end_date, basic_salary, overtime_pay, deductions):
        pass

    @abstractmethod
    def get_payroll_by_id(self,payroll_id):
        pass

    @abstractmethod
    def get_payrolls_for_employee(self,employee_id):
        pass

    @abstractmethod
    def get_payrolls_for_period(self,pay_period_start_date,pay_period_end_date):
        pass
