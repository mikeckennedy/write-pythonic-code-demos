# requirements.txt
import requests
import records

r = requests.get("http://google.com")
print(r.status_code)
