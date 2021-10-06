import requests

# https://www.machinelearningplus.com/python/requests-in-python/
# GET METHOD
# Setting parameters
#parameter= {'page':5 , 'count':10}
parameter= (('page',5) , ('count',10))
get_resp = requests.get("http://httpbin.org/", params=parameter)

code = get_resp.status_code
print("URL", get_resp.url)
print("code", code)
print(get_resp.text[:400])


# POST METHOD
# Setting parameters
param = { 'custname':'abcd', 'custemail': 'efgh@gmail.com'}
post_resp = requests.post("http://httpbin.org/post", data=param)

code = post_resp.status_code
print("URL", post_resp.url)
print("code", code)
print(post_resp.json())

for k, v in post_resp.json().items():
  print(k, ": ", v)

# PUT METHOD
put_resp = requests.put("https://httpbin.org/put", data={'name':'abcd'})

code = put_resp.status_code
print("URL", put_resp.url)
print("code", code)
print(put_resp.content)
print(put_resp.json())

# DELETE METHOD
delete_resp = requests.delete("https://httpbin.org/delete", data={'name':'abcd'})

code = delete_resp.status_code
print("URL", delete_resp.url)
print("code", code)
print(delete_resp.content)

# PATCH METHOD
patch_resp = requests.patch("https://httpbin.org/patch", data={'name':'abcd'})

code = patch_resp.status_code
print("URL", patch_resp.url)
print("code", code)
print(patch_resp.content)