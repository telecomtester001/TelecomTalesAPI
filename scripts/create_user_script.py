import requests
import json

def create_user(url, username, password):
    # Prepare the data for the POST request
    data = {
        'username': username,
        'password': password
    }
    # Send the POST request to the API
    response = requests.post(url, json=data)

    # Handle cases where the response might not be JSON
    try:
        return response.json(), response.status_code
    except json.JSONDecodeError:
        return "No JSON in response", response.status_code

if __name__ == "__main__":
    # URL of the Flask app's endpoint for creating users
    url = 'http://localhost:5000/users/'

    # Prompt the user for the username and password inputs
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Create the user by sending a POST request to the API
    result, status_code = create_user(url, username, password)

    # Print the response and status code
    print(f"Status Code: {status_code}\nResponse: {result}")
