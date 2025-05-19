from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

users = {
    '1': {'name': 'Alice'},
    '2': {'name': 'Bob'}
}

books = {
    '101': {'title': 'Book A', 'cover': 'book_a.jpg'},
    '102': {'title': 'Book B', 'cover': ''}
}

transactions = []

@app.route('/transactions', methods=['GET'])
def get_transactions():
    return jsonify(transactions)

if __name__ == '__main__':
    app.run(debug=True)
