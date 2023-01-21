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
                html.P(
                    "chance of patient tumour recurrence",
                    id=f"card-1-label-rec",
                    className="text-center",
                ),
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
                html.P(
                    "chance of patient tumour non-recurrence",
                    id=f"card-2-label-non-rec",
                    className="text-center",
                ),
            ]
        )
    ],
    color="danger",
    inverse=True,
)

third_card = dbc.Card(
    [
        dbc.CardBody(
            [
                # html.H2(
                #     f"0%",
                #     id=f"card-2-percent-non-rec",
                #     className="card-title text-center",
                # ),
                html.P(
                    "Hover over patient in graph to display their info",
                    id=f"card-3-label-datapoint-info",
                    className="text-center",
                ),
            ]
        )
    ],
    color="secondary",
    inverse=True,
)
