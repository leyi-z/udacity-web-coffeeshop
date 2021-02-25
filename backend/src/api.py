import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth


app = Flask(__name__)
setup_db(app)
CORS(app)


@app.after_request
def after_request(response):
    response.headers.add(
        'Access-Control-Allow-Headers',
        'Content-Type, Authorization'
    )
    response.headers.add(
        'Access-Control-Allow-Methods',
        'GET, POST, PATCH, DELETE, OPTIONS'
    )
    return response


# db_drop_and_create_all()


##########
# ROUTES #
##########

# placeholder homepage
@app.route('/', methods=['GET'])
def greeting_all():
    return jsonify({
        "greetings": 'bleh!'
    })


@app.route('/drinks', methods=['GET'])
def drinks_all():
    try:
        drinks = Drink.query.order_by(Drink.id).all()
        drinks = [drink.short() for drink in drinks]
        return jsonify({
            "success": True,
            "drinks": drinks
        }), 200
    except Exception as e:
        print(e)
        abort(404)


@app.route('/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def drinks_detail(jwt):
    try:
        drinks = Drink.query.order_by(Drink.id).all()
        drinks = [drink.long() for drink in drinks]
        return jsonify({
            "success": True,
            "drinks": drinks
        }), 200
    except Exception as e:
        print(e)
        abort(404)


@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def new_drink(jwt):
    body = request.get_json()
    new_title = body.get('title', None)
    new_recipe = body.get('recipe', None)
    new_recipe = json.dumps(new_recipe)
    try:
        new_drink = Drink(
            title=new_title,
            recipe=new_recipe
        )
        new_drink.insert()
        return jsonify({
            "success": True,
            "new id": new_drink.id
        }), 200
    except Exception as e:
        print(e)
        abort(422)


@app.route('/drinks/<int:drink_id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drink(jwt, drink_id):
    body = request.get_json()
    new_title = body.get('title', None)
    new_recipe = body.get('recipe', None)
    new_recipe = json.dumps(new_recipe)
    drink = Drink.query.filter(
        Drink.id == drink_id).order_by(
        Drink.id).one_or_none()
    try:
        drink.title = new_title
        drink.recipe = new_recipe
        drink.update()
        return jsonify({
            "success": True,
            "updated id": drink.id
        }), 200
    except Exception as e:
        print(e)
        abort(422)


@app.route('/drinks/<int:drink_id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(jwt, drink_id):
    drink = Drink.query.filter(
        Drink.id == drink_id).order_by(
        Drink.id).one_or_none()
    try:
        drink.delete()
        return jsonify({
            "success": True,
            "deleted id": drink_id
        }), 200
    except Exception as e:
        print(e)
        abort(422)


##################
# Error Handling #
###################


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "Bad request"
    }), 400


@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "unauthorized"
    }), 401


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "not found"
    }), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        "success": False,
        "error": 405,
        "message": "method not allowed"
    }), 405


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(500)
def server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "internal server error"
    }), 500


@app.errorhandler(AuthError)
def auth_error(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "unauthorized"
    }), 401
