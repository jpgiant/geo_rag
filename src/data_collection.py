import wikipediaapi
import json
from dotenv import load_dotenv
import os

load_dotenv()    

def collect_wikipedia_data():
    user_agent = os.getenv("USER_AGENT", "DefaultBot/1.0")
    wiki = wikipediaapi.Wikipedia(language='en', user_agent=user_agent)
    categories=["Geography of India", "Mountains of India", "Rivers of India"]
    data=[]

    for category in categories:
        cat=wiki.page(f"Category: {category}")
        for page in cat.categorymembers.values():
            if page.ns==0:
                content=wiki.page(page.title).text
                data.append({'title': page.title, 'content': content})

    with open('data/wikipedia_indian_geography.json', 'w') as f:
        json.dump(data, f)


if __name__ == "__main__":
    collect_wikipedia_data()