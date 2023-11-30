import requests
import json

def create_service(url, service_data, username, password):
    # Send the POST request to the API
    response = requests.post(url, json=service_data, auth=(username, password))

    # Return the JSON response and status code
    return response.json(), response.status_code

if __name__ == "__main__":
    # URL of the Flask app's endpoint for creating services
    url = 'http://localhost:5000/services'

    # Prompt for service data input
    print("Enter service details:")
    service_data = {
        'service': input("Service Name: "),
        'value': input("Value (True/False): ").lower() == 'true',
        'comment': input("Comment: ")
    }

    # Prompt the user for the username and password inputs
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Create the service by sending a POST request to the API
    result, status_code = create_service(url, service_data, username, password)

    # Print the response and status code
    print(f"Status Code: {status_code}\nResponse: {result}")
