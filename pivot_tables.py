import pandas as pd

sales = pd.DataFrame({
    "order_id": [
        101, 102, 103, 104,
        105, 106, 107, 108,
        109, 110
    ],

    "customer": [
        "Pavan", "Rahul", "Pavan", "Sneha",
        "Rahul", "Pavan", "Sneha", "Kiran",
        "Asha", "Vijay"
    ],

    "region": [
        "North", "South", "North", "South",
        "South", "North", "South", "North",
        "East", "East"
    ],

    "product": [
        "Laptop", "Phone", "Phone", "Laptop",
        "Laptop", "Phone", "Phone", "Laptop",
        "Phone", "Laptop"
    ],

    "quantity": [
        2, 1, 3, 1,
        2, 4, 2, 1,
        5, 3
    ],

    "price": [
        50000, 20000, 20000, 50000,
        50000, 20000, 20000, 50000,
        20000, 50000
    ]
})

# Calculate revenue
sales["revenue"] = sales["quantity"] * sales["price"]


# ==========================================
# TASK 1: Total Revenue by Region
# ==========================================

total_revenue_region = pd.pivot_table(
    sales,
    index="region",
    values="revenue",
    aggfunc="sum"
)

print("\nTotal Revenue by Region:")
print(total_revenue_region)


# ==========================================
# TASK 2: Total Revenue by Region and Product
# ==========================================

total_revenue_region_product = pd.pivot_table(
    sales,
    index="region",
    columns="product",
    values="revenue",
    aggfunc="sum",
    fill_value=0
)

print("\nTotal Revenue by Region and Product:")
print(total_revenue_region_product)


# ==========================================
# TASK 3: Total Quantity and Revenue by Region
# ==========================================

total_quantity_total_revenue_by_region = pd.pivot_table(
    sales,
    index="region",
    values=["quantity", "revenue"],
    aggfunc="sum",
    fill_value=0
)

print("\nTotal Quantity and Total Revenue by Region:")
print(total_quantity_total_revenue_by_region)


# ==========================================
# TASK 4: Revenue Summary by Region
# ==========================================

revenue_summary_region = pd.pivot_table(
    sales,
    index="region",
    values="revenue",
    aggfunc=["sum", "mean", "count"]
)

print("\nRevenue Summary by Region:")
print(revenue_summary_region)


# ==========================================
# TASK 5: Region × Product Report with Totals
# ==========================================

region_product_report = pd.pivot_table(
    sales,
    index="region",
    columns="product",
    values="revenue",
    aggfunc="sum",
    fill_value=0,
    margins=True
)

print("\nRegion × Product Revenue Report:")
print(region_product_report)


# ==========================================
# TASK 6: Quantity by Region and Product
# ==========================================

quantity_region_product = pd.pivot_table(
    sales,
    index="region",
    columns="product",
    values="quantity",
    aggfunc="sum",
    fill_value=0
)

print("\nQuantity by Region and Product:")
print(quantity_region_product)
