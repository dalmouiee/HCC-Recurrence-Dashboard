"""
    HCC Dashboard style layout
"""
import tempfile

from dash import dcc, html
from dash.dependencies import Input, Output, State
from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.io as pio

from .utils.reproduce_best_model import pipeline
from .components.banner import rec_card, non_rec_card
from .components.scatter import (
    generate_heatmap_plot,
)

from .components.filters import filter_card

app = DjangoDash(
    "HccDashboard", add_bootstrap_links=True, external_stylesheets=[dbc.themes.LUMEN]
)
app.layout = html.Div(
    [
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(
                    dbc.NavLink(
                        "Github",
                        href="https://github.com/VafaeeLab/HCC-Recurrence",
                        style={"color": "white"},
                    )
                ),
                dbc.NavItem(
                    dbc.NavLink(
                        "Vafaee lab",
                        href="http://vafaeelab.com/",
                        style={"color": "white"},
                    )
                ),
            ],
            brand="AI predictor of HCC Recurrence Post-Resection",
            brand_style={"color": "white"},
            brand_href="#",
            color="#042749",
        ),
        html.Br(),
        html.P(
            """This dashboard is a Graphical User Interface (GUI) for the model described
            in the following paper: 'Artificial intelligence reliably identifies patients
            at risk of HCC recurrence one-year post-surgical resection'."""
        ),
        html.Div(
            [
                html.Img(
                    src="../static/website-img.gif",
                ),
            ],
            style={"padding-left": "20%"},
        ),
        html.Br(),
        dbc.Button(
            "Toggle filters",
            id="collapse-button",
            style={"background-color": "#18bdc2", "border": "2px solid #042749"},
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
                        dbc.Button(
                            "Predict HCC Recurrence",
                            id="predict-btn",
                            style={
                                "background-color": "#042749",
                                "border": "2px solid white",
                            },
                        ),
                    ],
                    width=2,
                ),
                dbc.Col(
                    dcc.Loading(html.Div(id="placeholder-loading"), id=""), width=2
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
                                ],
                                width=5,
                            ),
                            dbc.Col(
                                [
                                    rec_card,
                                ],
                                width=5,
                            ),
                            dbc.Col(
                                dbc.Button(
                                    "Download Plot",
                                    id="btn_image",
                                    style={
                                        "visibility": "hidden",
                                        "background-color": "#18bdc2",
                                        "border": "2px solid #042749",
                                    },
                                ),
                            ),
                        ],
                        style={"width": "100%", "margin": "auto"},
                    ),
                    html.Br(),
                    html.P(id="description_graph"),
                    html.Div(
                        dcc.Graph(id="scatter-fig", style={"visibility": "hidden"}),
                    ),
                    html.Br(),
                ],
                id="predict-output",
            ),
            id="predict-loading",
            style={"width": "100%", "margin": "auto"},
        ),
        html.Br(),
        dcc.Download(id="download-image"),
    ],
    style={"width": "95%", "margin": "auto"},
)


@app.callback(
    [
        Output("card-1-percent-rec", "children"),
        Output("card-2-percent-non-rec", "children"),
        Output("scatter-fig", "figure"),
        Output("scatter-fig", "style"),
        Output("description_graph", "children"),
        Output("btn_image", "style"),
    ],
    [
        Input("predict-btn", "n_clicks"),
    ],
    [
        State("radioitems-satellite-input", "value"),
        State("radioitems-egfr-input", "value"),
        State("radioitems-pr_tace-input", "value"),
        State("radioitems-afp-input", "value"),
        State("radioitems-lympho_vasc-input", "value"),
        State("radioitems-ethnicity-input", "value"),
        State("radioitems-sex-input", "value"),
        State("radioitems-albumin-input", "value"),
        State("radioitems-lesions-input", "value"),
        State("radioitems-lesion_size-input", "value"),
        State("radioitems-cirr-input", "value"),
        State("radioitems-BMI-input", "value"),
        State("radioitems-age-input", "value"),
        State("radioitems-alt-input", "value"),
        State("radioitems-inr-input", "value"),
        State("radioitems-ihd-input", "value"),
        State("radioitems-dm-input", "value"),
        State("radioitems-liver-disease-input", "value"),
        State("radioitems-hpvg-input", "value"),
        State("radioitems-bilirubin-input", "value"),
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
    desc = """
    This plot shows the top 20 patients in the development cohort whose clinical variables are 
    most similar to the queried patient using the cosine similarity metric.
    """

    rec_score = f"{res[0]*100:.2f}"
    non_rec_score = f"{(100 - float(rec_score)):.2f}"

    return (
        f"{rec_score}%",
        f"{non_rec_score}%",
        fig,
        {},
        desc,
        {"background-color": "#18bdc2", "border": "2px solid #042749"},
    )


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
    [
        Output("download-image", "data"),
        Output("placeholder-loading", "children"),
    ],
    [
        Input("btn_image", "n_clicks"),
    ],
    State("scatter-fig", "figure"),
    prevent_initial_call=True,
)
def download_plot_to_pdf(_, fig):
    """Function to download the main plot figure to a PDF file to the client's
        machine

    Args:
        _ (dbc.Button.n_clicks): the "Download Plot" button nclicks attribute that
        triggers the callback
        fig (plotly.graph_objects.Figure): Plotly figure that will be downloaded

    Returns:
        dcc.Download.data : the plot that will be sent ot the Download component
        for eventual downloading
    """

    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=True) as temp_file:
        temp_fig = go.Figure(fig)
        pio.write_image(temp_fig, temp_file.name, height=780, width=1200)
        return dcc.send_file(temp_file.name), ""
