import requests
url = "https://bit.ly/2ta5cJP"
site = requests.get(url)
print("Actual url is:",site.url)
