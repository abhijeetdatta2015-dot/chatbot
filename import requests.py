import requests

resp = requests.get("http://127.0.0.1:8000/query/600363942")
print(resp.json())
