from config import inventory_collection
from bson import ObjectId

def serialize_item(item):
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "quantity": item["quantity"],
        "price": item["price"]
    }

def add_item(data):
    item = {
        "name": data["name"],
        "quantity": data["quantity"],
        "price": data["price"]
    }
    result = inventory_collection.insert_one(item)
    return str(result.inserted_id)

def get_all_items():
    return [serialize_item(item) for item in inventory_collection.find()]

def get_item(item_id):
    item = inventory_collection.find_one({"_id": ObjectId(item_id)})
    return serialize_item(item) if item else None

def update_item(item_id, data):
    result = inventory_collection.update_one(
        {"_id": ObjectId(item_id)},
        {"$set": data}
    )
    return result.modified_count > 0

def delete_item(item_id):
    result = inventory_collection.delete_one({"_id": ObjectId(item_id)})
    return result.deleted_count > 0
