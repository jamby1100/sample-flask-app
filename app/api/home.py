from flask import jsonify, request, render_template, redirect, url_for
from . import api
import os
import json

@api.route('/')
def home():
    return json.dumps({"status": "welcome"})