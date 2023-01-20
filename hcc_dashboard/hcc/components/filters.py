from dash import html
import dash_bootstrap_components as dbc

filter_card = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label("Age"),
                        dbc.RadioItems(
                            options=[
                                {"label": ">=65", "value": 0},
                                {"label": "<65", "value": 1},
                            ],
                            value=1,
                            id="radioitems-age-input",
                        ),
                    ]
                ),
                dbc.Col(
                    [
                        dbc.Label("Ethnicity"),
                        dbc.RadioItems(
                            options=[
                                {"label": "Asian", "value": 0},
                                {"label": "Caucasian", "value": 1},
                                {"label": "Others", "value": 2},
                            ],
                            value=1,
                            id="radioitems-ethnicity-input",
                        ),
                    ]
                ),
                dbc.Col(
                    [
                        dbc.Label("BMI"),
                        dbc.RadioItems(
                            options=[
                                {"label": ">=25", "value": 0},
                                {"label": "<25", "value": 1},
                            ],
                            value=1,
                            id="radioitems-BMI-input",
                        ),
                    ]
                ),
                dbc.Col(
                    [
                        dbc.Label("Sex"),
                        dbc.RadioItems(
                            options=[
                                {"label": "Male", "value": 0},
                                {"label": "Female", "value": 1},
                            ],
                            value=1,
                            id="radioitems-sex-input",
                        ),
                    ]
                ),
                dbc.Col(
                    [
                        dbc.Label("Liver Disease"),
                        dbc.RadioItems(
                            options=[
                                {"label": "NAFLD", "value": 0},
                                {"label": "Hep B", "value": 1},
                                {"label": "Hep c", "value": 2},
                                {"label": "Alcohol", "value": 3},
                                {"label": "Others", "value": 4},
                            ],
                            value=3,
                            id="radioitems-liver-disease-input",
                        ),
                    ]
                ),
                dbc.Col(
                    [
                        dbc.Label("No Lesions"),
                        dbc.RadioItems(
                            options=[
                                {"label": ">1", "value": 0},
                                {"label": "<=1", "value": 1},
                            ],
                            value=1,
                            id="radioitems-lesions-input",
                        ),
                    ]
                ),
            ]
        ),
    ],
    style={"margin-left": "5%", "margin-right": "5%", "background": "transparent"},
)
