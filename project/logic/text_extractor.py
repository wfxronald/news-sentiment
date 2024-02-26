def extract_snippet_from_search_result(data):
    text_to_analyze = []
    for item in data["items"]:
        text_to_analyze.append(item["snippet"])
    return text_to_analyze
