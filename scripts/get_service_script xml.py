import requests

def get_service_by_id_xml(url, service_id, username, password):
    # Set headers to request XML response
    headers = {'Accept': 'application/xml'}
    
    # Send a GET request to retrieve the service by ID with XML response
    response = requests.get(f"{url}/{service_id}", headers=headers, auth=(username, password))
    return response.text, response.status_code

if __name__ == "__main__":
    # URL of the Flask app's service retrieval endpoint
    url = 'http://localhost:5000/services'
    
    # User inputs the service ID
    service_id = input("Enter Service ID: ")
    
    # User inputs their authentication details
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    # Get service details by ID in XML format
    result, status_code = get_service_by_id_xml(url, service_id, username, password)
    
    # Display the result
    print(f"Status Code: {status_code}\nResponse (XML): {result}")
