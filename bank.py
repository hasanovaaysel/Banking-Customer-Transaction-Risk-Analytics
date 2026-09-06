import mysql.connector
import random
import pandas as pd
from datetime import  timedelta


# =========================================================
# 1. MYSQL CONNECTION
# =========================================================

connection = mysql.connector.connect(
    host="localhost",
    user="",
    password="",
    database="banking_analytics_db"
)




cursor = connection.cursor()

print("Connection successfully!")


# =========================================================
# 2. RANDOM DATE FUNCTION
# =========================================================

def random_date(start, end):

    difference = end - start

    random_days = random.randint(
        0,
        difference.days
    )

    return start + timedelta(
        days=random_days
    )


# # =========================================================
# # 3. BASIC DATA
# # =========================================================

# first_names = [
#     "Aysel", "Leyla", "Aylin", "Aynur", "Ayan",
#     "Nigar", "Zehra", "Gunel", "Leman", "Sabina",
#     "Melek", "Sevda", "Narmin", "Lala", "Samira",
#     "Derya", "Arzu", "Nuray", "Nurane", "Nazenin",
#     "Minaye", "Rena", "Elvin", "Murad", "Kamran",
#     "Tural", "Orkhan", "Rashad", "Emin", "Samir"
# ]

# last_names = [
#     "Hasanova",
#     "Aliyeva",
#     "Muxtarova",
#     "Agayeva",
#     "Mammadova",
#     "Ismayilova",
#     "Huseynova",
#     "Rahimova",
#     "Quliyeva",
#     "Abbasova",
#     "Aslanova",
#     "Muradova",
#     "Isayeva",
#     "Tagiyeva",
#     "Alizada"
# ]

# cities = [
#     "Baku",
#     "Ganja",
#     "Sumqayit",
#     "Mingachevir",
#     "Shaki",
#     "Lankaran",
#     "Quba",
#     "Gabala",
#     "Nakhchivan"
# ]


# # =========================================================
# # 4. CUSTOMERS
# # =========================================================

# customer_data = []

# segments = [
#     "Mass Market",
#     "Mass Affluent",
#     "Premium",
#     "Private"
# ]

# for customer_id in range(1, 10001):

#     name = (
#         random.choice(first_names)
#         + " "
#         + random.choice(last_names)
#     )

#     gender = random.choice([
#         "Female",
#         "Male"
#     ])

#     date_of_birth = random_date(
#         datetime(1960, 1, 1),
#         datetime(2008, 12, 31)
#     ).date()

#     city = random.choice(cities)

#     segment = random.choices(
#         segments,
#         weights=[55, 25, 15, 5]
#     )[0]

#     signup_date = random_date(
#         datetime(2021, 1, 1),
#         datetime(2026, 8, 29)
#     ).date()

#     status = random.choices(
#         ["Active", "Inactive"],
#         weights=[90, 10]
#     )[0]

#     customer_data.append([
#         customer_id,
#         name,
#         gender,
#         date_of_birth,
#         city,
#         segment,
#         signup_date,
#         status
#     ])


# # IMPORTANT:
# # executemany FOR LOOP-DAN SONRA olmalıdır.

# cursor.executemany(
#     """
#     INSERT INTO customers
#     (
#         customer_id,
#         customer_name,
#         gender,
#         date_of_birth,
#         city,
#         customer_segment,
#         signup_date,
#         customer_status
#     )
#     VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
#     """,
#     customer_data
# )

# connection.commit()

# print(
#     "Customers:",
#     len(customer_data)
# )


# # =========================================================
# # 5. BRANCHES
# # =========================================================

# branch_data = []

# branch_types = [
#     "Standard",
#     "Premium",
#     "Corporate",
#     "Digital Hub"
# ]

# for branch_id in range(1, 31):

#     city = random.choice(cities)

#     branch_name = (
#         city
#         + " Branch "
#         + str(branch_id)
#     )

