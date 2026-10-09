"""CodeAlpha Task 2: Stock Portfolio Tracker"""

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 125,
}


def main():
    print("=== STOCK PORTFOLIO TRACKER ===")
    print("Available stocks and prices:")
    for name, price in STOCK_PRICES.items():
        print(f"  {name}: ${price}")
    print("\nType 'done' as the stock name when finished.\n")

    portfolio = []  # list of (stock, quantity, value)
    total = 0

    while True:
        stock = input("Stock name: ").strip().upper()
        if stock == "DONE":
            break
        if stock not in STOCK_PRICES:
            print("Stock not found. Please choose from the list above.\n")
            continue

        try:
            quantity = int(input("Quantity: "))
            if quantity <= 0:
                raise ValueError
        except ValueError:
            print("Please enter a positive whole number.\n")
            continue

        value = STOCK_PRICES[stock] * quantity
        portfolio.append((stock, quantity, value))
        total += value
        print(f"Added {quantity} x {stock} = ${value}\n")

    if not portfolio:
        print("No stocks entered.")
        return

    print("\n--- Portfolio Summary ---")
    for stock, quantity, value in portfolio:
        print(f"{stock:<6} x {quantity:<5} = ${value}")
    print(f"Total investment: ${total}")

    save = input("\nSave result to file? (y/n): ").strip().lower()
    if save == "y":
        with open("portfolio.txt", "w") as f:
            f.write("Stock Portfolio Summary\n")
            for stock, quantity, value in portfolio:
                f.write(f"{stock} x {quantity} = ${value}\n")
            f.write(f"Total investment: ${total}\n")
        print("Saved to portfolio.txt")


if __name__ == "__main__":
    main()
