import requests

def get_all_addresses(url, username, password):
    response = requests.get(url, auth=(username, password))
    return response.json(), response.status_code

if __name__ == "__main__":
    url = 'http://localhost:5000/addresses'
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    result, status_code = get_all_addresses(url, username, password)
    print(f"Status Code: {status_code}\nAddresses: {result}")
