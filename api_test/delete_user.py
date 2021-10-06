import requests


resp = requests.delete("https://reqres.in/api/users/2")

print(resp.status_code)
assert resp.status_code==204

print(resp.headers)

headers = resp.headers

for key, value in headers.items():
    print(key, ":", value)