#     branch_data.append([
#         branch_id,
#         branch_name,
#         city,
#         random.choice(branch_types),
#         random_date(
#             datetime(2015, 1, 1),
#             datetime(2024, 12, 31)
#         ).date()
#     ])


# cursor.executemany(
#     """
#     INSERT INTO branches
#     (
#         branch_id,
#         branch_name,
#         city,
#         branch_type,
#         opening_date
#     )
#     VALUES (%s,%s,%s,%s,%s)
#     """,
#     branch_data
# )

# connection.commit()

# print(
#     "Branches:",
#     len(branch_data)
# )


# # =========================================================
# # 6. EMPLOYEES
# # =========================================================

# employee_data = []

# roles = [
#     "Branch Manager",
#     "Customer Service",
#     "Loan Officer",
#     "Relationship Manager",
#     "Cashier"
# ]

# for employee_id in range(1, 301):

#     employee_name = (
#         random.choice(first_names)
#         + " "
#         + random.choice(last_names)
#     )

#     # 1-30 because we have 30 branches
#     branch_id = random.randint(1, 30)

#     employee_data.append([
#         employee_id,
#         employee_name,
#         branch_id,
#         random.choice(roles),
#         random_date(
#             datetime(2018, 1, 1),
#             datetime(2026, 8, 29)
#         ).date(),
#         random.choices(
#             ["Active", "Inactive"],
#             weights=[92, 8]
#         )[0]
#     ])


# cursor.executemany(
#     """
#     INSERT INTO employees
#     (
#         employee_id,
#         employee_name,
#         branch_id,
#         role,
#         hire_date,
#         employee_status
#     )
#     VALUES (%s,%s,%s,%s,%s,%s)
#     """,
#     employee_data
# )

# connection.commit()

# print(
#     "Employees:",
#     len(employee_data)
# )


# # =========================================================
# # 7. ACCOUNTS
# # =========================================================

# account_data = []

# account_types = [
#     "Savings",
#     "Current",
#     "Salary",
#     "Premium",
#     "Business"
# ]

# for account_id in range(1, 15001):

#     customer_id = random.randint(
#         1,
#         10000
#     )

#     branch_id = random.randint(
#         1,
#         30
#     )

#     account_type = random.choice(
#         account_types
#     )

#     opening_date = random_date(
#         datetime(2021, 1, 1),
#         datetime(2026, 8, 29)
#     ).date()

#     if account_type == "Premium":

#         balance = random.uniform(
#             50000,
#             1000000
#         )

#     elif account_type == "Business":

#         balance = random.uniform(
#             100000,
#             3000000
#         )

#     else:

#         balance = random.uniform(
#             100,
#             300000
#         )

#     status = random.choices(
#         ["Active", "Dormant", "Closed"],
#         weights=[85, 10, 5]
#     )[0]

#     account_data.append([
#         account_id,
#         customer_id,
#         branch_id,
#         account_type,
#         opening_date,
#         round(balance, 2),
#         status
#     ])


# cursor.executemany(
#     """
#     INSERT INTO accounts
#     (
#         account_id,
#         customer_id,
#         branch_id,
#         account_type,
#         opening_date,
#         current_balance,
#         account_status
#     )
#     VALUES (%s,%s,%s,%s,%s,%s,%s)
#     """,
#     account_data
# )

# connection.commit()

# print(
#     "Accounts:",
#     len(account_data)
# )


# # =========================================================
# # 8. TRANSACTIONS
# # =========================================================

# transaction_data = []

# transaction_types = [
#     "Deposit",
#     "Withdrawal",
#     "Transfer",
#     "Payment",
#     "Fee",
#     "Interest"
# ]

# channels = [
#     "Branch",
#     "ATM",
#     "Mobile App",
#     "Internet Banking",
#     "POS"
# ]

# merchant_categories = [
#     "Grocery",
#     "Fashion",
#     "Restaurant",
#     "Travel",
#     "Healthcare",
#     "Entertainment",
#     "Utilities",
#     "Electronics",
#     "Education",
#     "Other"
# ]


