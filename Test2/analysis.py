# analyze sales data from csv file and calculate total sales, category-wise sales, top product and region-wise distribution

import pandas as pd
import io

# Sample data as a string (you can replace this with your actual CSV file path)
data = """OrderID,Date,Customer,Product,Category,Quantity,Price,Region
1001,2024-01-05,John Doe,Laptop,Electronics,1,800,North
1002,2024-01-06,Jane Smith,Mouse,Electronics,2,25,South
1003,2024-01-07,Alice Brown,Keyboard,Electronics,1,45,East
1004,2024-01-08,Bob White,Desk,Furniture,1,150,West
1005,2024-01-09,Chris Green,Chair,Furniture,2,85,North
1006,2024-01-10,Emma Stone,Monitor,Electronics,1,200,South
1007,2024-01-11,Liam Scott,Table,Furniture,1,120,East
1008,2024-01-12,Olivia King,Headphones,Electronics,3,60,West
1009,2024-01-13,Noah Lee,Laptop,Electronics,1,900,North
1010,2024-01-14,Sophia Hall,Chair,Furniture,1,95,South"""

# Read CSV data
df = pd.read_csv(io.StringIO(data))

# Task 1: Calculate total sales (Quantity × Price)
print("=" * 60)
print("TASK 1: TOTAL SALES CALCULATION")
print("=" * 60)

df['Sales'] = df['Quantity'] * df['Price']
print("\nDetailed Sales Breakdown:")
print(df[['OrderID', 'Customer', 'Product', 'Quantity', 'Price', 'Sales']])

total_sales = df['Sales'].sum()
print(f"\nTotal Sales: ${total_sales:,.2f}")

# Task 2: Find total sales by category
print("\n" + "=" * 60)
print("TASK 2: SALES BY CATEGORY")
print("=" * 60)

sales_by_category = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print("\n", sales_by_category)
print(f"\nCategory Summary:")
for category, sales in sales_by_category.items():
    percentage = (sales / total_sales) * 100
    print(f"  {category}: ${sales:,.2f} ({percentage:.1f}%)")

# Task 3: Identify the top-selling product
print("\n" + "=" * 60)
print("TASK 3: TOP-SELLING PRODUCT")
print("=" * 60)

sales_by_product = df.groupby('Product')['Sales'].sum().sort_values(ascending=False)
print("\n", sales_by_product)

top_product = sales_by_product.index[0]
top_sales = sales_by_product.values[0]
print(f"\nTop-Selling Product: {top_product}")
print(f"Total Sales: ${top_sales:,.2f}")

# Task 4: Find region-wise sales distribution
print("\n" + "=" * 60)
print("TASK 4: REGION-WISE SALES DISTRIBUTION")
print("=" * 60)

sales_by_region = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
print("\n", sales_by_region)
print(f"\nRegion Summary:")
for region, sales in sales_by_region.items():
    percentage = (sales / total_sales) * 100
    print(f"  {region}: ${sales:,.2f} ({percentage:.1f}%)")

# Task 5: Display orders where sales > $200
print("\n" + "=" * 60)
print("TASK 5: ORDERS WITH SALES > $200")
print("=" * 60)

high_sales_orders = df[df['Sales'] > 200][['OrderID', 'Customer', 'Product', 'Quantity', 'Price', 'Sales', 'Region']]
print("\n", high_sales_orders)
print(f"\nNumber of Orders with Sales > $200: {len(high_sales_orders)}")
print(f"Total Sales from High-Value Orders: ${high_sales_orders['Sales'].sum():,.2f}")

# Additional Summary Statistics
print("\n" + "=" * 60)
print("ADDITIONAL STATISTICS")
print("=" * 60)

print(f"\nTotal Number of Orders: {len(df)}")
print(f"Average Order Value: ${df['Sales'].mean():,.2f}")
print(f"Highest Order Value: ${df['Sales'].max():,.2f}")
print(f"Lowest Order Value: ${df['Sales'].min():,.2f}")
print(f"Total Units Sold: {df['Quantity'].sum()}")

# Optional: To use with actual CSV file, uncomment the line below and comment out the StringIO approach
# df = pd.read_csv('sales_data.csv')