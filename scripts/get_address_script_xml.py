import requests

def get_address_by_id_xml(url, address_id, username, password):
    # Set headers to request XML response
    headers = {'Accept': 'application/xml'}
    
    # Send a GET request to retrieve the address by ID with XML response
    response = requests.get(f"{url}/{address_id}", headers=headers, auth=(username, password))
    return response.text, response.status_code

if __name__ == "__main__":
    # URL of the Flask app's address retrieval endpoint
    url = 'http://localhost:5000/addresses'
    
    # User inputs the address ID
    address_id = input("Enter Address ID: ")
    
    # User inputs their authentication details
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    # Get address details by ID in XML format
    result, status_code = get_address_by_id_xml(url, address_id, username, password)
    
    # Display the result
    print(f"Status Code: {status_code}\nResponse (XML): {result}")