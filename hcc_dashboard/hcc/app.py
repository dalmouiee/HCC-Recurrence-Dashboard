from dash import html
from django_plotly_dash import DjangoDash

app = DjangoDash("HccDashboard")
app.layout = html.Div([html.H3("HCC Dashboard")])