# for transaction_id in range(1, 150001):

#     account_id = random.randint(
#         1,
#         15000
#     )

#     transaction_type = random.choices(
#         transaction_types,
#         weights=[25, 20, 15, 25, 5, 10]
#     )[0]

#     transaction_date = random_date(
#         datetime(2024, 1, 1),
#         datetime(2026, 6, 30)
#     )

#     amount = round(
#         random.uniform(
#             10,
#             50000
#         ),
#         2
#     )

#     status = random.choices(
#         ["Success", "Failed", "Pending"],
#         weights=[94, 4, 2]
#     )[0]

#     channel = random.choice(
#         channels
#     )

#     merchant_category = random.choice(
#         merchant_categories
#     )

#     transaction_data.append([
#         transaction_id,
#         account_id,
#         transaction_date,
#         transaction_type,
#         amount,
#         status,
#         channel,
#         merchant_category
#     ])


# cursor.executemany(
#     """
#     INSERT INTO transaction
#     (
#         transaction_id,
#         account_id,
#         transaction_date,
#         transaction_type,
#         amount,
#         transaction_status,
#         channel,
#         merchant_category
#     )
#     VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
#     """,
#     transaction_data
# )

# connection.commit()

# print(
#     "Transactions:",
#     len(transaction_data)
# )


# # =========================================================
# # 9. LOANS
# # =========================================================

# loan_data = []

# loan_types = [
#     "Personal Loan",
#     "Home Loan",
#     "Car Loan",
#     "Business Loan",
#     "Education Loan"
# ]

# for loan_id in range(1, 5001):

#     customer_id = random.randint(
#         1,
#         10000
#     )

#     loan_type = random.choice(
#         loan_types
#     )

#     if loan_type == "Home Loan":

#         amount = random.uniform(
#             1000000,
#             10000000
#         )

#         rate = random.uniform(
#             6.5,
#             9.5
#         )

#     elif loan_type == "Business Loan":

#         amount = random.uniform(
#             500000,
#             5000000
#         )

#         rate = random.uniform(
#             8,
#             13
#         )

#     else:

#         amount = random.uniform(
#             50000,
#             1000000
#         )

#         rate = random.uniform(
#             8,
#             15
#         )

#     issue_date = random_date(
#         datetime(2021, 1, 1),
#         datetime(2026, 1, 1)
#     ).date()

#     maturity_date = (
#         issue_date
#         + timedelta(
#             days=random.randint(
#                 365,
#                 3650
#             )
#         )
#     )

#     loan_status = random.choices(
#         ["Active", "Closed", "Defaulted"],
#         weights=[75, 20, 5]
#     )[0]

#     loan_data.append([
#         loan_id,
#         customer_id,
#         loan_type,
#         round(amount, 2),
#         round(rate, 2),
#         issue_date,
#         maturity_date,
#         loan_status
#     ])


# cursor.executemany(
#     """
#     INSERT INTO loans
#     (
#         loan_id,
#         customer_id,
#         loan_type,
#         loan_amount,
#         interest_rate,
#         issue_date,
#         maturity_date,
#         loan_status
#     )
#     VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
#     """,
#     loan_data
# )

# connection.commit()

# print(
#     "Loans:",
#     len(loan_data)
# )


# # =========================================================
# # 10. LOAN PAYMENTS
# # =========================================================

# loan_payment_data = []

# payment_id = 1

# for loan in loan_data:

#     loan_id = loan[0]

#     loan_amount = loan[3]

#     issue_date = loan[5]

#     number_of_payments = random.randint(
#         3,
#         12
#     )

#     monthly_amount = (
#         loan_amount
#         / number_of_payments
#     )

#     for i in range(number_of_payments):

#         payment_date = (
#             issue_date
#             + timedelta(
#                 days=30 * (i + 1)
#             )
#         )

