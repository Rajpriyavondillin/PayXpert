from util.DBConnUtil import get_connection
from dao.i_employee_service import IEmployeeService
from exception.exceptions import EmployeeNotFoundException
from entity.employee import Employee
from dao.validation_service import ValidationService
from datetime import datetime
from exception.exceptions import InvalidInputException

from colorama import Fore, Style, init
init(autoreset=True)

class EmployeeService(IEmployeeService):
    def get_employee_by_id(self,employee_id):
        db=get_connection()
        c=db.cursor()
        c.execute("select * from employee where EmployeeID=%s",(employee_id,))
        row=c.fetchone()
        if row is None:
            raise EmployeeNotFoundException(Style.BRIGHT + Fore.RED +"Employee Not Found")
        emp=Employee(*row)  #unpack tuple to object->Mapping
        return emp

    def get_all_employees(self):
        db=get_connection()
        c=db.cursor()
        c.execute("select * from employee")
        rows=c.fetchall()
        return rows

    def add_employee(self):
        try:
            db = get_connection()
            c = db.cursor()

            first_name = input("Enter First Name: ").strip()
            ValidationService.validate_name(first_name)

            last_name = input("Enter Last Name: ").strip()
            ValidationService.validate_name(last_name)

            dob = input("Enter DOB (YYYY-MM-DD): ").strip()
            gender = input("Enter Gender: ").strip()

            email = input("Enter Email: ").strip()
            ValidationService.validate_email(email)

            phone_number = input("Enter Phone Number: ").strip()
            ValidationService.validate_phone(phone_number)

            address = input("Enter Address: ").strip()
            position = input("Enter Position: ").strip()
            joining_date = input("Enter Joining Date (YYYY-MM-DD): ").strip()
            termination_date = input("Enter Termination Date (YYYY-MM-DD) or leave blank: ").strip()

            emp = Employee(
                None,
                first_name,
                last_name,
                datetime.strptime(dob, "%Y-%m-%d"),
                gender,
                email,
                phone_number,
                address,
                position,
                datetime.strptime(joining_date, "%Y-%m-%d"),
                datetime.strptime(termination_date, "%Y-%m-%d") if termination_date else None
            )

            # Generate new ID
            c.execute("SELECT MAX(EmployeeID) FROM employee")
            row = c.fetchone()
            new_employee_id = 1 if row[0] is None else row[0] + 1

            ValidationService.validate_employee_id(new_employee_id)
            emp.set_employee_id(new_employee_id)

            c.execute("""
                INSERT INTO Employee
                (EmployeeID, FirstName, LastName, DateOfBirth, Gender, Email,
                 PhoneNumber, Address, Position, JoiningDate, TerminationDate)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                emp.get_employee_id(), emp.get_first_name(), emp.get_last_name(),
                emp.get_dob(), emp.get_gender(), emp.get_email(),
                emp.get_phone_number(), emp.get_address(), emp.get_position(),
                emp.get_joining_date(), emp.get_termination_date()
            ))

            db.commit()
            db.close()
            print(Style.BRIGHT + Fore.GREEN +"Employee Added Successfully")

        except InvalidInputException as e:
            print(Style.BRIGHT + Fore.RED +f"Invalid Input: {e}")
        except ValueError:
            print(Style.BRIGHT + Fore.RED +"Invalid date format. Please use YYYY-MM-DD.")
        except Exception as e:
            print(Style.BRIGHT + Fore.RED +f"Failed to add employee: {e}")

    def update_employee(self, employee):
        db = get_connection()
        cursor = db.cursor()

        # Check if employee exists
        cursor.execute("SELECT * FROM Employee WHERE EmployeeID = %s", (employee.get_employee_id(),))
        if cursor.fetchone() is None:
            raise EmployeeNotFoundException(Style.BRIGHT + Fore.RED +"Employee not found")

        # Update employee details
        cursor.execute("""
            UPDATE Employee
            SET FirstName=%s, LastName=%s, DateOfBirth=%s, Gender=%s,
                Email=%s, PhoneNumber=%s, Address=%s, Position=%s,
                JoiningDate=%s, TerminationDate=%s
            WHERE EmployeeID=%s
        """, (
            employee.get_first_name(), employee.get_last_name(), employee.get_dob(),
            employee.get_gender(), employee.get_email(), employee.get_phone_number(),
            employee.get_address(), employee.get_position(), employee.get_joining_date(),
            employee.get_termination_date(), employee.get_employee_id()
        ))

        db.commit()
        cursor.close()
        db.close()
        print(Style.BRIGHT + Fore.GREEN +"Employee updated successfully.")

    def remove_employee(self, employee_id):
        db=get_connection()
        c=db.cursor()
        c.execute("delete from employee where EmployeeID=%s",(employee_id,))
        db.commit()
        db.close()
        print(Style.BRIGHT + Fore.GREEN +"Employee Removed Successfully")
