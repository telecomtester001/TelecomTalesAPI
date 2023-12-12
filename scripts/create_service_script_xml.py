import requests
import xmltodict
import xml.parsers.expat

def create_service_xml(url, service_data, username, password):
    """
    Send a POST request to create a new service using XML data.

    Args:
    - service_data: Dictionary containing service data.
    - username: Username for basic authentication.
    - password: Password for basic authentication.

    Returns:
    - Response from the server.
    """

    # Convert service data to XML
    xml_data = xmltodict.unparse({'service': service_data}, pretty=True)

    # Set the headers for XML
    headers = {'Content-Type': 'application/xml'}

    # Send the POST request with XML data
    response = requests.post(url, data=xml_data, headers=headers, auth=(username, password))

    # Check and return the response
    content_type = response.headers.get('Content-Type', '')
    if 'xml' in content_type:
        # Convert response to XML format
        try:
            response_xml = xmltodict.unparse(xmltodict.parse(response.text), pretty=True)
            return response_xml
        except xml.parsers.expat.ExpatError as e:
            return f"XML parsing error: {e}\nResponse: {response.text}"
    else:
        # Handle non-XML response
        return f"Non-XML response. Status Code: {response.status_code}, Response: {response.text}"

if __name__ == "__main__":
    # URL of the Flask app's endpoint for creating services
    url = 'http://localhost:5000/services'

    # Collect service data
    service_data = {
        'service': input("Enter service name: "),
        'value': input("Enter service value (True/False): ").strip().lower() in ['true', '1', 't'],
        'comment': input("Enter service comment: "),
        'address_id': int(input("Enter address ID: "))
    }

    # Collect authentication details
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Create the service using XML data
    response_xml = create_service_xml(url, service_data, username, password)

    # Print the XML response or error message
    print(response_xml)