#         status = random.choices(
#             ["Paid", "Late", "Missed"],
#             weights=[85, 10, 5]
#         )[0]

#         loan_payment_data.append([
#             payment_id,
#             loan_id,
#             payment_date,
#             round(monthly_amount, 2),
#             status
#         ])

#         payment_id += 1


# cursor.executemany(
#     """
#     INSERT INTO loan_payments
#     (
#         payment_id,
#         loan_id,
#         payment_date,
#         payment_amount,
#         payment_status
#     )
#     VALUES (%s,%s,%s,%s,%s)
#     """,
#     loan_payment_data
# )

# connection.commit()

# print(
#     "Loan Payments:",
#     len(loan_payment_data)
# )


# # =========================================================
# # 11. CARDS
# # =========================================================

# card_data = []

# card_types = [
#     "Debit",
#     "Credit",
#     "Premium"
# ]

# card_networks = [
#     "Visa",
#     "Mastercard"
# ]


# for card_id in range(1, 12001):

#     # First choose an account
#     account = random.choice(
#         account_data
#     )

#     account_id = account[0]

#     # Get the customer who owns that account
#     customer_id = account[1]

#     issue_date = random_date(
#         datetime(2022, 1, 1),
#         datetime(2026, 1, 1)
#     ).date()

#     expiry_date = (
#         issue_date
#         + timedelta(
#             days=1460
#         )
#     )

#     card_data.append([
#         card_id,
#         customer_id,
#         account_id,
#         random.choice(card_types),
#         random.choice(card_networks),
#         issue_date,
#         expiry_date,
#         random.choices(
#             ["Active", "Blocked", "Expired"],
#             weights=[85, 5, 10]
#         )[0]
#     ])


# cursor.executemany(
#     """
#     INSERT INTO cards
#     (
#         card_id,
#         customer_id,
#         account_id,
#         card_type,
#         card_network,
#         issue_date,
#         expiry_date,
#         card_status
#     )
#     VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
#     """,
#     card_data
# )

# connection.commit()

# print(
#     "Cards:",
#     len(card_data)
# )


# # =========================================================
# # 12. COMPLAINTS
# # =========================================================

# complaint_data = []

# complaint_categories = [
#     "Card Issue",
#     "Transaction Problem",
#     "Loan Issue",
#     "Account Issue",
#     "Customer Service",
#     "ATM Problem",
#     "Mobile Banking"
# ]

# for complaint_id in range(1, 5001):

#     customer_id = random.randint(
#         1,
#         10000
#     )

#     branch_id = random.randint(
#         1,
#         30
#     )

#     complaint_date = random_date(
#         datetime(2024, 1, 1),
#         datetime(2026, 6, 30)
#     ).date()

#     status = random.choice([
#         "Resolved",
#         "Pending",
#         "Escalated"
#     ])

#     resolution_days = random.randint(
#         1,
#         30
#     )

#     complaint_data.append([
#         complaint_id,
#         customer_id,
#         branch_id,
#         complaint_date,
#         random.choice(
#             complaint_categories
#         ),
#         status,
#         resolution_days
#     ])


# cursor.executemany(
#     """
#     INSERT INTO complaints
#     (
#         complaint_id,
#         customer_id,
#         branch_id,
#         complaint_date,
#         complaint_category,
#         complaint_status,
#         resolution_days
#     )
#     VALUES (%s,%s,%s,%s,%s,%s,%s)
#     """,
#     complaint_data
# )

# connection.commit()

# print(
#     "Complaints:",
#     len(complaint_data)
# )


# # =========================================================
# # 13. CAMPAIGNS
# # =========================================================

# campaign_data = []

# campaign_names = [
#     "Premium Upgrade",
#     "Salary Account",
#     "Credit Card Cashback",
#     "Personal Loan",
#     "Home Loan",
#     "Digital Banking",
#     "Savings Boost",
#     "Investment Campaign"
# ]

