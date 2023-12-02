import requests

def query_services_json(base_url, address_id, username, password):
    """Query services linked to a specific address in JSON format."""
    url = f"{base_url}/addresses/{address_id}/services"
    response = requests.get(url, auth=(username, password))

    # Check if the response is successful
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}, {response.text}"

if __name__ == '__main__':
    BASE_URL = "http://localhost:5000"
    address_id = input("Enter address ID to query services: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    services = query_services_json(BASE_URL, address_id, username, password)
    print("Services linked to the address:", services)
