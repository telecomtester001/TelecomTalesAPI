import requests

def get_service(url, service_id, username, password):
    # Send a GET request to retrieve service details
    response = requests.get(f"{url}/{service_id}", auth=(username, password))
    return response.json(), response.status_code

if __name__ == "__main__":
    # URL of the Flask app's service retrieval endpoint
    url = 'http://localhost:5000/services'
    # User inputs the service ID
    service_id = input("Enter Service ID: ")
    # User inputs their authentication details
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    # Get service details
    result, status_code = get_service(url, service_id, username, password)
    # Display the result
    print(f"Status Code: {status_code}\nResponse: {result}")
