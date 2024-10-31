import json
import urllib.parse
import requests

def read_large_json(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield json.loads(line)

# Set your username and password
username = 'default_user_IlR2D-NZ6d5U0tWa34m'
password = '9ZH8eHWc3bmpCxrbboHArn3qiUP1VieK'

# Set the base URL for your API
base_url = 'http://localhost:15672/api'

for item in read_large_json('all-connections-2.json'):
    # Encode the name for use in the URL
    encoded_name = urllib.parse.quote(item[0]['name'], safe='')
    
    # Construct the full URL
    url = f"{base_url}/connections/{encoded_name}"
    
    # Send a DELETE request with authentication
    response = requests.delete(url, auth=(username, password))
    
    # Check the response
    if response.status_code == 204:
        print(f"Successfully deleted connection: {item[0]['name']}")
    else:
        print(f"Failed to delete connection: {item[0]['name']}. Status code: {response.status_code}")
