import requests
import json

def create_address(url, address_data, username, password):
    # Send the POST request to the API with basic auth
    response = requests.post(url, json=address_data, auth=(username, password))

    # Handle cases where the response might not be JSON
    try:
        return response.json(), response.status_code
    except json.JSONDecodeError:
        return "No JSON in response", response.status_code

if __name__ == "__main__":
    # Updated URL for the Flask app's endpoint for creating addresses
    url = 'http://localhost:5000/addresses/'

    # Prompt for address data input
    print("Creating a new address...")
    address_data = {
        'streetNo': input("Enter Street Number: "),
        'street': input("Enter Street Name: "),
        'city': input("Enter City: "),
        'post': input("Enter Post: "),
        'postNo': input("Enter Post Number: ")
    }

    # Prompt the user for the username and password inputs
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Create the address by sending a POST request to the API
    result, status_code = create_address(url, address_data, username, password)

    # Print the response and status code
    print(f"Status Code: {status_code}\nResponse: {result}")
