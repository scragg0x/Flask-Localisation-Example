from flask import Flask, Blueprint, g, redirect, request

app = Flask(__name__)

mod = Blueprint('mysite', __name__, url_prefix='/<lang_code>')

sites = {
    'mysite.com': 'en',
    'myothersite.com': 'fr'
}

@app.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('lang_code', g.lang_code)

@app.url_value_preprocessor
def pull_lang_code(endpoint, values):
    url = request.url.split('/', 3)
    g.lang_code = sites[url[2]]

@mod.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('lang_code', g.lang_code)

@mod.url_value_preprocessor
def pull_lang_code(endpoint, values):
    g.lang_code = values.pop('lang_code')
    url = request.url.split('/', 3)
    if not g.lang_code:
        g.lang_code = sites[url[2]]

@app.route('/')
@mod.route('/')
def index():
    # Use g.lang_code to pull localized data for template
    return 'lang = %s' % g.lang_code

app.register_blueprint(mod)