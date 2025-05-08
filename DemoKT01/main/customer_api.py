from flask import Blueprint, jsonify, request
import service.customer_service as service

customer_api = Blueprint('customer_api', __name__)

@customer_api.route('/customers', methods=['GET'])
def get_customers():
    return jsonify(service.get_all_customers())

@customer_api.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete(customer_id):
    if service.delete_customer(customer_id):
        return jsonify({"message": "Deleted successfully"}), 200
    return jsonify({"error": "Customer not found"}), 404

@customer_api.route('/customers', methods=['POST'])
def add():
    data = request.json
    new_id = service.add_customer(data)
    return jsonify({"new_id": new_id})

@customer_api.route('/customers/<int:customer_id>', methods=['PUT'])
def update(customer_id):
    data = request.json
    if service.update_customer(customer_id, data):
        return jsonify({"message": "Updated successfully"})
    return jsonify({"error": "Customer not found"}), 404
