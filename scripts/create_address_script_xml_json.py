import requests
import json
import xmltodict

def create_address(url, address_data, username, password, data_format='json'):
    headers = {'Content-Type': 'application/json'} if data_format == 'json' else {'Content-Type': 'application/xml'}
    data = json.dumps(address_data) if data_format == 'json' else xmltodict.unparse({'address': address_data}, pretty=True)

    print("Sending Data:", data)  # For debugging

    # Send the POST request to the API with basic auth and appropriate headers
    response = requests.post(url, data=data, auth=(username, password), headers=headers)

    # Handle cases where the response is not in the expected format
    try:
        if data_format == 'json':
            return response.json(), response.status_code
        else:  # Handle XML
            return xmltodict.parse(response.content), response.status_code
    except (json.JSONDecodeError, xmltodict.expat.ExpatError):
        return "No valid response in the expected format", response.status_code

if __name__ == "__main__":
    url = 'http://localhost:5000/addresses/'

    # Prompt for the format
    data_format = input("Enter the data format (json/xml): ").lower()

    # Prompt for address data input
    print("Creating a new address...")
    address_data = {
        'streetNo': input("Enter Street Number: "),
        'street': input("Enter Street Name: "),
        'city': input("Enter City: "),
        'post': input("Enter Post: "),
        'postNo': int(input("Enter Post Number: "))  
    }

    # Prompt the user for the username and password inputs
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Create the address by sending a POST request to the API
    result, status_code = create_address(url, address_data, username, password, data_format)

    # Print the response and status code
    print(f"Status Code: {status_code}\nResponse: {result}")
