import requests
payload = {
    "name": "Siddu",
    "job": "QA"
}

print(type(payload))
resp = requests.post("https://reqres.in/api/users", data=payload)

print(resp.status_code)
print(resp.json())
print(resp.headers)
json_resp = resp.json()
assert json_resp['job'] == 'QA', "job not equals"