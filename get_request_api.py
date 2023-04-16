import requests

url = 'http://localhost:5000/api/protected'
headers = {'Authorization': 'my_secret_token'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print(response.json()['message']) # Output: Welcome to the protected endpoint!
else:
    print(response.json()['message']) # Output: Invalid token
