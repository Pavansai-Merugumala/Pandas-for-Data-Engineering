import pandas as pd
import numpy as np

employees = {
    "name": [
        "Pavan", "Rahul", "Sneha",
        "Kiran", "Asha", "Vijay"
    ],
    "department": [
        "IT", "HR", "IT",
        "Finance", "HR", "IT"
    ],
    "salary": [
        65000, 52000, 48000,
        75000, 58000, 70000
    ],
    "experience": [
        3, 2, 1, 5, 4, 6
    ]
}

df = pd.DataFrame(employees)
df['salary_category']=df['salary'].apply(
    lambda x:"High" if x>=70000 else("Medium" if x>=55000 else 'Low')
)
df['experience_level']=df['experience'].apply(
    lambda x: "Senior" if x>=5 else("Mid" if x>=3 else "Junior")
)
df["employee_type"] = df.apply(
    lambda row:
        "High Value"
        if (row["salary"] >= 70000) and (row["experience"] >= 5)
        else "Regular",
    axis=1
)
conditions=[
    df['salary']>=70000,df['salary']>=55000,
]
choices=['High',"Medium"]
df['salary_band']=np.select(conditions,choices,default="Low")
print(df)

