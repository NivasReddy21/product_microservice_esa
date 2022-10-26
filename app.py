"""Imports Flask"""
import json
from flask import Flask, jsonify
from pymongo import MongoClient
from bson import json_util
import urllib

app = Flask(__name__)

def get_database():
    """Creates and returns products column from Mongodb instance

    Returns:
        mongo_col: products list
    """

    CONNECTION_STRING = "mongodb+srv://NivasReddy:" + urllib.parse.quote("nivas@50") + "@cluster0.r4p9k.mongodb.net/test"
    client = MongoClient(CONNECTION_STRING)
    db = client['product_list']
    col = db["products"]

    return col

def parse_data(data):
    return json.loads(json_util.dumps(data))

@app.route('/rest/v1/products', methods = ['GET'])
def products():
    """Endpoint to get list of products

    Returns:
        json: List of products
    """
    try:
        mongo_col = get_database()
        data = mongo_col.find()
        product_list = parse_data(data)
        return jsonify({"products": product_list})

    except Exception as e:
        print(e)
        return jsonify({"error": e})
       

if __name__ == '__main__':
    app.run()
