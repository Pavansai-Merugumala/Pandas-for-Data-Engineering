import pandas as pd

employees = {
    "id": [101, 102, 103, 104, 105, 106, 107, 108],
    "name": [
        "Pavan",
        "Rahul",
        None,
        "Kiran",
        "Asha",
        "Vijay",
        None,
        "Ravi"
    ],
    "department": [
        "Data Engineering",
        "Analytics",
        "HR",
        None,
        "Finance",
        "Analytics",
        "Data Engineering",
        "Engineering"
    ],
    "salary": [
        65000,
        None,
        47000,
        60000,
        None,
        55000,
        72000,
        43000
    ],
    "city": [
        "Hyderabad",
        "Delhi",
        None,
        "Bangalore",
        "Mumbai",
        None,
        "Hyderabad",
        "Bangalore"
    ],
    "experience": [
        3,
        2,
        None,
        4,
        2,
        3,
        5,
        None
    ]
}

df = pd.DataFrame(employees)

# 1. Missing values
print("Missing values:")
print(df.isna())

# 2. Missing values per column
print("\nMissing values per column:")
print(df.isna().sum())

# 3. Total missing values
print("\nTotal missing values:")
print(df.isna().sum().sum())

# 4. Missing percentage
print("\nMissing percentage:")
print(df.isna().mean() * 100)

# 5. Employees having at least one missing value
print("\nEmployees with at least one missing value:")
print(df[df.isna().any(axis=1)])

# 6. Employees whose salary is missing
print("\nEmployees with missing salary:")
print(df[df["salary"].isna()])

# 7. Valid salary records
valid_salary_df = df[df["salary"].notna()].copy()

# 8. Create cleaned DataFrame
cleaned_employees = df.dropna(
    subset=["id", "name", "salary"]
).copy()

# 9. Fill optional fields
cleaned_employees["department"] = (
    cleaned_employees["department"]
    .fillna("Unknown")
)

cleaned_employees["city"] = (
    cleaned_employees["city"]
    .fillna("Unknown")
)

cleaned_employees["experience"] = (
    cleaned_employees["experience"]
    .fillna(cleaned_employees["experience"].median())
)

# 10. Sort by salary
cleaned_employees = cleaned_employees.sort_values(
    "salary",
    ascending=False
)

# 11. Final output
print("\nCleaned Employees:")
print(
    cleaned_employees[
        ["id", "name", "department",
         "salary", "city", "experience"]
    ]
)
