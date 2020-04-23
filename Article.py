from flask import Markup

class Article:
    def __init__(self, author: str, pubdate: str, title: str, html: str):
        self.author = author
        self.pubdate = pubdate
        self.title = title
        self.html = Markup(html)
