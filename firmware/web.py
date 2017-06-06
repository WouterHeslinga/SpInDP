from flask import Flask

class Web:
    """Web interface"""
    def __init__(self):
        self.web = Flask(__name__)
        self.web.add_url_rule('/', 'index', self.index)

    def index(self):
        return 'Hello World'

    def run(self):
        self.web.run()