import requests


data = {'values':[1,2,3,4,5]}
response = requests.post('http://127.0.0.1:3000/first_app', json=data )

print(response.text)