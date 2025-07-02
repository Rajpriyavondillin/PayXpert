import mysql.connector

from colorama import Fore, Style, init
init(autoreset=True)

#CONNECTION ESTABLISHMENT
db=mysql.connector.connect(host='localhost',user='root',password="Riya@1105")
c=db.cursor()

#CREATION OF DB
c.execute('create database if not exists payXpertDB')
c.execute('use payXpertDB')

#CREATION OF TABLES
c.execute(
    '''create table if not exists Employee(
    EmployeeID int primary key,
    FirstName varchar(50) not null,
    LastName varchar(50) not null,
    DateOfBirth date,
    Gender varchar(15),
    Email varchar(50) unique,
    PhoneNumber varchar(15) unique,
    Address varchar(100),
    Position varchar(30),
    JoiningDate date,
    TerminationDate date)'''
)

c.execute(
    '''create table if not exists Payroll(
    PayrollID int primary key,
    EmployeeID int references Employee(EmployeeID),
    PayPeriodStartDate date,
    PayPeriodEndDate date,
    BasicSalary decimal(10,2),
    OvertimePay decimal(10,2),
    Deductions decimal(10,2),
    NetSalary decimal(10,2))'''
)

c.execute(
    '''create table if not exists Tax(
    TaxID int primary key,
    EmployeeID int references Employee(EmployeeID),
    TaxYear int,
    TaxableIncome decimal(10,2),
    TaxAmount decimal(10,2))'''
)

c.execute(
    '''create table if not exists FinancialRecord(
    RecordID int primary key,
    EmployeeID int references Employee(EmployeeID),
    RecordDate date,
    Description varchar(100),
    Amount decimal(10,2),
    RecordType varchar(50))'''
)

print(Style.BRIGHT + Fore.GREEN +"Tables Created Successfully")

#INSERTION OF RECORDS IN EACH TABLE
c.execute("""
insert into Employee
    (EmployeeID, FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position, JoiningDate, TerminationDate)
    values 
    (101, 'Raj', 'Priya', '2004-05-11', 'F', 'raj101@mail.com', '9994335933', 'Coimbatore', 'Manager', '2022-01-15', NULL),
    (102, 'Anusuya', 'Thangaraj', '2003-04-05', 'F', 'anu102@mail.com', '9000000002', 'Coimbatore', 'HR', '2021-02-01', NULL),
    (103, 'Vikram', 'Singh', '1998-06-25', 'M', 'vikram103@mail.com', '9557457403', 'Salem', 'Developer', '2020-08-10', NULL),
    (104, 'Priya', 'Menon', '2001-05-05', 'F', 'priya104@mail.com', '9080786757', 'Coimbatore', 'Tester', '2023-03-05', NULL),
    (105, 'Karthik', 'Raj', '1997-12-20', 'M', 'karthik105@mail.com', '9079735674', 'Trichy', 'Analyst', '2019-11-01', NULL),
    (106, 'Divya', 'Shree', '2000-07-12', 'F', 'divya106@mail.com', '9567533469', 'Chennai', 'Designer', '2022-06-10', NULL),
    (107, 'Arun', 'Babu', '1995-02-28', 'M', 'arun107@mail.com', '9090905678', 'Erode', 'Manager', '2018-09-15', NULL),
    (108, 'Sneha', 'Reddy', '1999-09-09', 'F', 'sneha108@mail.com', '9678903456', 'Madurai', 'Support', '2020-10-20', NULL),
    (109, 'Siva', 'Vikram', '1996-11-11', 'M', 'siva109@mail.com', '8903456789', 'Tirunelveli', 'Admin', '2017-12-01', NULL),
    (110, 'Keerthi', 'Ganesh', '2002-04-18', 'F', 'keerthi110@mail.com', '7856357890', 'Chengalpattu', 'Intern', '2024-01-05',NULL);""")

c.execute("""
    insert into Payroll 
    (PayrollID, EmployeeID, PayPeriodStartDate, PayPeriodEndDate, BasicSalary, OvertimePay, Deductions, NetSalary) 
    values
    (201, 101, '2025-05-01', '2025-05-31', 50000, 5000, 2000, 53000),
    (202, 102, '2025-05-01', '2025-05-31', 40000, 4000, 1500, 42500),
    (203, 103, '2025-05-01', '2025-05-31', 45000, 3000, 1000, 47000),
    (204, 104, '2025-05-01', '2025-05-31', 30000, 2000, 800, 31200),
    (205, 105, '2025-05-01', '2025-05-31', 55000, 3500, 2500, 56000),
    (206, 106, '2025-05-01', '2025-05-31', 42000, 2500, 2000, 42500),
    (207, 107, '2025-05-01', '2025-05-31', 60000, 4000, 3000, 61000),
    (208, 108, '2025-05-01', '2025-05-31', 32000, 1000, 1000, 32000),
    (209, 109, '2025-05-01', '2025-05-31', 48000, 3000, 1800, 49200),
    (210, 110, '2025-05-01', '2025-05-31', 25000, 1500, 500,26000);""")

c.execute("""
    insert into Tax 
    (TaxID, EmployeeID, TaxYear, TaxableIncome, TaxAmount)
    values 
    (301, 101, 2025, 600000, 60000),
    (302, 102, 2023, 480000, 45000),
    (303, 103, 2024, 530000, 50000),
    (304, 104, 2022, 360000, 30000),
    (305, 105, 2021, 640000, 65000),
    (306, 106, 2020, 520000, 46000),
    (307, 107, 2020, 700000, 75000),
    (308, 108, 2021, 384000, 31000),
    (309, 109, 2025, 576000, 58000),
    (310, 110, 2024, 300000,20000);""")

c.execute("""
    insert into FinancialRecord 
    (RecordID, EmployeeID, RecordDate, Description, Amount, RecordType) 
    values 
    (401, 101, '2025-05-31', 'Salary Credit', 53000, 'Income'),
    (402, 102, '2025-05-31', 'Salary Credit', 42500, 'Income'),
    (403, 103, '2025-05-31', 'Salary Credit', 47000, 'Income'),
    (404, 104, '2025-05-31', 'Salary Credit', 31200, 'Income'),
    (405, 105, '2025-05-31', 'Salary Credit', 56000, 'Income'),
    (406, 106, '2025-06-30', 'Tax Paid', 2000, 'Tax Payment'),
    (407, 107, '2024-01-31', 'Office Travel Expense', 3000, 'Expense'),
    (408, 108, '2025-06-30', 'Tax Paid', 1000, 'Tax Payment'),
    (409, 109, '2025-05-31', 'Salary Credit', 49200, 'Income'),
    (410, 110, '2025-05-31', 'Salary Credit', 26000,'Income');""")

db.commit()
print(Style.BRIGHT + Fore.GREEN +"Records Inserted Successfully")
db.close()