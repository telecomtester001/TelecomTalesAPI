import requests
import json

def update_service(url, service_id, updated_data, username, password):
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f"{url}/{service_id}", headers=headers, data=json.dumps(updated_data), auth=(username, password))
    return response.json(), response.status_code

if __name__ == "__main__":
    url = 'http://localhost:5000/services'
    service_id = input("Enter Service ID to update: ")

    print("Enter updated service details:")
    updated_data = {
        'service': input("Service Name: "),
        'value': bool(input("Value (True/False): ")),
        'comment': input("Comment: ")
    }

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    result, status_code = update_service(url, service_id, updated_data, username, password)
    print(f"Status Code: {status_code}\nResponse: {result}")
