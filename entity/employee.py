#Employee:
#Properties: EmployeeID, FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position, JoiningDate, TerminationDate
#Methods: CalculateAge()

from datetime import date

from colorama import Fore, Style, init
init(autoreset=True)

class Employee:
    def __init__(self,employee_id=None,first_name="",last_name="",dob=None,gender="",email="",phone_number="",address="",position="",joining_date=None,termination_date=None):
        self.__employee_id=employee_id
        self.__first_name=first_name
        self.__last_name=last_name
        self.__dob=dob
        self.__gender=gender
        self.__email=email
        self.__phone_number=phone_number
        self.__address=address
        self.__position=position
        self.__joining_date=joining_date
        self.__termination_date=termination_date

#PROPERTIES - used to define getters and setters
    #getters-to print/retrieve value
    #setter-to set or change value

    def get_employee_id(self):
        return self.__employee_id
    def set_employee_id(self, value):
        self.__employee_id=value


    def get_first_name(self):
        return self.__first_name
    def set_first_name(self, value):
        self.__first_name=value


    def get_last_name(self):
        return self.__last_name
    def set_last_name(self, value):
        self.__last_name=value


    def get_dob(self):
        return self.__dob
    def set_dob(self, value):
        self.__dob=value


    def get_gender(self):
        return self.__gender
    def set_gender(self, value):
        self.__gender=value


    def get_email(self):
        return self.__email
    def set_email(self, value):
        self.__email=value


    def get_phone_number(self):
        return self.__phone_number
    def set_phone_number(self, value):
        self.__phone_number=value


    def get_address(self):
        return self.__address
    def set_address(self, value):
        self.__address=value


    def get_position(self):
        return self.__position
    def set_position(self, value):
        self.__position=value


    def get_joining_date(self):
        return self.__joining_date
    def set_joining_date(self, value):
        self.__joining_date=value


    def get_termination_date(self):
        return self.__termination_date
    def set_termination_date(self, value):
        self.__termination_date=value

#METHOD
    def calculate_age(self):
        if self.__dob is None:
            return None
        today=date.today()
        return today.year-self.__dob.year-((today.month,today.day) < (self.__dob.month,self.__dob.day))

#__str__ method
    def __str__(self):
        return Style.BRIGHT + Fore.BLUE + f"""Employee Details:
    Employee ID     : {self.__employee_id}
    First Name      : {self.__first_name}
    Last Name       : {self.__last_name}
    Age             : {self.__dob}
    Gender          : {self.__gender}
    Email           : {self.__email}
    Phone Number    : {self.__phone_number}
    Address         : {self.__address}
    Position        : {self.__position}
    Joining Date    : {self.__joining_date}
    Termination Date: {self.__termination_date if self.__termination_date else 'N/A'}
    """


