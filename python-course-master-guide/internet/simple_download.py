import requests

url = "https://www.httpbin.org/ip"

response = requests.get(url)
if response.status_code == 200:
    print(response.text)
else:
    print("Download error.")
