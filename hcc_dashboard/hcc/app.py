from dash import dcc, html
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

from .utils.reproduce_best_model import pipeline
from .components.banner import first_card, second_card
from .components.scatter import generate_scatter_plot

from .components.filters import filter_card

app = DjangoDash(
    "HccDashboard", add_bootstrap_links=True, external_stylesheets=[dbc.themes.QUARTZ]
)
app.layout = html.Div(
    [
        html.H3("HCC Dashboard"),
        html.Br(),
        dcc.Loading(
            html.Div(
                [
                    dbc.Row(
                        [
                            dbc.Col(first_card, width=6),
                            dbc.Col(second_card, width=6),
                        ],
                        style={"width": "100%", "margin": "auto"},
                    ),
                    html.Br(),
                    dbc.Row([dcc.Graph(figure=generate_scatter_plot())]),
                ],
                id="predict-output",
            ),
            id="predict-loading",
        ),
        html.Br(),
        dbc.Button("Predict HCC Recurrence", id="predict-btn"),
        html.Br(),
        filter_card,
    ]
)


@app.callback(
    [
        Output("card-1-percent-rec", "children"),
        Output("card-2-percent-non-rec", "children"),
    ],
    [Input("predict-btn", "n_clicks")],
    prevent_initial_call=True,
)
def predict(_):
    res = pipeline()[0]
    return f"{res[0]}%", f"{res[1]}%"
