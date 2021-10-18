import requests

server_name = "http://127.0.0.1:5000"

r = requests.get(server_name+"/info")
print(r.text)