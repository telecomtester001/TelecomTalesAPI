import requests

def delete_service(url, service_id, username, password):
    # Send the DELETE request to the API
    response = requests.delete(f"{url}/{service_id}", auth=(username, password))

    # Return the status code
    return response.status_code

if __name__ == "__main__":
    # URL of the Flask app's endpoint for deleting services
    url = 'http://localhost:5000/services'

    # Prompt the user for the service ID
    service_id = input("Enter Service ID to delete: ")
    
    # Prompt the user for the username and password inputs
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Delete the service by sending a DELETE request to the API
    status_code = delete_service(url, service_id, username, password)

    # Print the status code
    if status_code == 204:
        print("Service Deleted Successfully")
    else:
        print(f"Error: Status Code {status_code}")
