import requests
import json

def update_address(url, address_id, updated_data, username, password):
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f"{url}/{address_id}", headers=headers, data=json.dumps(updated_data), auth=(username, password))
    try:
        return response.json(), response.status_code
    except json.JSONDecodeError:
        return response.text, response.status_code

if __name__ == "__main__":
     # Get address ID from the user
    url = 'http://localhost:5000/addresses/'
    address_id = input("Enter Address ID to update: ")
    
    # Collect updated data from the user
    updated_data = {
        'streetNo': input("Enter updated Street Number: "),
        'street': input("Enter updated Street Name: "),
        'city': input("Enter updated City: "),
        'post': input("Enter updated Post: "),
        'postNo': input("Enter updated Post Number: ")
    }

    # Get user credentials for authentication
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Send the update request
    result, status_code = update_address(url, address_id, updated_data, username, password)
    # Display the result
    print(f"Status Code: {status_code}\nResponse: {result}")
