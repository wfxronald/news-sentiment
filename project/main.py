from flask import Flask, render_template, request

from project.common.forms import SearchForm
from project.logic.crawler import perform_search
from project.logic.text_extractor import extract_snippet_from_search_result
from project.logic.sentiment_analyzer import analyze_sentiments


app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template("index.html", form=SearchForm())


@app.route('/search', methods=['POST'])
def search():
    form = SearchForm(request.form)
    keyword = form.search_key.data
    search_result = perform_search(keyword)
    snippets = extract_snippet_from_search_result(search_result)
    result = analyze_sentiments(snippets)
    return render_template("search.html", form=SearchForm(), keyword=keyword, result=result)


if __name__ == "__main__":
    app.run(debug=True)
