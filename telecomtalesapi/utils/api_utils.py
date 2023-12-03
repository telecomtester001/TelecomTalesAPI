from flask import request
import xmltodict


# Helper function to check if request is XML
def is_request_xml():
    # Check the Content-Type of the request to see if it contains 'xml'
    return 'xml' in request.headers.get('Content-Type', '').lower()

# Helper function to check if response should be XML
def should_return_xml():
    # Check the Accept header of the request to determine if the response should be in XML
    return 'xml' in request.headers.get('Accept', '').lower()

# Helper function to convert data to XML
def to_xml(data):
    # Convert the given data dictionary into XML format
    return xmltodict.unparse({'response': data})