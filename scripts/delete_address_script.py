import requests

def delete_address(url, address_id, username, password):
    # Send the DELETE request to the API
    response = requests.delete(f"{url}/{address_id}", auth=(username, password))

    # Return the status code
    return response.status_code

if __name__ == "__main__":
    # URL of the Flask app's endpoint for deleting addresses
    url = 'http://localhost:5000/addresses'

    # Prompt the user for the address ID
    address_id = input("Enter Address ID to delete: ")
    
    # Prompt the user for the username and password inputs
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Delete the address by sending a DELETE request to the API
    status_code = delete_address(url, address_id, username, password)

    # Print the status code
    if status_code == 204:
        print("Address Deleted Successfully")
    else:
        print(f"Error: Status Code {status_code}")
