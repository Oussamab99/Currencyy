
import requests

def get_exchange_rate(base_currency, target_currency, api_key):
    url = f"https://api.exchangeratesapi.io/latest?base={base_currency}&symbols={target_currency}&access_key={api_key}"
    response = requests.get(url)
    data = response.json()
    if 'error' in data:
        raise Exception(f"Error from API: {data['error']}")
    elif 'rates' in data and target_currency in data['rates']:
        return data['rates'][target_currency]
    else:
        raise Exception("Unexpected response from API")

def convert_currency(amount, base_currency, target_currency, api_key):
    exchange_rate = get_exchange_rate(base_currency, target_currency, api_key)
    converted_amount = amount * exchange_rate
    return converted_amount

# Example usage
def main():
    api_key = "YOUR_API_KEY"
    print("Welcome to the Currency Converter!")
    amount = float(input("Enter the amount you want to convert: "))
    base_currency = input("Enter your base currency: ")
    target_currency = input("Enter your target currency: ")
    resutl = convert_currency(amount, base_currency, target_currency, api_key)
    print(f"{amount} {base_currency} is equal to {resutl} {target_currency}")   

if __name__ == "__main__":
    main()