# campaign_types = [
#     "Acquisition",
#     "Retention",
#     "Cross Sell",
#     "Loan",
#     "Digital"
# ]

# for campaign_id in range(1, 51):

#     start_date = random_date(
#         datetime(2024, 1, 1),
#         datetime(2026, 1, 1)
#     ).date()

#     end_date = (
#         start_date
#         + timedelta(
#             days=random.randint(
#                 14,
#                 90
#             )
#         )
#     )

#     campaign_data.append([
#         campaign_id,
#         random.choice(campaign_names),
#         random.choice(campaign_types),
#         random.choice([
#             "Email",
#             "SMS",
#             "App",
#             "Branch",
#             "Social Media"
#         ]),
#         start_date,
#         end_date,
#         round(
#             random.uniform(
#                 5000,
#                 100000
#             ),
#             2
#         ),
#         random.choice([
#             "Completed",
#             "Active",
#             "Cancelled"
#         ])
#     ])


# cursor.executemany(
#     """
#     INSERT INTO campaigns
#     (
#         campaign_id,
#         campaign_name,
#         campaign_type,
#         channel,
#         start_date,
#         end_date,
#         campaign_budget,
#         campaign_status
#     )
#     VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
#     """,
#     campaign_data
# )

# connection.commit()

# print(
#     "Campaigns:",
#     len(campaign_data)
# )


customers = pd.read_sql(
    "SELECT * FROM customers",
    connection
)

accounts = pd.read_sql(
    "SELECT * FROM accounts",
    connection
)

transactions = pd.read_sql(
    "SELECT * FROM transaction",
    connection
)

branches = pd.read_sql(
    "SELECT * FROM branches",
    connection
)

loans = pd.read_sql(
    "SELECT * FROM loans",
    connection
)
employees = pd.read_sql(
    "SELECT * FROM employees",
    connection
)

loan_payments = pd.read_sql(
    "SELECT * FROM loan_payments",
    connection
)

complaints = pd.read_sql(
    "SELECT * FROM complaints",
    connection
)

cards = pd.read_sql(
    "SELECT * FROM cards",
    connection
)
campaigns=pd.read_sql(
    "SELECT*FROM campaigns",
    connection
)
print(customers.shape)
print(customers.head())
print(customers.isnull().sum())
print(branches.isnull().sum())
print(employees.isnull().sum())
print(accounts.isnull().sum())
print(cards.isnull().sum())
print(complaints.isnull().sum())
print(campaigns.isnull().sum())

print(employees.duplicated().sum())

transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)
# print(transactions["transaction_date"])

customers["date_of_birth"]=pd.to_datetime(customers["date_of_birth"])
# print(customers["date_of_birth"])

loans["issue_date"] = pd.to_datetime(
    loans["issue_date"]
)

loans["maturity_date"] = pd.to_datetime(
    loans["maturity_date"]
)

complaints["complaint_date"] = pd.to_datetime(
    complaints["complaint_date"]
)
df=transactions.merge(accounts,on="account_id",how="left")
df=df.merge(customers,on="customer_id",how="left")
df=df.merge(branches,on="branch_id",how="left")
print(df)
print(df.isnull().sum())
print(df.duplicated().sum())

successful=df[df["transaction_status"]=="Success"].copy()
print(successful)

total_transactions=successful["amount"].sum()
print(total_transactions)

average_transactions=successful["amount"].mean()
print(average_transactions)

total_deposits = successful.loc[
    successful["transaction_type"] == "Deposit",
    "amount"
].sum()
print(total_deposits) #?????????????

total_withdrawals = successful.loc[
    successful["transaction_type"] == "Withdrawal",
    "amount"
].sum()


customer_analysis=(
    successful.groupby(["customer_id","customer_name","customer_segment"]).agg(
    transaction_count=("transaction_id","nunique"),
    transaction_value=("amount","sum")
).reset_index()

)
print(customer_analysis)


