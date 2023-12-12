import requests
import json
import xmltodict

def parse_response(response, expected_format):
    if 'xml' in response.headers.get('Content-Type', ''):
        return xmltodict.parse(response.text)
    else:  # default to json
        return response.json()

def create_address(url, address_data, username, password, response_format='json'):
    headers = {'Content-Type': 'application/json', 'Accept': f'application/{response_format}'}
    response = requests.post(f"{url}/addresses", headers=headers, data=json.dumps(address_data), auth=(username, password))
    response_data = parse_response(response, response_format)
    address_id = response_data.get('address', {}).get('id')
    return address_id, response.status_code

def create_service(url, service_data, username, password, response_format='json'):
    headers = {'Content-Type': 'application/json', 'Accept': f'application/{response_format}'}
    response = requests.post(f"{url}/services", headers=headers, data=json.dumps(service_data), auth=(username, password))
    response_data = parse_response(response, response_format)
    service_id = response_data.get('service', {}).get('id')
    return service_id, response.status_code

def load_mock_data(url, file_path, username, password, response_format='json'):
    with open(file_path, 'r') as file:
        mock_data = json.load(file)

    for entry in mock_data:
        address_data = entry['address']
        address_data.pop('id', None)  # Ignore the 'id' from JSON

        address_id, address_code = create_address(url, address_data, username, password, response_format)
        if address_code != 201:
            print(f"Failed to create address. Status Code: {address_code}")
            continue

        for service in entry['services']:
            service['address_id'] = address_id  # Associate with the generated address ID
            service_res, service_code = create_service(url, service, username, password, response_format)
            if service_code != 201:
                print(f"Failed to create service. Status Code: {service_code}")

if __name__ == "__main__":
    url = 'http://localhost:5000'
    file_path = '../mock/json/mock1JSON.json'  # Update with the correct path to your JSON file if you've put another file that you want to load in ../mock/json/ folder 
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    load_mock_data(url, file_path, username, password)
