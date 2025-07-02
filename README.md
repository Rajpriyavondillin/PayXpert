# 💼 PayXpert – Payroll Management System

PayXpert is a menu-driven, object-oriented payroll management system built using **Python** and **MySQL**. It provides efficient employee, payroll, tax, and financial record management with database integration, user-defined exceptions, validation, reports, and CSV export functionality.

---

## 🚀 Features

✅ **Employee Management**  
- Add, view, update, and delete employees  
- Field-specific update with validation  
- Date and email format validation

✅ **Payroll Processing**  
- Generate payroll based on basic salary, overtime, and deductions  
- View payroll by ID, by employee, or by period  
- Net salary calculation

✅ **Tax Management**  
- Automatic tax calculation based on net salary  
- View tax by ID, employee, or tax year  
- Vertical display with color formatting

✅ **Financial Records**  
- Add and view financial records  
- View by Record ID, Employee ID, or Date

✅ **Report Generation**  
- Salary, Tax, and Financial Reports  
- Export reports to CSV format  
- Optional date range-based filtering

✅ **Color-Coded Output**  
- Enhanced terminal readability using `colorama`  
- Section-based highlights

---

## 🛠️ Technologies Used

- **Python 3.10+**
- **MySQL** with `mysql-connector-python`
- **colorama** for colored CLI output
- **unittest** for testing

---

## 🧩 Project Structure

```text
PayXpert/
│
├── main/
│ └── main_module.py # Entry point – menu-driven interface
│
├── entity/
│ ├── employee.py
│ ├── payroll.py
│ ├── tax.py
│ └── financial_record.py
│
├── dao/
│ ├── employee_service.py
│ ├── payroll_service.py
│ ├── tax_service.py
│ ├── financial_record_service.py
│ ├── report_generator.py
│ └── validation_service.py
│
├── util/
│ ├── DBConnUtil.py
│ └── DBPropertyUtil.py
│
├── exception/
│ └── exceptions.py
│
├── unitTest/
│ └── testcases.py
│
├── db.properties # DB configuration file
└── requirements.txt # List of dependencies

---

## ⚙️ Setup Instructions

1. 📦 Install Dependencies

In pycharm terminal,
pip install mysql-connector-python colorama

---

2. 🗂️ Create db.properties
Add your DB credentials:

properties
Copy code
host=localhost
user=root
password=your_password
database=payXpertDB

---

3. 🧱 Database Setup
Use the setup script to create database and tables, or do it manually.

---

4. ▶️ Run the Application
python main/main_module.py


