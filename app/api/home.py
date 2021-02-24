from flask import jsonify, request, render_template, redirect, url_for, Response
from . import api
import os
import json

user_db = {
    "raphael.jambalos@gmail.com": {"password": "jambyiscool", "token": "jambytoken"},
    "ana.jambalos@gmail.com": {"password": "anaiscool", "token": "anatoken"},
    "john.jambalos@gmail.com": {"password": "johniscool", "token": "johntoken"},
    "miguel.jambalos@gmail.com": {"password": "migueliscool", "token": "migueltoken"},
    "ysabelle.jambalos@gmail.com": {"password": "ysabelleiscool", "token": "ysabelletoken"},
}


def build_post_body():
    if request.json:
        return request.json
    elif request.form.to_dict():
        return request.form.to_dict()

    return {}

def authenticated():
    auth_token = request.headers.get('Auth')

    for email in user_db:
        user = user_db[email]
        if user["token"] == auth_token:
            return True

    return False


@api.route('/')
def home():
    return json.dumps({"status": "homeroast celebration"})


cards = []

@api.route('/users/signin', methods=['POST'])
def users_sign():
    post_body = build_post_body()

    if "email" not in post_body or "password" not in post_body:
        return Response("{'access denied':'your request does not have email or password'}", status=403, mimetype='application/json')

    if post_body["email"] in user_db:
        user = user_db[post_body["email"]]

        if user["password"] == post_body["password"]:
            token = user['token']
            return Response("{'token':" + token + "}", status=200, mimetype='application/json')
        else:
            return Response("{'access denied':'you have the wrong password'}", status=403, mimetype='application/json')
    else:
        return Response("{'access denied':'username is not in database'}", status=403, mimetype='application/json')

@api.route('/loyalty_cards', methods=['POST'])
def loyalty_cards_create():
    post_body = build_post_body()

    print("LOYALTY CARDS")

    if not authenticated():
        return Response("{'forbidden':'you are logged out'}", status=403, mimetype='application/json')

    if "first_name" not in post_body or "last_name" not in post_body:
        return Response("{'wrong input':'you did not supply a last name or first name'}", status=400, mimetype='application/json')

    if len(post_body["first_name"]) <= 2 or len(post_body["last_name"]) <= 2:
        return Response("{'wrong input':'last name or first name must be more than 2 letters'}", status=400, mimetype='application/json')


    return json.dumps({"status": "we created loyalty cards", "post_body": post_body})

@api.route('/loyalty_cards', methods=['GET'])
def loyalty_cards_list():
    if not authenticated():
        return Response("{'forbidden':'you are logged out'}", status=403, mimetype='application/json')

    return json.dumps({"status": "displaying loyalty cards", "cards": cards})

@api.route('/loyalty_cards/<loyalty_card_id>', methods=['GET'])
def loyalty_cards_show(loyalty_card_id):
    if not authenticated():
        return Response("{'forbidden':'you are logged out'}", status=403, mimetype='application/json')

    print(f"RETRIEVE INFORMATION FOR loyalty_card_id: {loyalty_card_id}")

    return json.dumps({"status": f"we looked on loyalty card number: {loyalty_card_id}"})


@api.route('/transactions', methods=['POST'])
def transactions_create():
    post_body = build_post_body()

    print("TRANSACTIONS")

    return json.dumps({"status": "we posted a transaction", "post_body": post_body})