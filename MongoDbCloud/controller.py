from flask import request, jsonify
import service

def register_routes(app):
    @app.route('/items', methods=['GET'])
    def get_items():
        items = service.get_all_items()
        return jsonify(items)

    @app.route('/items', methods=['POST'])
    def add_item():
        data = request.json
        inserted_id = service.add_item(data)
        return jsonify({"inserted_id": inserted_id}), 201
