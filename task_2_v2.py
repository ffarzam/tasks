import requests


def get_sports_news(api_key, count=20):
    url = f'https://newsapi.org/v2/top-headlines'
    params = {
        'apiKey': api_key,
        'category': 'sports',
        'pageSize': count,
        "language": "en"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()['articles']
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None


def display_news(news_list):
    if news_list:
        for index, news in enumerate(news_list, start=1):
            print(f"{index}. {news['title']}")
            print(f"{news['description']}")
            print(f"Source: {news['source']['name']}")
            print(f"URL: {news['url']}")
            print()


if __name__ == "__main__":
    api_key = "83a35dd3b2fc422daf92d6e3a6e290a2"

    sports_news = get_sports_news(api_key)

    if sports_news:
        display_news(sports_news)
