import os
import yaml
import markdown

from flask import Flask
from flask import g
from flask import Markup

from Article import Article
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    articles = []
    path = "static/articles"
    for filename in os.listdir(path):
        if filename.endswith(".yaml"):
            with open(path + os.sep + filename) as metadata_file:
                metadata = yaml.load(metadata_file, yaml.FullLoader)
                with open(path + os.sep + filename.replace(".yaml", ".md")) as markdown_file:
                    markdown_html = markdown.markdown(markdown_file.read())
                    articles.append(Article(metadata['author'], metadata['pubdate'], metadata['title'], markdown_html))
    g.articles = articles

    return render_template('base.html')


if __name__ == '__main__':
    app.run()
