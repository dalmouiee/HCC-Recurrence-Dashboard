from dash import html
import dash_bootstrap_components as dbc   

filter_card = dbc.Card(
        [   
            dbc.Row([
                dbc.Col([
                    dbc.Label("Age"),
                    dbc.RadioItems(
                    options=[
                        {"label": ">=65", "value": 1},
                        {"label": "<65", "value": 2},
                    ],
                    value=1,
                    id="radioitems-age-input",
                    ),
                ]),
                dbc.Col([
                    dbc.Label("Ethnicity"),
                    dbc.RadioItems(
                    options=[
                        {"label": "Asian", "value": 1},
                        {"label": "Caucasian", "value": 2},
                        {"label": "Others", "value": 3},
                    ],
                    value=1,
                    id="radioitems-ethnicity-input",
                    ),
                ]),
                dbc.Col([
                    dbc.Label("BMI"),
                    dbc.RadioItems(
                    options=[
                        {"label": ">=25", "value": 1},
                        {"label": "<25", "value": 2},
                    ],
                    value=1,
                    id="radioitems-BMI-input",
                    ),
                ]),
                dbc.Col([
                    dbc.Label("Sex"),
                    dbc.RadioItems(
                    options=[
                        {"label": "Male", "value": 1},
                        {"label": "Female", "value": 2},
                    ],
                    value=1,
                    id="radioitems-sex-input",
                    ),
                ]),
                dbc.Col([
                    dbc.Label("Liver Disease"),
                    dbc.RadioItems(
                    options=[
                        {"label": "NAFLD", "value": 1},
                        {"label": "Hep B", "value": 2},
                        {"label": "Hep c", "value": 3},
                        {"label": "Alcohol", "value": 4},
                        {"label": "Others", "value": 5},
                    ],
                    value=3,
                    id="radioitems-liver-disease-input",
                    ),
                ]),
                dbc.Col([
                    dbc.Label("No Lesions"),
                    dbc.RadioItems(
                    options=[
                        {"label": ">1", "value": 1},
                        {"label": "<=1", "value": 2},
                    ],
                    value=1,
                    id="radioitems-sex-input",
                    ),
                ]),
            ]),
          
     
        ],
        style={
            "margin-left": "5%",
            "margin-right": "5%",
            "background": "transparent"
        },
    )