customer_analysis_best=customer_analysis.sort_values("transaction_value",ascending=False)
print(customer_analysis_best.head(10))


channel_analysis=(successful.groupby("channel").agg(
    customer_count=("customer_id","nunique"),
    transaction_count=("transaction_id","nunique"),
    transaction_value=("amount","sum"),
    average_transaction=("amount","mean")
).reset_index()
)
print(channel_analysis)



successful["month"]=(successful["transaction_date"].dt.to_period("M"))
monthly_analysis=(successful.groupby("month").agg(
    transaction_count=("transaction_id","nunique"),
    transaction_value=("amount","sum") 
).reset_index())
print(monthly_analysis)


transaction_type_analysis=(successful.groupby("transaction_type").agg(
    transaction_count=("transaction_id","nunique"),
    transaction_value=("amount","sum"),
    average_transaction=("amount","mean")

).reset_index())
print(transaction_type_analysis.head())


loan_analysis = (loans.groupby("loan_type").agg(
    loan_count=("loan_id","count"),
    total_loan_amount=("loan_amount","sum"),
    average_loan_amount=("loan_amount","mean"),
    average_interest_rate=("interest_rate","mean"))
    .reset_index()
)
print(loan_analysis)


default_rate = (loans["loan_status"].eq("Defaulted").mean()* 100)

complaint_analysis = (complaints.groupby("complaint_category").agg(
        complaint_count=("complaint_id","count"),
        average_resolution_days=("resolution_days","mean")
).reset_index())
complaint_analysis = complaint_analysis.sort_values(
    "complaint_count",
    ascending=False
)

print(complaint_analysis)


customer_best=(successful.groupby(["customer_id","customer_name"]).agg(
    transaction_count=("transaction_id","nunique"),
    transaction_value=("amount","sum")
))
print(customer_best.sort_values("transaction_value",ascending=False))


segment_analysis = (
    successful
    .groupby("customer_segment")
    .agg(
        customer_count=("customer_id", "nunique"),
        transaction_count=("transaction_id", "nunique"),
        transaction_value=("amount", "sum"),
        average_transaction=("amount", "mean")
    )
    .reset_index()
)

print(segment_analysis)


customer_status=(customers["customer_status"].value_counts())
print(customer_status)


segment_count=(successful.groupby("customer_segment").agg(
    customer_count=("customer_id","nunique"),
    transaction_value=("amount","sum")
))
print(segment_count)


city_analysis=(customers.groupby("city").agg(
    customer_count=("customer_id","nunique")
).reset_index())
print(city_analysis.sort_values("customer_count",ascending=False))


city_segment=(customers.groupby(["city","customer_segment"]).agg(
    customer_count=("customer_id","nunique")

).reset_index())
print(city_segment.sort_values("customer_count",ascending=False))


customers["signup_date"] = pd.to_datetime(
    customers["signup_date"]
)

customers["signup_year"] = (
    customers["signup_date"].dt.year
)

signup_analysis=(
    customers.groupby("signup_year").agg(
        new_customers=("customer_id","nunique")

    )
)
print(signup_analysis)


transaction_status_analysis = (
    transactions.groupby("transaction_status")
    .agg(
        transaction_count=("transaction_id", "nunique"),
        transaction_value=("amount", "sum")
    )
    .reset_index()
)



branch_analysis = (
    successful.groupby(["branch_id", "branch_name"])
    .agg(
        transaction_count=("transaction_id", "nunique"),
        transaction_value=("amount", "sum"),
        customer_count=("customer_id", "nunique"),
        average_transaction=("amount", "mean")
    )
    .reset_index()
)

monthly_type_analysis = (
    successful.groupby([
        successful["transaction_date"].dt.to_period("M"),
        "transaction_type"
    ])
    .agg(
        transaction_value=("amount", "sum")
    )
    .reset_index()
)

