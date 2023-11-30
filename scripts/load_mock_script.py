import requests
import json

def create_address(url, address_data, username, password):
    response = requests.post(url + '/addresses', 
                             headers={'Content-Type': 'application/json'}, 
                             data=json.dumps(address_data), 
                             auth=(username, password))
    return response.json(), response.status_code

def create_service(url, service_data, username, password):
    response = requests.post(url + '/services', 
                             headers={'Content-Type': 'application/json'}, 
                             data=json.dumps(service_data), 
                             auth=(username, password))
    return response.json(), response.status_code

def load_mock_data(url, file_path, username, password):
    with open(file_path, 'r') as file:
        mock_data = json.load(file)

    for entry in mock_data:
        address_data = entry['address']
        # Removing 'id' key if present in address_data
        address_data.pop('id', None)

        address_res, address_code = create_address(url, address_data, username, password)
        if address_code != 201:
            print(f"Failed to create address: {address_res}")
            continue

        # Extract the address ID from the created address
        address_id = address_res['id']

        for service in entry['services']:
            # Add address_id to the service data
            service['address_id'] = address_id
            service_res, service_code = create_service(url, service, username, password)
            if service_code != 201:
                print(f"Failed to create service: {service_res}")

if __name__ == "__main__":
    url = 'http://localhost:5000'
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    file_path = '../mock/json/mock1JSON.json'
    load_mock_data(url, file_path, username, password)



