from flask import request, jsonify, Response
from flask_api import FlaskAPI, status
import requests
import re
import json

from machaao import request_handler, send_message

app = FlaskAPI(__name__)

# Get your MESSENGERX_API_TOKEN from https://portal.messengerx.io
MESSENGERX_API_TOKEN = ""

# For development use https://ganglia-dev.machaao.com
MESSENGERX_BASE_URL = "https://ganglia-dev.machaao.com"


@app.route("/health")
def health_check():
    """
    Function to check, server running or not.
    """
    ret = {"Status": 200, "Msg": "Service is Up"}
    return jsonify(ret)


@app.route("/machaao/incoming", methods=["GET", "POST"])
def messageHandler():
    """
    Incoming message handler.
    """

    # Edit this function the way you want.

    incoming_data = request_handler(request)

    user_id = incoming_data["user_id"]

    message = incoming_data["messaging"]

    source = incoming_data["source"]

    message = message[0]["message_data"]["text"]

    # Currently server set to echo.
    # Write your code here.

    payload = {
        "identifier": "BROADCAST_FB_QUICK_REPLIES",
        "users": [user_id],
        "message": {"text": message},
    }

    if source:
        payload["source"] = source

    # Read more about APIs here: https://ganglia.machaao.com/api-docs/#/
    # or here https://messengerx.readthedocs.io/en/latest/ or here
    # https://github.com/machaao/machaao-py 
    response = send_message(MESSENGERX_API_TOKEN, MESSENGERX_BASE_URL, payload)

    output_payload = {
        "success": True,
        "message": response.text,
    }

    return Response(
        mimetype="application/json",
        response=json.dumps(output_payload),
        status=200,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0")
