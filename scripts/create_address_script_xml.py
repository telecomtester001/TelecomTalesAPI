import requests
import xmltodict

def add_address_xml(base_url, address_data, username, password):
    """
    Send a POST request to add a new address with XML data.

    Args:
    - base_url: Base URL of the Flask application.
    - address_data: Dictionary containing address information.
    - username: Username for basic authentication.
    - password: Password for basic authentication.

    Returns:
    - Processed response from the server.
    """
    # Construct the full URL for the address route
    url = f"{base_url}/addresses/"

    # Convert the address data to XML format
    xml_data = xmltodict.unparse({"address": address_data})

    # Set headers for XML
    headers = {'Content-Type': 'application/xml'}

    # Send the POST request with XML data and basic authentication
    response = requests.post(url, data=xml_data, headers=headers, auth=(username, password))
    
    

    # Process the response based on its content type
    if response.headers.get('Content-Type') == 'application/xml':
        try:
            # Parse the XML response
            response_data = xmltodict.parse(response.text)
            return f"XML Response: {response_data}"
        except Exception as e:
            return f"Failed to parse XML: {e}"
    else:
        return f"Response: {response.text}"

if __name__ == "__main__":
    # Base URL of your Flask application
    BASE_URL = "http://localhost:5000"  # Update with your actual base URL

    # Collect address details from the user
    streetNo = input("Enter Street Number: ")
    street = input("Enter Street Name: ")
    city = input("Enter City: ")
    post = input("Enter Post: ")
    postNo = int(input("Enter Post Number: "))

    # Collect authentication details
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Construct the address data dictionary
    address_data = {
        "streetNo": streetNo,
        "street": street,
        "city": city,
        "post": post,
        "postNo": postNo
    }

    # Send the request to add the address with XML data
    response = add_address_xml(BASE_URL, address_data, username, password)

    # Print the processed response
    print(response)