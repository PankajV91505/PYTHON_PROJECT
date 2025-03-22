from forex_python.converter import CurrencyRates

def currency_converter():
    c = CurrencyRates()
    
    try:
        from_currency = input("Enter base currency (e.g., USD): ").upper()
        to_currency = input("Enter target currency (e.g., EUR): ").upper()
        amount = float(input("Enter amount: "))

        converted_amount = c.convert(from_currency, to_currency, amount)
        print(f"\n{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    currency_converter()
