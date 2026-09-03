import pandas as pd

customers = pd.DataFrame({
    "customer_id": [1, 2, 3, 4, 5],
    "name": ["Pavan", "Rahul", "Sneha", "Kiran", "Asha"],
    "city": ["Hyderabad", "Delhi", "Bengaluru", "Chennai", "Mumbai"]
})

orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104, 105, 106],
    "customer_id": [1, 2, 1, 3, 6, 2],
    "product_id": [201, 202, 203, 201, 202, 204],
    "quantity": [2, 1, 3, 1, 2, 4]
})

products = pd.DataFrame({
    "product_id": [201, 202, 203, 204],
    "product_name": ["Laptop", "Phone", "Keyboard", "Monitor"],
    "price": [50000, 20000, 3000, 25000]
})
inner_df=customers.merge(
    orders, 
    on='customer_id',
)
#customer id 4,5 and 6 are disappeared, as the merge acts as a inner join
left_df=customers.merge(
    orders,
    on='customer_id',
    how='left'
)
reconciliation_df=customers.merge(
    orders,
    on='customer_id',
    how='outer',
    indicator=True
)
print(reconciliation_df)
customers_without_orders=reconciliation_df[reconciliation_df['_merge']=='left_only'].copy()

orders_without_customers=reconciliation_df[reconciliation_df['_merge']=="right_only"].copy()
valid_customer_orders=reconciliation_df[(reconciliation_df['_merge']!='left_only')&(reconciliation_df['_merge']!='right_only')]
valid_customer_orders=valid_customer_orders.drop(columns='_merge')
print(valid_customer_orders)
final_orders=valid_customer_orders.merge(
    products,
    on='product_id'
)
final_orders['revenue']=final_orders['quantity']*final_orders['price']
orders.merge(
    products,
    on='product_id',
    validate='many_to_one'
)
print()
#many to one is apprpriate as orders table can contian multiple same customerids as a single customer can make multiple orders
#task 6: validate can catch when customer id in customer table have any duplicates
