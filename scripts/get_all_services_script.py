import requests

def get_all_services(url, username, password):
    response = requests.get(url, auth=(username, password))
    return response.json(), response.status_code

if __name__ == "__main__":
    url = 'http://localhost:5000/services'
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    result, status_code = get_all_services(url, username, password)
    print(f"Status Code: {status_code}\nServices: {result}")
