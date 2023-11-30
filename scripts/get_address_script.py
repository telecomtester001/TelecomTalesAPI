import requests

def get_address(url, address_id, username, password):
    # Send a GET request to retrieve address details
    response = requests.get(f"{url}/{address_id}", auth=(username, password))
    return response.json(), response.status_code

if __name__ == "__main__":
    # URL of the Flask app's address retrieval endpoint
    url = 'http://localhost:5000/addresses'
    # User inputs the address ID
    address_id = input("Enter Address ID: ")
    # User inputs their authentication details
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    # Get address details
    result, status_code = get_address(url, address_id, username, password)
    # Display the result
    print(f"Status Code: {status_code}\nResponse: {result}")
