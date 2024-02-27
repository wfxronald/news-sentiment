import json
import os

from dotenv import load_dotenv
import requests


def perform_search(keyword):
    # TODO: review caching logic, currently cache to save up API calls
    if os.path.isfile(f'{keyword}.json'):
        print("retrieving cached data")
        with open(f'{keyword}.json', 'r', encoding='utf-8') as f:
            cached_data = json.load(f)
        return cached_data

    load_dotenv()

    endpoint = "https://www.googleapis.com/customsearch/v1"
    query_param = {
        "key": os.environ["API_KEY"],
        "cx": os.environ["SEARCH_ENGINE_ID"],
        "q": keyword,
    }

    r = requests.get(url=endpoint, params=query_param)
    data = r.json()

    with open(f'{keyword}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return data


def pack_result(data):
    to_return = []

    for item in data["items"]:
        to_return.append({
            "title": item["title"],
            "link": item["link"],
        })

    return to_return


def search(keyword):
    return pack_result(perform_search(keyword))
