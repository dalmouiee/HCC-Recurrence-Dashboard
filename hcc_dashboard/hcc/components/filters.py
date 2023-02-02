"""
    Module to handle the filters
"""
from dash import html
import dash_bootstrap_components as dbc

filter_card = html.Div(
    [
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        dbc.Row(
                            [
                                dbc.Row(
                                    [
                                        html.H4(
                                            "Demographics",
                                            style={"font-weight": "bold"},
                                        )
                                    ]
                                ),
                                dbc.Row(
                                    html.Hr(
                                        style={"border-width": "6px", "width": "90%"}
                                    ),
                                ),
                                html.Br(),
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
                            ]
                        ),
                        html.Hr(style={"border-width": "6px"}),
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Row(
                                    [
                                        html.H4(
                                            "Metabolic", style={"font-weight": "bold"}
                                        )
                                    ]
                                ),
                                dbc.Row(
                                    html.Hr(
                                        style={"border-width": "6px", "width": "90%"}
                                    ),
                                ),
                                html.Br(),
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
                                        dbc.Label("eGFR"),
                                        dbc.RadioItems(
                                            options=[
                                                {"label": ">=90", "value": 0},
                                                {"label": "<90", "value": 1},
                                            ],
                                            value=1,
                                            id="radioitems-egfr-input",
                                        ),
                                    ]
                                ),
                                dbc.Col(
                                    [
                                        dbc.Label("IHD"),
                                        dbc.RadioItems(
                                            options=[
                                                {"label": "Yes", "value": 0},
                                                {"label": "No", "value": 1},
                                            ],
                                            value=1,
                                            id="radioitems-ihd-input",
                                        ),
                                    ]
                                ),
                                dbc.Col(
                                    [
                                        dbc.Label("type II DM"),
                                        dbc.RadioItems(
                                            options=[
                                                {"label": "Yes", "value": 0},
                                                {"label": "No", "value": 1},
                                            ],
                                            value=1,
                                            id="radioitems-dm-input",
                                        ),
                                    ]
                                ),
                            ]
                        ),
                        html.Hr(style={"border-width": "6px"}),
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Row(
                                    [html.H4("Tumor", style={"font-weight": "bold"})]
                                ),
                                dbc.Row(
                                    html.Hr(
                                        style={"border-width": "6px", "width": "90%"}
                                    ),
                                ),
                                html.Br(),
                                dbc.Col(
                                    [
                                        dbc.Label("Lymphovascular invasion"),
                                        dbc.RadioItems(
                                            options=[
                                                {"label": "Yes", "value": 0},
                                                {"label": "No", "value": 1},
                                            ],
                                            value=1,
                                            id="radioitems-lympho_vasc-input",
                                        ),
                                    ]
                                ),
                                dbc.Col(
                                    [
                                        dbc.Label("Prior TACE"),
                                        dbc.RadioItems(
                                            options=[
                                                {"label": "Yes", "value": 0},
                                                {"label": "No", "value": 1},
                                            ],
                                            value=1,
                                            id="radioitems-pr_tace-input",
                                        ),
                                    ]
                                ),
                                dbc.Col(
                                    [
                                        dbc.Label("Satellite"),
                                        dbc.RadioItems(
                                            options=[
                                                {"label": "Yes", "value": 0},
                                                {"label": "No", "value": 1},
                                            ],
                                            value=1,
                                            id="radioitems-satellite-input",
                                        ),
                                    ]
                                ),
                                dbc.Col(
                                    [
                                        dbc.Label("Size of Lesion (cm)"),
                                        dbc.RadioItems(
                                            options=[
                                                {"label": ">=5", "value": 0},
                                                {"label": "<5", "value": 1},
                                            ],
                                            value=1,
                                            id="radioitems-lesion_size-input",
                                        ),
                                    ]
                                ),
                            ]
                        ),
                        html.Hr(style={"border-width": "6px"}),
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Row(
                                    [html.H4("Liver", style={"font-weight": "bold"})]
                                ),
                                dbc.Row(
                                    html.Hr(
                                        style={"border-width": "6px", "width": "90%"}
                                    ),
                                ),
                                html.Br(),
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
                                dbc.Col(
                                    [
                                        dbc.Label("Cirrhosis"),
                                        dbc.RadioItems(
                                            options=[
                                                {"label": "Yes", "value": 0},
                                                {"label": "No", "value": 1},
                                            ],
                                            value=1,
                                            id="radioitems-cirr-input",
                                        ),
                                    ]
                                ),
                                dbc.Col(
                                    [
                                        dbc.Label("Bilirubin"),
                                        dbc.RadioItems(
                                            options=[
                                                {"label": ">20", "value": 0},
                                                {"label": "<=20", "value": 1},
                                            ],
                                            value=1,
                                            id="radioitems-bilirubin-input",
                                        ),
                                    ]
                                ),
                                dbc.Col(
                                    [
                                        dbc.Label("Albumin"),
                                        dbc.RadioItems(
                                            options=[
                                                {"label": ">=35", "value": 0},
                                                {"label": "<35", "value": 1},
                                            ],
                                            value=1,
                                            id="radioitems-albumin-input",
                                        ),
                                    ]
                                ),
                                dbc.Col(
                                    [
                                        dbc.Label("HPVG"),
                                        dbc.RadioItems(
                                            options=[
                                                {"label": ">5", "value": 0},
                                                {"label": "<=5", "value": 1},
                                            ],
                                            value=1,
                                            id="radioitems-hpvg-input",
                                        ),
                                    ]
                                ),
                                dbc.Col(
                                    [
                                        dbc.Label("AFP"),
                                        dbc.RadioItems(
                                            options=[
                                                {"label": ">100", "value": 0},
                                                {"label": ">8 & <=100", "value": 1},
                                                {"label": "<=8", "value": 2},
                                            ],
                                            value=2,
                                            id="radioitems-afp-input",
                                        ),
                                    ]
                                ),
                                dbc.Col(
                                    [
                                        dbc.Label("ALT"),
                                        dbc.RadioItems(
                                            options=[
                                                {"label": ">50", "value": 0},
                                                {"label": "<=50", "value": 1},
                                            ],
                                            value=1,
                                            id="radioitems-alt-input",
                                        ),
                                    ]
                                ),
                                dbc.Col(
                                    [
                                        dbc.Label("INR"),
                                        dbc.RadioItems(
                                            options=[
                                                {"label": ">1.1", "value": 0},
                                                {"label": "<=1.1", "value": 1},
                                            ],
                                            value=1,
                                            id="radioitems-inr-input",
                                        ),
                                    ]
                                ),
                            ]
                        ),
                    ]
                ),
            ],
            style={"background": "transparent"},
        ),
    ]
)
