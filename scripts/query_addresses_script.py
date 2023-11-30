import requests

def query_addresses(url, city, post_no, username, password):
    # Define the query parameters
    params = {'city': city, 'postNo': post_no}
    # Send a GET request with query parameters
    response = requests.get(url, params=params, auth=(username, password))
    return response.json(), response.status_code

if __name__ == '__main__':
    # Define the URL for querying addresses
    url = 'http://localhost:5000/addresses/query'
    # Prompt the user for query parameters
    city = input("Enter city to query: ")
    post_no = input("Enter post number to query: ")
    # Get user credentials for authentication
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    # Perform the query
    result, status_code = query_addresses(url, city, post_no, username, password)
    # Display the results
    print(f"Status Code: {status_code}\nQuery Result: {result}")
