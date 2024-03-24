from typing import Type
from flask import Flask

app = Flask(__name__)


@app.errorhandler(404)
def not_found(e: Type[Exception]) -> str:
    if str(e)[:3] == '404':
        result = 'Этой страницы нет. Все доступные страницы:'
        for i in app.url_map.iter_rules():
            result += f'<br>{i}'
        return result


@app.route('/hello')
def hello():
    return 'hello'


@app.route('/bye')
def bye():
    return 'bye'


if __name__ == '__main__':
    app.run(debug=True)
