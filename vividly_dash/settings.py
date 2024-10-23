import dash_bootstrap_components as dbc
from dotenv import load_dotenv

import os

# Loading envs
load_dotenv()

# Secret Keys
# ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
APP_SECRET = os.getenv("APP_SECRET")
APP_ID = os.getenv("APP_ID")
# id = '<AD_ACCOUNT_ID>'

# URL
HOST_URL = "https://vividly-dash.onrender.com"
REDIRECT_URL = f"{HOST_URL}/access_token"

# Themes
THEME = dbc.themes.SUPERHERO
# Icons
ICON_PACK = dbc.icons.BOOTSTRAP

# Auth links
GOOGLE_LOGIN_URL=""

META_LOGIN_URL = f"https://www.facebook.com/v21.0/dialog/oauth?client_id={APP_ID}&redirect_uri={REDIRECT_URL}&scope=ads_read&response_type=code"

META_ACCESS_TOKEN_URL= f"https://graph.facebook.com/v21.0/oauth/access_token?client_id={APP_ID}&redirect_uri={REDIRECT_URL}&client_secret={APP_SECRET}"
