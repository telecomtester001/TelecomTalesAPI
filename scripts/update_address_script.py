import requests
import json

def update_address(url, updated_data, username, password):
    #Sends a PUT request to update an address.
    response = requests.put(url, headers={'Content-Type': 'application/json'}, 
                            data=json.dumps(updated_data), auth=(username, password))
    return response.json(), response.status_code

def main():
    # Get address ID from the user
    address_id = input("Enter Address ID to update: ")
    url = f'http://localhost:5000/addresses/{address_id}'

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
    result, status_code = update_address(url, updated_data, username, password)

    # Display the result
    print(f"Status Code: {status_code}\nResponse: {result}")

if __name__ == '__main__':
    main()
