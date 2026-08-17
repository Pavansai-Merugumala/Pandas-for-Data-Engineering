df["revenue"] = df["quantity"] * df["price"]

df.groupby("region")["revenue"].sum()

df.groupby("region")["revenue"].mean()

df.groupby("product")["quantity"].sum()

df.groupby("customer")["order_id"].count()

customer_summary = df.groupby("customer").agg(
    order_count=("order_id", "count"),
    total_quantity=("quantity", "sum"),
    total_revenue=("revenue", "sum"),
    average_order_value=("revenue", "mean")
)

df.groupby(["region", "product"])["revenue"].sum()
