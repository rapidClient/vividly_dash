from flask import Flask, request
import requests

from vividly_dash.settings import META_ACCESS_TOKEN_URL


class OAuthViews:
    server: Flask = None

    @server.route("/access_token")
    def meta_redirect():
        if "code" in request.args.keys():
            auth_code = request.args.get("code")
            endpoint = META_ACCESS_TOKEN_URL + f"&code={auth_code}"
            response = requests.get(endpoint)
            return response.json()
        return "Error"
    
    @classmethod()
    def create(cls, server):
        cls.server = server
