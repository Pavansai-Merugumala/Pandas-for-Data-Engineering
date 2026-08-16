import pandas as pd

employees = {
    "id": [101, 102, 103, 104, 105, 106, 107, 108],
    "name": [
        "Pavan", "Rahul", "Sneha", "Kiran",
        "Asha", "Vijay", "Anjali", "Ravi"
    ],
    "department": [
        "Data Engineering",
        "Analytics",
        "HR",
        "Engineering",
        "Finance",
        "Analytics",
        "Data Engineering",
        "Engineering"
    ],
    "salary": [
        65000, 52000, 47000, 60000,
        48000, 55000, 72000, 43000
    ],
    "city": [
        "Hyderabad",
        "Delhi",
        "Chennai",
        "Bangalore",
        "Mumbai",
        "Delhi",
        "Hyderabad",
        "Bangalore"
    ],
    "experience": [3, 2, 1, 4, 2, 3, 5, 1]
}

df = pd.DataFrame(employees)

# 1. Salary ascending
print(df.sort_values("salary"))

# 2. Salary descending
print(df.sort_values("salary", ascending=False))

# 3. Top 3 highest-paid employees
print(
    df.nlargest(3, "salary")[["name", "department", "salary"]]
)

# 4. Two lowest-paid employees
print(
    df.nsmallest(2, "salary")[["name", "department", "salary"]]
)

# 5. Department ascending, salary descending
print(
    df.sort_values(
        ["department", "salary"],
        ascending=[True, False]
    )
)

# 6. Salary rank
df["salary_rank"] = (
    df["salary"]
    .rank(ascending=False)
    .astype(int)
)

# 7. Combined ETL challenge
new_df = df.loc[
    (df["salary"] >= 50000) &
    (df["experience"] >= 2)
].copy()

new_df = new_df.sort_values(
    "salary",
    ascending=False
)

new_df["salary_rank"] = (
    new_df["salary"]
    .rank(ascending=False)
    .astype(int)
)

print(
    new_df[
        ["name", "department", "salary",
         "experience", "salary_rank"]
    ]
)
