from project.logic.crawler import search
from project.logic.text_extractor import get_text_content
from project.logic.sentiment_analyzer import analyze_sentiments


def process_keyword(keyword):
    search_result = search(keyword)
    get_text_content(search_result)
    analyze_sentiments(search_result)
    return search_result
