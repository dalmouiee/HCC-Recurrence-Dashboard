import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

df = pd.read_csv("../../../data/training_data.csv")
df_3 = pd.DataFrame(df["Recurrence"]).head(20)
df_2 = pd.DataFrame(df["DaysToRecurrence"]).head(20)

COLS_TO_DROP = [
    "PlateletCount",
    "CVS",
    "Hypertension",
    "Recurrence",
    "DaysToRecurrence",
]

TABLE_RIGHT_BOUND = 0.898
MAP_1_LEFT_BOUND = 0.9
MAP_1_RIGHT_BOUND = 0.95
MAP_2_LEFT_BOUND = 0.95
MAP_2_RIGHT_BOUND = 1
GRAPH_BOTTOM_BOUND = 0.123
GRAPH_TOP_BOUND = 0.94

GREEN_RED_CMAP = [[0, "rgb(0,255,0)"], [1, "rgb(255,0,0)"]]


df_1 = df.drop(COLS_TO_DROP, axis=1).head(20)


def df_to_plotly(df):
    return {"z": df.values.tolist(), "x": df.columns.tolist(), "y": df.index.tolist()}


fig = make_subplots(rows=1, cols=3)
trace_1 = go.Table(
    header=dict(values=list(df_1.columns), fill_color="paleturquoise", align="left"),
    cells=dict(
        values=[df_1[x] for x in df_1.columns],
        fill_color="lavender",
        align="left",
    ),
    domain=dict(x=[0, TABLE_RIGHT_BOUND], y=[0, 1]),
)

trace_2 = go.Heatmap(df_to_plotly(df_2), xaxis="x1", yaxis="y1")
trace_3 = go.Heatmap(
    df_to_plotly(df_3),
    xaxis="x2",
    yaxis="y2",
    colorscale=GREEN_RED_CMAP,
    showscale=False,
    text=df_3["Recurrence"].astype(str),
    texttemplate="%{text}",
    xgap=1,
    ygap=1,
)

layout = dict(
    xaxis1=dict(
        dict(domain=[MAP_1_LEFT_BOUND, MAP_1_RIGHT_BOUND], anchor="y1", visible=True)
    ),
    xaxis2=dict(
        dict(domain=[MAP_2_LEFT_BOUND, MAP_2_RIGHT_BOUND], anchor="y2", visible=True)
    ),
    yaxis1=dict(
        dict(domain=[GRAPH_BOTTOM_BOUND, GRAPH_TOP_BOUND], anchor="x1", visible=False)
    ),
    yaxis2=dict(
        dict(domain=[GRAPH_BOTTOM_BOUND, GRAPH_TOP_BOUND], anchor="x2", visible=False)
    ),
)
fig = go.Figure(data=[trace_1, trace_2, trace_3], layout=layout)
fig.update_xaxes(tickangle=25)
fig.show()
