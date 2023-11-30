import requests

def link_service(url, address_id, service_id, username, password):
    # Send a POST request to link a service to an address
    response = requests.post(f"{url}/addresses/{address_id}/link_service/{service_id}", auth=(username, password))
    return response.json(), response.status_code

if __name__ == "__main__":
    # URL of the Flask app's endpoint for linking service to address
    url = 'http://localhost:5000'
    # User inputs the address and service IDs
    address_id = input("Enter Address ID: ")
    service_id = input("Enter Service ID: ")
    # User inputs their authentication details
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    # Link service to address
    result, status_code = link_service(url, address_id, service_id, username, password)
    # Display the result
    print(f"Status Code: {status_code}\nResponse: {result}")