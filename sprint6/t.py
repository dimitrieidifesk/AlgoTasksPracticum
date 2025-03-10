import requests
r = requests.get('http://stagingdez.ru:8091/ai/config/1/')
print(r.status_code)
