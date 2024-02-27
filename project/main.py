from flask import Flask, render_template, request

from project.common.forms import SearchForm
from project.logic.processor import process_keyword


app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template("index.html", form=SearchForm())


@app.route('/search', methods=['POST'])
def search():
    form = SearchForm(request.form)
    keyword = form.search_key.data
    result = process_keyword(keyword)
    return render_template("search.html", form=SearchForm(), keyword=keyword, result=result)


if __name__ == "__main__":
    app.run(debug=True)
