import requests
"""payloads={
    'page':2,'count':25
}"""
payloads={
    'username':'hkom',
    'password':'testing'
}
#r=requests.get('https://httpbin.org/get',params=payloads)
#r=requests.post('https://httpbin.org/post',data=payloads)
#r=requests.get('https://httpbin.org/basic-auth/hkom/testing',auth=('hkom','testing'))
r=requests.get('https://httpbin.org/delay/6',timeout=3)

"""print(dir(r))
print(help(r))
print(r.text)
with open ('comic.png','wb') as f:
    f.write(r.content)
print(r.status_code)
print(r.ok)"""
"""print (r.headers)"""
#https:/httpbin.org/
#r.url,r.url,r.text,r.json()
#r_dict=r.json()
print(r)


