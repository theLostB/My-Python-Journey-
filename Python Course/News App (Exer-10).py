import requests
import json

query = input("Which type of news you want: ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-01-19&sortBy=publishedAt&apiKey=795129f1e4c545ac8b5a574ed6de6531"
response = requests.get(url)
news = json.loads(response.text)

# Check if "articles" key exists in the response
if "articles" in news:
    articles = news["articles"]
    # Limiting the number of articles to 10
    for article in articles[:10]:
        print("\n\n• ", article["title"])
        print("  ", article["description"])
        print("____________________________________________________________\n")
else:
    print("No articles found for the given query.")
