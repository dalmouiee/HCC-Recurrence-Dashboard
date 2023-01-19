from dash import html
import dash_bootstrap_components as dbc

first_card = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H2(
                    f"100%",
                    id=f"card-1-percent-rec",
                    className="card-title text-center",
                ),
                html.P("", id=f"card-1-label-rec", className="text-center"),
            ]
        )
    ],
    color="success",
    inverse=True,
)

second_card = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H2(
                    f"0%",
                    id=f"card-2-percent-non-rec",
                    className="card-title text-center",
                ),
                html.P("", id=f"card-2-label-non-rec", className="text-center"),
            ]
        )
    ],
    color="danger",
    inverse=True,
)
