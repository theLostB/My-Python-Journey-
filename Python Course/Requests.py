import requests
from bs4 import BeautifulSoup
#Sending get request
response = requests.get("https://codewithharry.com")
print(response.text)
#Sending POST Request
url = "https://jsonplaceholder.typicode.com/posts"
data = {
  "title": 'harry',
  "body": 'bhai',
  "userId": 12,
}
headers = {'Content-type': 'application/json; charset=UTF-8'}
response = requests.post(url, headers=headers, json=data)
print(response.text) 
r2 = requests.get('https://codewithharry.com')
#we use this
soup = BeautifulSoup(r2.text, 'html.parser')#because this preetfy the code
print(soup.prettify())
for heading in soup.find_all('h2'):
    print(heading.text) #We can also scrap elements like this
    #here we scrap h2 from this page