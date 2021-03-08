from flask import Flask, jsonify, request
app = Flask(__name__)
stores = [
    {
        "name": "My Wonderful Store",
        "items": [
            {
                "name": "Milk",
                "price": 15.99
            }
        ]
    },
    {
        "name": "My Awesome Store",
        "items": [
            {
                "name": "Soap",
                "price": 5.19
            },
            {
                "name": "Tablet",
                "price": 12.90
            },
            {
                "name": "TV",
                "price": 30.00
            }
        ]
    }
]


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    stores.append(request_data)
    return jsonify({"store": request_data})


@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({"store": store})


@app.route('/store')
def get_stores():
    return jsonify({"stores": stores})


@app.route('/store/<string:name>/items', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            newItem = {
                "name": request_data['name'],
                "price": request_data['price']
            }
            store['items'].append(newItem)
            return jsonify({"Item": newItem})


@app.route('/store/<string:name>/items')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({"Items": store["items"]})


if __name__ == "__main__":
    app.run(port=5000)
