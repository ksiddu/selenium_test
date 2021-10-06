import requests
payload = {
    "name": "Siddu"
}

print(type(payload))
resp = requests.patch("https://reqres.in/api/users/2", data=payload)

print(resp.status_code)
print(resp.json())
print(resp.headers)
json_resp = resp.json()
assert json_resp['name'] == 'Siddu', "name not equals"