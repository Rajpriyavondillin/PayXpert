#• Payroll:
# Properties: PayrollID, EmployeeID, PayPeriodStartDate, PayPeriodEndDate, BasicSalary, OvertimePay, Deductions, NetSalary
from datetime import date

from colorama import Fore, Style, init
init(autoreset=True)

class Payroll:
    def __init__(self,payroll_id=None,employee_id=None,pay_period_start_date=None,pay_period_end_date=None,basic_salary=None,overtime_pay=None,deductions=None,net_salary=None):
        self.__payroll_id=payroll_id
        self.__employee_id=employee_id
        self.__pay_period_start_date=pay_period_start_date
        self.__pay_period_end_date=pay_period_end_date
        self.__basic_salary=basic_salary
        self.__overtime_pay=overtime_pay
        self.__deductions=deductions
        self.__net_salary=net_salary


    def get_payroll_id(self):
        return self.__payroll_id
    def set_payroll_id(self,value):
        self.__payroll_id=value


    def get_employee_id(self):
        return self.__employee_id
    def set_employee_id(self,value):
        self.__employee_id=value


    def get_pay_period_start_date(self):
        return self.__pay_period_start_date
    def set_pay_period_start_date(self, value):
        self.__pay_period_start_date = value


    def get_pay_period_end_date(self):
        return self.__pay_period_end_date
    def set_pay_period_end_date(self, value):
        self.__pay_period_end_date = value


    def get_basic_salary(self):
        return self.__basic_salary
    def set_basic_salary(self, value):
        self.__basic_salary = value


    def get_overtime_pay(self):
        return self.__overtime_pay
    def set_overtime_pay(self, value):
        self.__overtime_pay = value


    def get_deductions(self):
        return self.__deductions
    def set_deductions(self, value):
        self.__deductions = value


    def get_net_salary(self):
        return self.__net_salary
    def set_net_salary(self, value):
        self.__net_salary = value

    def __str__(self):
        return Style.BRIGHT + Fore.BLUE +f"""Payroll Details:
    Payroll ID: {self.__payroll_id}
    Employee ID: {self.__employee_id}
    Pay Period: {self.__pay_period_start_date} to {self.__pay_period_end_date}
    Basic Salary: {float(self.__basic_salary)}
    Overtime Pay: {float(self.__overtime_pay)}
    Deductions: {float(self.__deductions)}
    Net Salary: {float(self.__net_salary)}
    """


