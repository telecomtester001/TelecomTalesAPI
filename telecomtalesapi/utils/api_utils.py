import json
import xmltodict
import logging

from flask import request
from flask import make_response

from xmltodict import unparse


# Define common XML MIME types
XML_MIME_TYPES = ['application/xml', 'text/xml']

# Helper function to check if request is XML
def is_request_xml():
    content_type = request.headers.get('Content-Type', '').lower()
    return any(mime in content_type for mime in XML_MIME_TYPES)

# Helper function to check if response should be XML
def should_return_xml():
    accept = request.headers.get('Accept', '').lower()
    return any(mime in accept for mime in XML_MIME_TYPES)

# Helper function to convert data to XML
def to_xml(data, root_element='response'):
    try:
        return xmltodict.unparse({root_element: data})
    except Exception as e:
        logging.error(f"Error converting data to XML: {e}")
        raise

# Helper function to make a Flask response with a JSON encoded body
def output_json(data, code, headers=None):
    resp_body = json.dumps(data)
    resp = make_response(resp_body, code)
    resp.headers['Content-Type'] = 'application/json'
    if headers:
        resp.headers.extend(headers)
    return resp

# Helper function to make a Flask response with an XML encoded body
def output_xml(data, code, headers=None):
    resp_body = unparse({'response': data}) 
    resp = make_response(resp_body, code)
    resp.headers['Content-Type'] = 'application/xml'
    if headers:
        resp.headers.extend(headers)
    return resp