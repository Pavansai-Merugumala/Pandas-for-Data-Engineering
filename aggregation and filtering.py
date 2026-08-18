import pandas as pd

sales = {
    "order_id": [101, 102, 103, 104, 105, 106, 107, 108],
    "customer": [
        "Pavan", "Rahul", "Pavan", "Sneha",
        "Rahul", "Pavan", "Sneha", "Kiran"
    ],
    "region": [
        "North", "South", "North", "South",
        "South", "North", "South", "North"
    ],
    "product": [
        "Laptop", "Phone", "Phone", "Laptop",
        "Laptop", "Phone", "Phone", "Laptop"
    ],
    "quantity": [2, 1, 3, 1, 2, 4, 2, 1],
    "price": [50000, 20000, 20000, 50000, 50000, 20000, 20000, 50000]
}

df = pd.DataFrame(sales)
df['revenue']=df['quantity']*df['price']
customer_summary=df.groupby('customer').agg(
    order_count=('order_id','count'),
    total_quantity=('quantity','sum'),
    total_revenue=('revenue','sum'),
    average_order_value=('revenue','mean')
).reset_index()
high_value_customers=customer_summary[customer_summary['total_revenue']>100000]
frequent_high_quantity_customers=customer_summary[(customer_summary['order_count']>=2)&(customer_summary['total_quantity']>=2)]
customer_summary.sort_values('total_revenue',ascending=False)
region_analysis=df.groupby('region').agg(
    order_count=('order_id','count'),
    total_quantity=('quantity','sum'),
    total_revenue=('revenue','sum'),
    average_order_value=('revenue','mean')
)
high_revenue_regions=region_analysis[region_analysis['total_revenue']>20000]
"""task 8 answer:first one is filtering the rows and second one 
is filtering the aggreagated row"""
