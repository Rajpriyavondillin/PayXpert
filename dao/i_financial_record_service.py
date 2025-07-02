from abc import ABC ,abstractmethod
from entity.financial_record import FinancialRecord

class IFinancialService(ABC):
    @abstractmethod
    def add_financial_record(self,employee_id,description,amount,record_type):
        pass

    @abstractmethod
    def get_financial_record_by_id(self,record_id):
        pass

    @abstractmethod
    def get_financial_records_for_employee(self,employee_id):
        pass

    @abstractmethod
    def get_financial_records_for_date(self,record_date):
        pass
