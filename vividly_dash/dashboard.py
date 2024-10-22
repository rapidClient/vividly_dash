from dash import html, dcc, callback, Output, Input, State
import dash_bootstrap_components as dbc

from vividly_dash.settings import META_LOGIN_URL

layout = dbc.Container(
    [
        dbc.NavbarSimple(
            dbc.Button(
                html.P(
                    [html.Span(className="bi bi-download me-1"), "Import"],
                    className="my-0 mx-0 align-middle fw-semibold",
                ),
                id="import-button",
                title="Import",
                size="md",
                class_name="rounded-pill my-0 mx-0 px-4 py-3",
            ),
            brand="VIVIDLY",
            dark=True,
            sticky="top",
            brand_style={
                "font-family": "Poppins sans-serif",
                "font-size": "2.8rem",
                "font-weight": "700",
                "color": "#df6919",
                "text-transform": "uppercase",
                "letter-spacing": "0.05rem",
                "transition": "color 0.3s ease, transform 0.3s ease",
            },
            class_name="py-2",
        ),
        html.Div(
            [
                dbc.Col(
                    [
                        dbc.Navbar(),
                        dbc.Col(),
                    ]
                ),
                dbc.Col(),
            ]
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Select the platform..")),
                dbc.ModalBody(
                    dbc.Row(
                        [
                            dbc.Button(
                                [
                                    html.I(className="bi bi-meta"),
                                    html.P("Meta"),
                                ],
                                class_name="w-25 me-4",
                                # external_link="",
                                href=META_LOGIN_URL,
                            ),
                            dbc.Button(
                                [
                                    html.I(className="bi bi-google"),
                                    html.P("Google"),
                                ],
                                class_name="w-25",
                            ),
                        ],
                        justify="center",
                    ),
                ),
            ],
            id="select-platform-dialog",
            is_open=False,
        ),
    ],
    class_name="bg-primary px-0",
    fluid=True,
)


@callback(
    Output("select-platform-dialog", "is_open"),
    Input("import-button", "n_clicks"),
    prevent_initial_call=True,
)
def open_platform_select_dialog(_):
    return True
