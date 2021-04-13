import requests

id = int(input("Inserire il proprio id"))
url = " http://127.0.0.1:5000/request"

params = {'id': id }

r = requests.get(url=url, params=params)

print(r.status_code)
