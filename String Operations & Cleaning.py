import pandas as pd

customers = {
    "id": [101, 102, 103, 104, 105, 106],
    "name": [
        "  pavan ",
        "RAHUL",
        " SneHa ",
        "kiran",
        " ASHA ",
        " Vijay "
    ],
    "email": [
        " PAVAN@GMAIL.COM ",
        "rahul@YAHOO.COM",
        " Sneha@Outlook.COM ",
        "kiran@gmail.com ",
        " ASHA@GMAIL.COM",
        "vijay@Yahoo.COM "
    ],
    "city": [
        " hyderabad ",
        "DELHI",
        " Hyderabad",
        "mumbai ",
        " CHENNAI",
        "delhi "
    ]
}

df = pd.DataFrame(customers)

# Clean string columns
df["name"] = df["name"].str.strip().str.title()
df["email"] = df["email"].str.strip().str.lower()
df["city"] = df["city"].str.strip().str.title()

# Extract email provider
df["email_provider"] = (
    df["email"]
    .str.split("@")
    .str[1]
)

# Gmail customers
print("Gmail customers:")
print(df[df["email_provider"] == "gmail.com"])

# Yahoo customers
print("Yahoo customers:")
print(df[df["email_provider"] == "yahoo.com"])

# City distribution
print("City distribution:")
print(df["city"].value_counts())

# Invalid email providers
valid_providers = [
    "gmail.com",
    "yahoo.com",
    "outlook.com"
]

print("Customers with invalid email providers:")
print(
    df[
        ~df["email_provider"].isin(valid_providers)
    ]
)

# Final cleaned dataset
cleaned_df = df.copy()

print("Cleaned DataFrame:")
print(cleaned_df)
