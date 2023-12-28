from flask import Blueprint, request, jsonify

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    search_id = request.args.get('id')
    search_name = request.args.get('name')
    search_age = request.args.get('age')
    search_occupation = request.args.get('occupation')

    results = []

    for item in USERS:
        match = ((search_id is None or str(item['id']) == search_id) and
            (search_name is None or item['name'].lower() == search_name.lower()) and
            (search_age is None or str(item['age']-1) <= search_age <= str(item['age']+1)) and
            (search_occupation is None or search_occupation.lower() in item['occupation'].lower() == search_occupation.lower()))
        if match:
            results.append(item)
    if results:
            return jsonify({'results': results})
    else:
        return jsonify({'error':'No matching records found.'})