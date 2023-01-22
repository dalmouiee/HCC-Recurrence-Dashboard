"""
    Module to handle the info banner cards
"""
from dash import html
import dash_bootstrap_components as dbc

rec_card = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H2(
                    "100%",
                    id="card-1-percent-rec",
                    className="card-title text-center",
                ),
                html.P(
                    "chance of patient tumour recurrence",
                    id="card-1-label-rec",
                    className="text-center",
                ),
            ]
        )
    ],
    color="danger",
    inverse=True,
)

non_rec_card = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H2(
                    "0%",
                    id="card-2-percent-non-rec",
                    className="card-title text-center",
                ),
                html.P(
                    "chance of patient tumour non-recurrence",
                    id="card-2-label-non-rec",
                    className="text-center",
                ),
            ]
        )
    ],
    color="success",
    inverse=True,
)

pat_info_card = dbc.Card(
    [
        dbc.CardBody(
            [
                html.P(
                    "Hover over patient in graph to display their info",
                    id="card-3-label-datapoint-info",
                    className="text-center",
                ),
            ]
        )
    ],
    color="secondary",
    inverse=True,
)
