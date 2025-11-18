from flask import Blueprint, request, jsonify
from models.inventory_model import (
    add_item, get_all_items, get_item, update_item, delete_item
)

inventory_bp = Blueprint("inventory", __name__)

@inventory_bp.route("/items", methods=["POST"])
def create_item():
    data = request.json
    item_id = add_item(data)
    return jsonify({"message": "Item added", "id": item_id})

@inventory_bp.route("/items", methods=["GET"])
def read_items():
    return jsonify(get_all_items())

@inventory_bp.route("/items/<item_id>", methods=["GET"])
def read_single_item(item_id):
    item = get_item(item_id)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

@inventory_bp.route("/items/<item_id>", methods=["PUT"])
def update(item_id):
    data = request.json
    updated = update_item(item_id, data)
    if updated:
        return jsonify({"message": "Item updated"})
    return jsonify({"error": "Item not found"}), 404

@inventory_bp.route("/items/<item_id>", methods=["DELETE"])
def delete(item_id):
    deleted = delete_item(item_id)
    if deleted:
        return jsonify({"message": "Item deleted"})
    return jsonify({"error": "Item not found"}), 404
