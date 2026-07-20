# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

# 1. Define calculate_revenue(prices, quantities_sold)
def calculate_revenue(prices, quantities_sold):
    revenue = []
    for price, quantity in list(zip(prices, quantities_sold)):
        revenue.append(price * quantity)
    return revenue


revenue = calculate_revenue(prices, quantities_sold)

revenue_per_product = list(zip(products, revenue))

def formatted_output(revenues):
    sorted_revenue = sorted(revenues)
    for product, revenue in sorted_revenue:
        print(f"{product} has total revenue of ${revenue}")

formatted_output(revenue_per_product)

# Example of expected output line (do not remove):
# print(f"{revenue[0]} has total revenue of ${revenue[1]}")