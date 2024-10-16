import os
from flask import Flask, render_template, url_for, redirect


def create_app(test_config=None):
    app = Flask(__name__,
                static_url_path='',
                instance_relative_config=True,
                )
    app.config.from_pyfile('config.py', silent=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return redirect('/index.html')

    @app.route('/alive')
    def hello():
        return f'service is running'

    return app
