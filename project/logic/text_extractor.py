import trafilatura


# this method mutates the existing data dictionary
def get_text_content(results):
    for result in results:
        downloaded = trafilatura.fetch_url(result["link"])
        text = trafilatura.extract(downloaded)
        result["text"] = text
