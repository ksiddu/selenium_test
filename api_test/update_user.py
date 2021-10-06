import requests
payload = {
    "name": "morpheus",
    "job": "QA2"
}

print(type(payload))
resp = requests.put("https://reqres.in/api/users/2", data=payload)

print(resp.status_code)
print(resp.json())
print(resp.headers)
json_resp = resp.json()
assert json_resp['job'] == 'QA2', "job not equals"