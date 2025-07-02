#FinancialRecord:
#Properties: RecordID, EmployeeID, RecordDate, Description, Amount, RecordType

from datetime import date

from colorama import Fore, Style, init
init(autoreset=True)

class FinancialRecord:
    def __init__(self,record_id=None,employee_id=None,record_date=None,description="",amount=None,record_type=""):
        self.__record_id=record_id
        self.__employee_id=employee_id
        self.__record_date=record_date
        self.__description=description
        self.__amount=amount
        self.__record_type=record_type


    def get_record_id(self):
        return self.__record_id
    def set_record_id(self,value):
        self.__record_id=value


    def get_employee_id(self):
        return self.__employee_id
    def set_employee_id(self,value):
        self.__employee_id=value


    def get_record_date(self):
        return self.__record_date
    def set_record_date(self, value):
        self.__record_date = value


    def get_description(self):
        return self.__description
    def set_description(self, value):
        self.__description = value


    def get_amount(self):
        return self.__amount
    def set_amount(self, value):
        self.__amount = value


    def get_record_type(self):
        return self.__record_type
    def set_record_type(self, value):
        self.__record_type = value

    def __str__(self):
        return Style.BRIGHT + Fore.BLUE +f"""Financial Record:
    Record ID: {self.__record_id}
    Record Date: {self.__record_date}
    Description: {self.__description}
    Amount: {float(self.__amount)}
    Type: {self.__record_type}
    """

