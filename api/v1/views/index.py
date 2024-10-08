#!/usr/bin/python3
# api/v1/views/index.py

from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status', methods=['GET'])
def status():
    """Return status of the API"""
    return jsonify({"status": "OK"})

