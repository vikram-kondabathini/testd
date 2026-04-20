from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


@app.route('/')
def read_route():
    return {"message": "Hello World! v2"}


books = [
    {"id": 1, "title": "Soft Skills", "author": "John Sonmez"},
    {"id": 2, "title": "The Daily Stoic", "author": "Ryan Holiday"}
]

@app.route('/books/<int:id>', methods=['GET'])
def get_books(id):
    book = [book for book in books if book['id'] == id]
    return jsonify(book), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
    # gunicorn -b '0.0.0.0' main':app


# curl http://localhost:5000/books
# curl -X POST -H "Content-Type: application/json" -d '{"title":"Book Name", "author":"Author Name"}' http://localhost:5000/books
# curl -X POST -H "Content-Type: application/json" -d "{\"title\":\"Book Name\", \"author\":\"Author Name\"}" http://localhost:5000/books
