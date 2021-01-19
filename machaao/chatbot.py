# Bot Template: A simple sample echo bot to get started.
# Platform: MessengerX.io
# Author: @Abhishek Raj

from flask import request, Response
from flask_api import FlaskAPI, status
import requests
import re
import json
import argparse

from machaao import Machaao

app = FlaskAPI(__name__)

# Get your MESSENGERX_API_TOKEN from https://portal.messengerx.io
MESSENGERX_API_TOKEN = ""

# For development use https://ganglia-dev.machaao.com
MESSENGERX_BASE_URL = "https://ganglia-dev.machaao.com"

machaao = Machaao(MESSENGERX_API_TOKEN, MESSENGERX_BASE_URL)

@app.route("/health")
def health_check():
    """
    Function to check, server running or not.
    """
    return {"status": 200, "msg": "Service is Up"}


@app.route("/machaao/incoming", methods=["POST"])
def messageHandler():
    """
    Incoming message handler.
    """

    # Edit this function the way you want.

    incoming_data = machaao.request_handler(request)

    user_id = incoming_data["user_id"]

    message = incoming_data["messaging"]

    message = message[0]["message_data"]["text"]

    # Currently server set to echo.
    # Write your code here.

    payload = {
        "identifier": "BROADCAST_FB_QUICK_REPLIES",
        "users": [user_id],
        "message": {"text": message},
    }

    # Read more about APIs here: https://ganglia.machaao.com/api-docs/#/
    # or here https://messengerx.readthedocs.io/en/latest/ or here
    # https://github.com/machaao/machaao-py

    response = machaao.send_message(payload)

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
    parser = argparse.ArgumentParser(description='A simple Machaao Chatbot')
    parser.add_argument('-p', '--port', type=int, default=False,
                        help='Port number of the local server')
    args = parser.parse_args()
    if args.port:
        _port = args.port
        print(f"starting at {_port}")
        app.run(host="0.0.0.0", port=_port)
    else:
        app.run(host="0.0.0.0")
