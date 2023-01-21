from dash import dcc, html
from dash.dependencies import Input, Output, State
from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

from .utils.reproduce_best_model import pipeline
from .components.banner import first_card, second_card, third_card
from .components.scatter import generate_scatter_plot, generate_cosine_sim

from .components.filters import filter_card

app = DjangoDash(
    "HccDashboard", add_bootstrap_links=True, external_stylesheets=[dbc.themes.QUARTZ]
)
app.layout = html.Div(
    [
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("Github", href="#")),
                dbc.NavItem(dbc.NavLink("VLAB", href="#")),
            ],
            brand="HCC DASHBOARD",
            brand_href="#",
            color="#BF40BF",
            dark=True,
        ),
        html.Br(),
        dbc.Button(
            "Toggle filters",
            id="collapse-button",
            style={"background-color": "DeepPink"},
            n_clicks=0,
        ),
        html.Br(),
        dbc.Collapse(
            [
                html.Br(),
                filter_card],
            id="collapse",
            is_open=True,
        ),
        html.Br(),
        dbc.Row([
            dbc.Col([
                dbc.Button("Predict HCC Recurrence", id="predict-btn"),
            ]),
            dbc.Col([
                third_card,
            ], width=9)
        ]),
        html.Br(),
        dcc.Loading(
            html.Div(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    first_card,
                                    html.Br(),
                                    second_card,
                                ],
                                width=3,
                            ),
                            dbc.Col(dcc.Graph(id="scatter-fig"), width=9),
                        ],
                        style={"width": "100%", "margin": "auto"},
                    ),
                    html.Br(),
                ],
                id="predict-output",
            ),
            id="predict-loading",
            style={"width": "100%", "margin": "auto"},
        ),
        # html.Br(),
        # dbc.Button("Predict HCC Recurrence", id="predict-btn"),
        html.Br(),
    ],
    style={"width": "95%", "margin": "auto"},
)


@app.callback(
    [
        Output("card-1-percent-rec", "children"),
        Output("card-2-percent-non-rec", "children"),
        Output("scatter-fig", "figure"),
    ],
    [
        Input("predict-btn", "n_clicks"),
    ],
    [
        State("radioitems-age-input", "value"),
        State("radioitems-ethnicity-input", "value"),
        State("radioitems-BMI-input", "value"),
        State("radioitems-sex-input", "value"),
        State("radioitems-liver-disease-input", "value"),
        State("radioitems-lesions-input", "value"),
        State("radioitems-satellite-input", "value"),
        State("radioitems-lympho_vasc-input", "value"),
        State("radioitems-cirr-input", "value"),
        State("radioitems-dm-input", "value"),
        State("radioitems-ihd-input", "value"),
        State("radioitems-pr_tace-input", "value"),
        State("radioitems-inr-input", "value"),
        State("radioitems-albumin-input", "value"),
        State("radioitems-afp-input", "value"),
        State("radioitems-hpvg-input", "value"),
        State("radioitems-alt-input", "value"),
        State("radioitems-egfr-input", "value"),
        State("radioitems-bilirubin-input", "value"),
        State("radioitems-lesion_size-input", "value"),
    ],
    prevent_initial_call=True,
)
def predict(_, *inputs):
    print(inputs)
    res = pipeline(inputs)[0]

    fig = generate_scatter_plot(inputs)

    return f"{res[0]:.2f}%", f"{res[1]:.2f}%", fig



@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("card-3-label-datapoint-info", "children"),
    Input("scatter-fig", "hoverData"),
    [
        State("radioitems-age-input", "value"),
        State("radioitems-ethnicity-input", "value"),
        State("radioitems-BMI-input", "value"),
        State("radioitems-sex-input", "value"),
        State("radioitems-liver-disease-input", "value"),
        State("radioitems-lesions-input", "value"),
        State("radioitems-satellite-input", "value"),
        State("radioitems-lympho_vasc-input", "value"),
        State("radioitems-cirr-input", "value"),
        State("radioitems-dm-input", "value"),
        State("radioitems-ihd-input", "value"),
        State("radioitems-pr_tace-input", "value"),
        State("radioitems-inr-input", "value"),
        State("radioitems-albumin-input", "value"),
        State("radioitems-afp-input", "value"),
        State("radioitems-hpvg-input", "value"),
        State("radioitems-alt-input", "value"),
        State("radioitems-egfr-input", "value"),
        State("radioitems-bilirubin-input", "value"),
        State("radioitems-lesion_size-input", "value"),
    ],
)
def show_info(info, *filters):
    print(info)
    df = generate_cosine_sim(filters)
    pat_id = df[df["cosine_sim"] == info["points"][0]["x"]]["patient_id"]
    
    return pat_id