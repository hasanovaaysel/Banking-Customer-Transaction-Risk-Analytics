# 🏦 Banking Customer, Transaction & Risk Analytics

An end-to-end banking analytics project focused on analyzing customers, accounts, transactions, loans, cards, complaints, branches, and campaigns using **MySQL, Python, Pandas, and Excel**.

## 📌 Project Overview

This project analyzes banking data to identify customer behavior, transaction patterns, branch performance, loan trends, and potential risk indicators.

The project follows an end-to-end data analytics workflow:

**MySQL → Python & Pandas → Excel Dashboard → Business Insights**

## 🎯 Business Objectives

* Analyze customer and account activity
* Understand transaction behavior and transaction status
* Evaluate branch performance
* Analyze loan distribution and loan status
* Examine loan payment patterns
* Analyze card usage
* Explore customer complaints
* Evaluate campaign performance
* Identify useful business and risk-related insights

## 🛠️ Technologies

* **MySQL** — Database creation, data storage, relationships, and SQL analysis
* **Python** — Data generation and analysis
* **Pandas** — Data manipulation and exploratory analysis
* **Excel** — Dashboard development and data visualization

## 🗄️ Database Structure

The project contains 10 main tables:

* Customers
* Branches
* Employees
* Accounts
* Transactions
* Loans
* Loan Payments
* Cards
* Complaints
* Campaigns

These tables are connected through relational keys to represent a realistic banking data environment.

## 🐍 Python & Pandas Analysis

Python was used to generate and work with the banking dataset.

Pandas was used for:

* Data loading
* Data exploration
* Grouping and aggregation
* Transaction status analysis
* Branch performance analysis
* Monthly transaction type analysis
* Loan status analysis

## 📊 Excel Dashboard

The final analysis was visualized in an interactive Excel dashboard.

The dashboard includes KPI cards, charts, and filters for exploring important banking metrics.

### Key KPIs

* Total Branches
* Total Customers
* Total Transactions
* Transaction Value
* Average Transaction

### Dashboard Analysis

The dashboard focuses on:

* Transaction performance
* Transaction status
* Transaction types
* Branch performance
* Customer activity
* Loan performance
* Banking trends

## 📁 Project Structure

```text
Banking-Customer-Transaction-Risk-Analytics/
│
├── bank.py
├── bank.sql
├── banking_analyticss.xlsx
└── README.md
```

## ▶️ How to Run

### 1. Create the database

Run `bank.sql` in MySQL to create the database, tables, and relationships.

### 2. Configure MySQL

Open `bank.py` and enter your own MySQL credentials:

```python
connection = mysql.connector.connect(
    host="localhost",
    user="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    database="banking_analytics_db"
)
```

### 3. Install required libraries

```bash
pip install pandas mysql-connector-python
```

### 4. Run the Python script

```bash
python bank.py
```

The script generates and inserts the banking data into MySQL and performs the required Pandas analysis.

## 📈 Key Skills Demonstrated

* Relational Database Design
* SQL
* MySQL
* Python
* Pandas
* Data Analysis
* Data Cleaning
* Exploratory Data Analysis
* Excel
* Pivot Tables
* Interactive Dashboards
* Business Analytics
* Banking & Risk Analytics

## 🚀 Future Improvements

Possible future extensions include:

* Power BI dashboard
* Advanced customer segmentation
* More detailed risk scoring
* Predictive analytics
* Automated reporting
* Advanced SQL analysis

## 👩‍💻 Author

**Aysel Hasanova**

Aspiring Data Analyst interested in **SQL, Python, Excel, Power BI, and Business Analytics**.
