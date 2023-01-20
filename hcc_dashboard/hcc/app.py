from dash import dcc, html
from dash.dependencies import Input, Output, State
from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

from .utils.reproduce_best_model import pipeline
from .components.banner import first_card, second_card, third_card
from .components.scatter import generate_scatter_plot

from .components.filters import filter_card

app = DjangoDash(
    "HccDashboard", add_bootstrap_links=True, external_stylesheets=[dbc.themes.QUARTZ]
)
app.layout = html.Div(
    [
        html.H3("HCC Dashboard"),
        html.Br(),
        filter_card,
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
                                    html.Br(),
                                    third_card,
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
        ),
        html.Br(),
        dbc.Button("Predict HCC Recurrence", id="predict-btn"),
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
    ],
    prevent_initial_call=True,
)
def predict(_, age, ethnic, bmi, sex, liver, lesion):
    inputs = [age, ethnic, bmi, sex, liver, lesion]
    res = pipeline(inputs)[0]

    fig = generate_scatter_plot(inputs)

    return f"{res[0]:.2f}%", f"{res[1]:.2f}%", fig
