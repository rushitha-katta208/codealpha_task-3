# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 125,
    "MSFT": 310
}

# Dictionary to store user stock and quantity
user_portfolio = {}

# User input
print("Enter stock names and quantities. Type 'done' to finish.")
while True:
    stock = input("Stock name: ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not in database. Try again.")
        continue
    try:
        quantity = int(input(f"Quantity of {stock}: "))
        user_portfolio[stock] = user_portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid number.")

# Calculate total investment
total_investment = 0
print("\nYour Portfolio:")
for stock, quantity in user_portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_investment += value
    print(f"{stock}: {quantity} shares × ${price} = ${value}")

print(f"\nTotal Investment Value: ${total_investment}")

# Save to file option
save = input("\nDo you want to save this to a file? (yes/no): ").lower()
if save == 'yes':
    file_type = input("Choose file type - txt or csv: ").lower()
    if file_type == 'txt':
        with open("investment_report.txt", "w") as f:
            for stock, quantity in user_portfolio.items():
                f.write(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${stock_prices[stock]*quantity}\n")
            f.write(f"\nTotal Investment Value: ${total_investment}")
        print("Saved to investment_report.txt")
    elif file_type == 'csv':
        with open("investment_report.csv", "w") as f:
            f.write("Stock,Quantity,Price,Value\n")
            for stock, quantity in user_portfolio.items():
                price = stock_prices[stock]
                value = price * quantity
                f.write(f"{stock},{quantity},{price},{value}\n")
            f.write(f"Total,,,{total_investment}")
        print("Saved to investment_report.csv")
    else:
        print("Invalid file type. Not saved.")
