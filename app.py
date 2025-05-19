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

@app.route('/transactions', methods=['GET', 'POST'])
def manage_transactions():
    if request.method == 'GET':
        return jsonify(transactions)
    elif request.method == 'POST':
        data = request.json
        action = data['action']
        user_id = data['user_id']
        book_id = data['book_id']

        if user_id not in users or book_id not in books:
            return jsonify({'status':'error', 'message':'Invalid user or book'}), 400

        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        transactions.append({
            'user_id': user_id,
            'user_name': users[user_id]['name'],
            'book_id': book_id,
            'book_title': books[book_id]['title'],
            'action': action,
            'date': date
        })
        return jsonify({'status': 'success'}), 201
