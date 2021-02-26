from flask import Flask, jsonify

app = Flask(__name__)

books = [
 {'id': 0, 'title': 'Il nome della Rosa', 'author': 'Umberto Eco','year_published': '1980'},
 {'id': 1, 'title': 'Il problema dei tre corpi', 'author': 'Liu Cixin', 'published': '2008'},
 {'id': 2,'title': 'Fondazione', 'author': 'Isaac Asimov', 'published': '1951'} ]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Biblioteca online</h1><p>Prototipo di web API.</p>"

@app.route('/api')
def api_all():
    return jsonify(books)

@app.route('/findip')
def findip():

    return "todo"


if __name__ == '__main__':
    app.run()