import pandas as pd

df = pd.DataFrame(employees)

# 1. Inspect dtypes
print(df.dtypes)

# 2. Convert ID to nullable integer
df["id"] = pd.to_numeric(df["id"], errors="coerce").astype("Int64")

# 3. Clean salary
df["salary"] = df["salary"].str.replace(",", "", regex=False)
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

# 4. Salary validation
valid_salary = df[
    (df["salary"] > 0) &
    df["salary"].notna()
]

invalid_salary = df[
    (df["salary"] <= 0) |
    df["salary"].isna()
]

# 5. Convert experience
df["experience"] = pd.to_numeric(
    df["experience"],
    errors="coerce"
)

# 6. Convert quantity
df["quantity"] = pd.to_numeric(
    df["quantity"],
    errors="coerce"
)

# Optional business validation:
# negative quantity is converted to NaN
df["quantity"] = df["quantity"].mask(df["quantity"] < 0)

# 7. Convert price
df["price"] = pd.to_numeric(
    df["price"],
    errors="coerce"
)

# 8. Total amount
df["total_amount"] = df["quantity"] * df["price"]

# 9. Valid transactions
valid_transactions = df[
    (df["quantity"] > 0) &
    (df["price"] > 0)
]

# 10. Invalid transactions
invalid_transactions = df[
    (df["quantity"] <= 0) |
    (df["price"] <= 0) |
    df["quantity"].isna() |
    df["price"].isna()
]

# 11. Fully cleaned dataset
cleaned_df = df[
    (df["salary"] > 0) &
    (df["experience"] > 0) &
    (df["quantity"] > 0) &
    (df["price"] > 0)
].copy()

# 12. Total amount for valid records
cleaned_df["total_amount"] = (
    cleaned_df["quantity"] * cleaned_df["price"]
)

# 13. Sort
cleaned_df = cleaned_df.sort_values(
    "total_amount",
    ascending=False
)

# 14. Final output
print(
    cleaned_df[
        [
            "id",
            "name",
            "salary",
            "experience",
            "quantity",
            "price",
            "total_amount"
        ]
    ]
)
