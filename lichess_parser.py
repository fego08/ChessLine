import requests

url = 'https://lichess.org/api/account'
headers = {'Authorization': 'Bearer lip_2b2jM2kM659XMu0EnoWG'}
r = requests.get(url, headers=headers)
print(f'Status Code: {r.status_code}')

response_dict = r.json()
print(f'Username: {response_dict["username"]}')
print(f'Current Game: {response_dict["playing"]}')