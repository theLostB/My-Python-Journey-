import requests

url = "https://google.com"
file_name = "download.html"

response = requests.get(url)
if response.status_code == 200:
    with open(file_name, 'wb') as f:
        f.write(response.content)
    print("Download successful!")
else:
    print("Failed to download:", response.status_code)
