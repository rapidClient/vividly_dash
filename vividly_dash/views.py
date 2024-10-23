from flask import Flask, jsonify, request
import requests

from vividly_dash.settings import META_ACCESS_TOKEN_URL


def access_token(server: Flask) -> None:
    @server.route("/access_token")
    def redirect():
        if "code" in request.args.keys():
            auth_code = request.args.get("code")
            endpoint = META_ACCESS_TOKEN_URL + f"&code={auth_code}"
            response = requests.get(endpoint)
            return response.json()
        return "Error"
