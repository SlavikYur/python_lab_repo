from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://iotstudent:4321@localhost/iot_test_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class ItemOrdered(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    weight_kg = db.Column(db.Float, nullable=False)
    item_count = db.Column(db.Integer, nullable=False)
    item_type = db.Column(db.Enum('FRAGILE', 'LIQUID', 'REGULAR'), nullable=False)

    def __init__(self,
                 name,
                 price,
                 weight_kg,
                 item_count,
                 item_type,
                 ):

        self.name = name
        self.price = price
        self.weight_kg = weight_kg
        self.item_count = item_count
        self.item_type = item_type

db.create_all()

class ItemOrderedSchema(ma.Schema):
    class Meta:
        fields = ('name',
                 'price',
                 'weight_kg',
                 'item_count',
                 'item_type')

item_ordered_schema = ItemOrderedSchema()
items_ordered_schema = ItemOrderedSchema(many=True)
        

@app.route('/item_ordered', methods=['POST'])
def add_item_ordered():
    name = request.json['name']
    price = request.json['price']
    weight_kg = request.json['weight_kg']
    item_count = request.json['item_count']
    item_type = request.json['item_type']

    new_item = ItemOrdered(name,
                           price,
                           weight_kg,
                           item_count,
                           item_type)

    db.session.add(new_item)
    db.session.commit()

    return item_ordered_schema.jsonify(new_item)


@app.route('/item_ordered', methods=['GET'])
def get_items_ordered():
    all_items = ItemOrdered.query.all()
    return items_ordered_schema.jsonify(all_items)


@app.route('/item_ordered/<id>', methods=['GET'])
def item_ordered_info(id):
    item = ItemOrdered.query.get(id)

    if not item:
        abort(404)
    return item_ordered_schema.jsonify(item)


@app.route('/item_ordered/<id>', methods=['PUT'])
def update_item_ordered(id):
    item = ItemOrdered.query.get(id)

    if not item:
        abort(404)
    name = request.json['name']
    price = request.json['price']
    weight_kg = request.json['weight_kg']
    item_count = request.json['item_count']
    item_type = request.json['item_type']
        
    item.name = name
    item.price = price
    item.weight_kg = weight_kg
    item.item_count = item_count
    item.item_type = item_type
        
    db.session.commit()
    return item_ordered_schema.jsonify(item)


@app.route('/item_ordered/<id>', methods=['DELETE'])
def delete_item_ordered(id):
    item = ItemOrdered.query.get(id)

    if not item:
        abort(404)
    db.session.delete(item)
    db.session.commit()
    return item_ordered_schema.jsonify(item)