loan_status_analysis = (
    loans.groupby("loan_status")
    .agg(
        loan_count=("loan_id", "count"),
        total_loan_amount=("loan_amount", "sum")
    )
    .reset_index()
)


monthly_type_analysis.columns = [
    "month",
    "transaction_type",
    "transaction_value"
]

monthly_analysis["month"] = monthly_analysis["month"].astype(str)
monthly_type_analysis["month"] = monthly_type_analysis["month"].astype(str)


with pd.ExcelWriter("banking_analytics.xlsx", engine="openpyxl") as writer:

    customers.to_excel(
        writer,
        sheet_name="Customers",
        index=False
    )

    accounts.to_excel(
        writer,
        sheet_name="Accounts",
        index=False
    )

    transactions.to_excel(
        writer,
        sheet_name="Transactions",
        index=False
    )

    branches.to_excel(
        writer,
        sheet_name="Branches",
        index=False
    )

    loans.to_excel(
        writer,
        sheet_name="Loans",
        index=False
    )

    employees.to_excel(
        writer,
        sheet_name="Employees",
        index=False
    )

    loan_payments.to_excel(
        writer,
        sheet_name="Loan_Payments",
        index=False
    )

    complaints.to_excel(
        writer,
        sheet_name="Complaints",
        index=False
    )

    cards.to_excel(
        writer,
        sheet_name="Cards",
        index=False
    )

    campaigns.to_excel(
        writer,
        sheet_name="Campaigns",
        index=False
    )

    customer_analysis.to_excel(
        writer,
        sheet_name="Customer_Analysis",
        index=False
    )

    customer_analysis_best.to_excel(
        writer,
        sheet_name="Customer_Best",
        index=False
    )

    channel_analysis.to_excel(
        writer,
        sheet_name="Channel_Analysis",
        index=False
    )

    monthly_analysis.to_excel(
        writer,
        sheet_name="Monthly_Analysis",
        index=False
    )

    transaction_type_analysis.to_excel(
        writer,
        sheet_name="Transaction_Type",
        index=False
    )

    loan_analysis.to_excel(
        writer,
        sheet_name="Loan_Analysis",
        index=False
    )

    complaint_analysis.to_excel(
        writer,
        sheet_name="Complaint_Analysis",
        index=False
    )

    customer_best.to_excel(
        writer,
        sheet_name="Customer_Best_2",
        index=False
    )

    segment_analysis.to_excel(
        writer,
        sheet_name="Segment_Analysis",
        index=False
    )

    customer_status.to_frame(
        name="customer_count"
    ).to_excel(
        writer,
        sheet_name="Customer_Status"
    )

    segment_count.to_excel(
        writer,
        sheet_name="Segment_Count"
    )

    city_analysis.to_excel(
        writer,
        sheet_name="City_Analysis",
        index=False
    )

    city_segment.to_excel(
        writer,
        sheet_name="City_Segment",
        index=False
    )

    signup_analysis.to_excel(
        writer,
        sheet_name="Signup_Analysis"
    )

    transaction_status_analysis.to_excel(
        writer,
        sheet_name="Transaction_Status",
        index=False
    )

    branch_analysis.to_excel(
        writer,
        sheet_name="Branch_Analysis",
        index=False
    )

    monthly_type_analysis.to_excel(
        writer,
        sheet_name="Monthly_Type",
        index=False
    )

    loan_status_analysis.to_excel(
        writer,
        sheet_name="Loan_Status",
        index=False
    )

    kpi_data = pd.DataFrame({
        "KPI": [
            "Total Transaction Value",
            "Average Transaction",
            "Total Deposits",
            "Total Withdrawals",
            "Default Rate"
        ],
        "Value": [
            total_transactions,
            average_transactions,
            total_deposits,
            total_withdrawals,
            default_rate
        ]
    })
   
    kpi_data.to_excel(
        writer,
        sheet_name="KPI",
        index=False
    )

print("Excel file successfully created: banking_analytics.xlsx")



















cursor.close()
connection.close()
