# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

for product_name, details in products.items():
        price, quantity_sold = details
        price = float(price)
        quantity_sold = int(quantity_sold)
        total_sales = price*quantity_sold
        total_sales_list.append(total_sales)
        print(f"Total sales for {product_name}: ${total_sales}")

# print(total_sales_list)
total_sum = sum(total_sales_list)
print(f"Total sum of all sales: ${total_sum}")
min_sales = min(total_sales_list)
print(f"Minimum sales: ${min_sales}")
max_sales = max(total_sales_list)
print(f"Maximum sales: ${max_sales}")






