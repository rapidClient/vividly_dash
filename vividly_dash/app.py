from dash import Dash, html, dcc, callback, Output, Input

from vividly_dash.dashboard import layout
from vividly_dash.settings import THEME, ICON_PACK
from vividly_dash.views import OAuthViews


def create_app():
    app = Dash(
        __name__,
        external_stylesheets=[THEME, ICON_PACK],
        title="Vividly - Ads Analytics",
    )

    # Setting up access token retriver view for google and meta ads apis
    OAuthViews.create(app.server)

    app.layout = layout

    return app
