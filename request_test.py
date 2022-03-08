import requests
import json

url = 'http://localhost:8000'

# fetching records
x = requests.get(url+"/books", headers = {"HTTP_HOST": "localhost:8000"})
print(f"Status code: {x.status_code} \n")
print(f"All Books: {x.text} \n")
x = requests.get(url+"/books/1")
print(f"First record: {x.json()} \n")

# create records
payload = {"isbn":"4545454", "title":"Book Three", "author":{"firstname":"Harry","lastname":"White"}}
r = requests.post(url+"/books", data=payload)
if r.status_code == 200:
    print("Record Added \n")

x = requests.get(url+"/books", headers = {"HTTP_HOST": "localhost:8000"})
print(f"All Books: {x.text} \n")

# remove records
r = requests.delete(url+"/books/1")
if r.status_code == 200:
    print("Record Removed \n")

# edit records
payload = {"isbn":"454555", "title":"Updated Title", "author":{"firstname":"Sharron","lastname":"Smith"}}
r = requests.put(url+"/books/2", data=payload)