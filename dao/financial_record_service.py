from entity.financial_record import FinancialRecord
from dao.i_financial_record_service import IFinancialService
from exception.exceptions import FinancialRecordException
from util.DBConnUtil import get_connection

from colorama import Fore, Style, init
init(autoreset=True)

from datetime import date

class FinancialRecordService(IFinancialService):

    def add_financial_record(self, employee_id, description, amount, record_type):
        try:
            db =get_connection()
            c = db.cursor()

            c.execute("SELECT MAX(RecordID) FROM FinancialRecord")
            row = c.fetchone()
            new_record_id = 1 if row[0] is None else row[0] + 1

            record_date = date.today()

            fr = FinancialRecord()
            fr.set_record_id(new_record_id)
            fr.set_employee_id(employee_id)
            fr.set_record_date(record_date)
            fr.set_description(description)
            fr.set_amount(amount)
            fr.set_record_type(record_type)

            c.execute("""
                INSERT INTO FinancialRecord (RecordID, EmployeeID, RecordDate, Description, Amount, RecordType)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                fr.get_record_id(), fr.get_employee_id(), fr.get_record_date(),
                fr.get_description(), fr.get_amount(), fr.get_record_type()
            ))

            db.commit()
            db.close()
            print(Style.BRIGHT + Fore.GREEN +"Financial Record Added Successfully")

        except Exception as e:
            raise FinancialRecordException(Style.BRIGHT + Fore.RED +f"Failed to add Financial Record: {e}")

    def get_financial_record_by_id(self,record_id):
        db=get_connection()
        c=db.cursor()
        c.execute("select * from FinancialRecord where RecordID=%s",(record_id,))
        return c.fetchone()

    def get_financial_records_for_employee(self,employee_id):
        db=get_connection()
        c=db.cursor()
        c.execute("select * from FinancialRecord where EmployeeID=%s",(employee_id,))
        return c.fetchall()

    def get_financial_records_for_date(self,record_date):
        db=get_connection()
        c=db.cursor()
        c.execute("select * from FinancialRecord where recordDate=%s",(record_date,))
        return c.fetchall()
