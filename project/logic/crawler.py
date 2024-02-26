# import json
import os

from dotenv import load_dotenv
import requests


def perform_search(keyword):
    load_dotenv()

    endpoint = "https://www.googleapis.com/customsearch/v1"
    query_param = {
        "key": os.environ["API_KEY"],
        "cx": os.environ["SEARCH_ENGINE_ID"],
        "q": keyword,
    }

    r = requests.get(url=endpoint, params=query_param)
    data = r.json()

    # with open('test.json', 'w', encoding='utf-8') as f:
    #     json.dump(data, f, ensure_ascii=False, indent=4)

    # with open('test.json', 'r', encoding='utf-8') as f:
    #     data = json.load(f)

    return data
