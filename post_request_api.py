import requests

url = 'http://localhost:5000/api/protected'
headers = {'Authorization': 'my_secret_token'}
data = {'key': 'value'} # Add any data that you want to send with the request
response = requests.post(url, headers=headers, data=data)

if response.status_code == 200:
    print(response.json()['message']) # Output: Welcome to the protected endpoint!
else:
    print(response.json()['message']) # Output: Invalid token
