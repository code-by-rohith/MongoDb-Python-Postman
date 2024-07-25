from flask import request, jsonify
import UserService
def create_user():
    data = request.get_json()
    data.pop('_id', None)

    result = UserService.insert_mongo(data)
    return jsonify({'id': str(result.inserted_id)}), 201

def update_user(id):
    data = request.get_json()
    result = UserService.update_mongo(id, data)

    if result.matched_count == 0:
        return jsonify({'error': 'Not found'}), 404

    return jsonify({
        'matched': result.matched_count,
        'modified': result.modified_count
    }), 200


def get_user(id):
    result = UserService.get_mongo(id)

    if result is None:
        return jsonify({'error': 'Not found'}), 404

    result['_id'] = str(result['_id'])
    return jsonify(result), 200
