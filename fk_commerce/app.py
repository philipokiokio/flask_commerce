from core import create_app
from flask import jsonify


app = create_app()


@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not found", "message": error.description}), 404


@app.errorhandler(400)
def bad_request_error(error):
    return jsonify({"error": "Bad request", "message": error.description}), 400


@app.errorhandler(500)
def internal_server_error(error):
    return (
        jsonify({"error": "Internal server error"}),
        500,
    )
