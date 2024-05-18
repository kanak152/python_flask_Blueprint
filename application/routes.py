from flask import render_template , jsonify,request
from . import application

# Sample data to simulate a database
sample_data = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"},
    {"id": 3, "name": "Item 3", "description": "This is item 3"},
]

@application.route('/')
def home():
    return render_template('index.html')

@application.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(sample_data)

@application.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in sample_data if item["id"] == item_id), None)
    if item is not None:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404

@application.route('/api/items', methods=['POST'])
def create_item():
    new_item = request.json
    new_item["id"] = len(sample_data) + 1
    sample_data.append(new_item)
    return jsonify(new_item), 201
