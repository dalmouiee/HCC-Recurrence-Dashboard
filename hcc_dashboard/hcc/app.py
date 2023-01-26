"""
    HCC Dashboard style layout
"""
from dash import dcc, html
from dash.dependencies import Input, Output, State
from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

from .utils.reproduce_best_model import pipeline
from .components.banner import rec_card, non_rec_card, pat_info_card
from .components.scatter import (
    generate_cosine_sim,
    generate_heatmap_plot,
)

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
            [html.Br(), filter_card],
            id="collapse",
            is_open=True,
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Button("Predict HCC Recurrence", id="predict-btn"),
                    ]
                ),
                dbc.Col(
                    [
                        pat_info_card,
                    ],
                    width=9,
                ),
            ]
        ),
        html.Br(),
        dcc.Loading(
            html.Div(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    non_rec_card,
                                    html.Br(),
                                    rec_card,
                                ],
                                width=3,
                            ),
                            dbc.Col(
                                dcc.Graph(id="scatter-fig"),
                                width=9,
                                style={"height": "500px"},
                            ),
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
def infer_model(_, *inputs):
    """Callback to run the Machine Learning model inference on a datapoint instance from the
        dashboard

    Args:
        _ (int): n_clicks of the button that triggers the callback (not necessary)
        *inputs (list): list of filter inputs that is passed to the machine learning model inference

    Returns:
        str: Probablity of tumour recurrence
        str: Probablity of tumour non-recurrence
        dcc.graph.figure: scatterplot to be displayed on the dashboard
    """
    res = pipeline(inputs)[0]

    fig = generate_heatmap_plot(inputs)

    return f"{(res[0]*100):.2f}%", f"{(res[1]*100):.2f}%", fig


@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):  # pylint: disable=invalid-name
    """Callback to toggle the filter container display

    Args:
        n (int): toggle button n_clicks
        is_open (bool): checks if the dislplayed is shown or not

    Returns:
        bool: flips the state of the toggle depending on the input
    """
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
    prevent_initial_call=True,
)
def show_info(info, *filters):
    """Callback to show the patient information when hovering over the scatterplot datapoint

    Args:
        info (dict): dictonary that contains the hover information of the datapoint
        *filters (list): list of filter inputs that is passed to generate the cosine similarity
            scores

    Returns:
        str: patient features to be shown in info card
    """
    df = generate_cosine_sim(filters, 20)  # pylint: disable=invalid-name
    pat_id = df[df["cosine_sim"] == info["points"][0]["x"]]["patient_id"]

    return pat_id
