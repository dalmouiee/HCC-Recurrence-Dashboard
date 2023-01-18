from dash import dcc, html
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

from .utils.reproduce_best_model import pipeline


app = DjangoDash("HccDashboard", add_bootstrap_links=True)
app.layout = html.Div(
    [
        html.H3("HCC Dashboard"),
        dcc.Loading(html.Div(id="predict-output"), id="predict-loading"),
        dbc.Button("Predict HCC Recurrence", id="predict-btn"),
    ]
)


@app.callback(
    [Output("predict-loading", "children")],
    [Input("predict-btn", "n_clicks")],
    prevent_initial_call=True,
)
def predict(_):
    return pipeline()
