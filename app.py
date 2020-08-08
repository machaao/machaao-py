from flask import Flask, escape, request, Response, jsonify
from flask_api import FlaskAPI
import requests, re, json
from bs4 import BeautifulSoup
from flask_api import FlaskAPI
import jwt
import json
import requests
import linecache
import sys
import traceback
import os
import asyncio
from machaao import requestHandler

app = FlaskAPI(__name__)

@app.route("/health")
def health_check():
    ret = {"Status": 200, "Msg": "Service is Up"}
    return jsonify(ret)

@app.route("/machaao_hook", methods=["POST"])
def messageHandler():

    print(requestHandler(request))

    return jsonify({"Status": 200, "Msg": "Service is Up"})


if __name__ == "__main__":
    app.run(host="0.0.0.0")