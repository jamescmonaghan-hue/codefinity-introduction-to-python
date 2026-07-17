prices = [29.99, 45.50, 12.75, 38.20]
discounts = [0.1, 0.2, 0.15, 0.05]
updated_price = []

for i in range(len(prices)):
    prices[i]-= prices[i]*discounts[i]
    updated_price = prices[i]
    print(f"Updated price for item {i}: ${updated_price:.2f}")