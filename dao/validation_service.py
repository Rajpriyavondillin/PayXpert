from exception.exceptions import InvalidInputException
import re

from colorama import Fore, Style, init
init(autoreset=True)

class ValidationService:
    @staticmethod
    def validate_salary_inputs(basic_salary,overtime_pay,deductions):
        if basic_salary < 0 or overtime_pay < 0 or deductions < 0:
            raise InvalidInputException(Style.BRIGHT + Fore.RED +"Salary inputs must be non-negative")

    @staticmethod
    def validate_employee_id(employee_id):
        if not isinstance(employee_id, int) or employee_id <= 0:
            raise InvalidInputException(Style.BRIGHT + Fore.RED +f"Invalid Employee ID: {employee_id}")

    @staticmethod
    def validate_email(email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, email):
            raise InvalidInputException(Style.BRIGHT + Fore.RED +"Invalid email format")

    @staticmethod
    def validate_phone(phone):
        if not phone.isdigit() or len(phone) != 10:
            raise InvalidInputException(Style.BRIGHT + Fore.RED +"Phone number must be 10 digits")

    @staticmethod
    def validate_name(name):
        if not name.isalpha():
            raise InvalidInputException(Style.BRIGHT + Fore.RED +"Name must contain only alphabetic characters.")
