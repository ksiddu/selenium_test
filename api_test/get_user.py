import requests

#resp = requests.get("https://reqres.in/api/users?page=2")
p = {"pages":2}
resp = requests.get("https://reqres.in/api/users", params=p)

code = resp.status_code


print("URL", resp.url)
print("code", code)
#print("body", body)

#print(resp.text)
#print(resp.content)
print(resp.json())
print(resp.headers)

headers = resp.headers
print(headers.get('Content-Type'))

json_response = resp.json()
assert json_response['total'] == 12
assert json_response['total_pages'] == 2, "total pages not found"

print(json_response["data"][0]['email'])
assert (json_response["data"][0]['email'])!=None

print(json_response["support"]['url'])