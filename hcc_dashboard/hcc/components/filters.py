from dash import html
import dash_bootstrap_components as dbc

filter_card = html.Div([
    dbc.Card(
        [      
        dbc.CardBody([    
            dbc.Row([
                dbc.Col([
                    dbc.Label("Satellite"), 
                    dbc.Checklist(
                    options=[
                        {"value": 1},
                    ],
                    value=1,
                    id="satellite_switches",
                    switch=True,
                    inline=True,
                    ),
                ]),
                dbc.Col([
                    dbc.Label("Lymphovascular invasion"), 
                    dbc.Checklist(
                    options=[
                        {"value": 1},
                    ],
                    value=1,
                    id="lympho_vasc_switches",
                    switch=True,
                    inline=True,
                    ),
                ]),
                dbc.Col([
                    dbc.Label("Cirrhosis"), 
                    dbc.Checklist(
                    options=[
                        {"value": 1},
                    ],
                    value=1,
                    id="cirr_switches",
                    switch=True,
                    inline=True,
                    ),
                ]),
                dbc.Col([
                    dbc.Label("DM"), 
                    dbc.Checklist(
                    options=[
                        {"value": 1},
                    ],
                    value=1,
                    id="dm_switches",
                    switch=True,
                    inline=True,
                    ),
                ]),
                dbc.Col([
                    dbc.Label("IHD"), 
                    dbc.Checklist(
                    options=[
                        {"value": 1},
                    ],
                    value=1,
                    id="ihd_switches",
                    switch=True,
                    inline=True,
                    ),
                ]),
                dbc.Col([
                    dbc.Label("Prior TACE"), 
                    dbc.Checklist(
                    options=[
                        {"value": 1},
                    ],
                    value=1,
                    id="pr_tace_switches",
                    switch=True,
                    inline=True,
                    ),
                ]),
            ]),
            html.Hr(style={"border-width": "6px"}),
            html.Br(),
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
                dbc.Col([
                    dbc.Label("INR"),
                    dbc.RadioItems(
                    options=[
                        {"label": ">1.1", "value": 1},
                        {"label": "<=1.1", "value": 2},
                    ],
                    value=1,
                    id="radioitems-inr-input",
                    ),
                ]), 
            ]),
            html.Hr(style={"border-width": "6px"}),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    dbc.Label("Albumin"),
                    dbc.RadioItems(
                    options=[
                        {"label": ">=35", "value": 1},
                        {"label": "<35", "value": 2},
                    ],
                    value=2,
                    id="radioitems-albumin-input",
                    ),
                ]), 
                dbc.Col([
                    dbc.Label("AFP"),
                    dbc.RadioItems(
                    options=[
                        {"label": ">100", "value": 1},
                        {"label": ">8 & <=100", "value": 2},
                        {"label": "<=8", "value": 3},
                    ],
                    value=2,
                    id="radioitems-afp-input",
                    ),
                ]),
                dbc.Col([
                    dbc.Label("HPVG"),
                    dbc.RadioItems(
                    options=[
                        {"label": ">5", "value": 1},
                        {"label": "<=5", "value": 2},
                    ],
                    value=2,
                    id="radioitems-hpvg-input",
                    ),
                ]),
                dbc.Col([
                    dbc.Label("ALT"),
                    dbc.RadioItems(
                    options=[
                        {"label": ">50", "value": 1},
                        {"label": "<=50", "value": 2},
                    ],
                    value=1,
                    id="radioitems-alt-input",
                    ),
                ]),
                dbc.Col([
                    dbc.Label("eGFR"),
                    dbc.RadioItems(
                    options=[
                        {"label": ">=90", "value": 1},
                        {"label": "<90", "value": 2},
                    ],
                    value=1,
                    id="radioitems-egfr-input",
                    ),
                ]),
                dbc.Col([
                    dbc.Label("Bilirubin"),
                    dbc.RadioItems(
                    options=[
                        {"label": ">20", "value": 1},
                        {"label": "<=20", "value": 2},
                    ],
                    value=1,
                    id="radioitems-bilirubin-input",
                    ),
                ]),
                dbc.Col([
                    dbc.Label("Size of Lesion (cm)"),
                    dbc.RadioItems(
                    options=[
                        {"label": ">=5", "value": 1},
                        {"label": "<5", "value": 2},
                    ],
                    value=1,
                    id="radioitems-lesion_size-input",
                    ),
                ]),
            ]),
        ]), 
        ],
        style={
            "margin-left": "3%",
            "margin-right": "3%",
            "background": "transparent"
        },
    ), 
])
