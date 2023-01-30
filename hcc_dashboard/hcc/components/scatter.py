"""
    Module to handle the scatter plot similarity scores graph
"""
from numpy import dot
from numpy.linalg import norm
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from hcc_dashboard.settings import DATA_PATH

COLS_TO_DROP = [
    "PlateletCount",
    "CVS",
    "Hypertension",
    "Recurrence",
    "DaysToRecurrence",
]

COLS_ORDER = [
    "Satellite",
    "eGFR",
    "PriorTACE",
    "AFP",
    "LVI",
    "Ethnicity",
    "Sex",
    "Albumin",
    "No_Lesions",
    "Size",
    "Cirrhosis",
    "BMI",
    "Age",
    "ALT",
    "INR",
    "IHD",
    "DM",
    "LiverDisease",
    "HPVG",
    "Bilirubin",
] + COLS_TO_DROP

TABLE_RIGHT_BOUND = 0.898
MAP_1_LEFT_BOUND = 0.9
MAP_1_RIGHT_BOUND = 0.95
MAP_2_LEFT_BOUND = 0.95
MAP_2_RIGHT_BOUND = 1
MAPS_BOTTOM_BOUND = 0.1
MAPS_TOP_BOUND = 0.94
TABLE_BOTTOM_BOUND = 0

GREEN_RED_CMAP = [[0, "rgb(0,255,0)"], [1, "rgb(255,0,0)"]]


def df_to_plotly(df):  # pylint: disable=invalid-name
    """Function to convert a dataframe to a plotly dictionary

    Args:
        df (pd.DataFrame): pandas dataframe to be converted

    Returns:
        dict: with the following keys:
            - x: list of column names
            - y: list of df indices
            - z: 2D list of all column values
    """
    return {"x": df.columns.tolist(), "y": df.index.tolist(), "z": df.values.tolist()}


def generate_cosine_sim(inputs, n):  # pylint: disable=invalid-name
    """Function to generate the top N Cosine Similarity scores between the
        inference point and machine learning model's training samples

    Args:
        inputs (list): inference point features

    Returns:
        pd.DataFrame: dataframe of the top N similarity scores
    """

    df = (  # pylint: disable=invalid-name
        pd.read_csv(f"{DATA_PATH}/training_data.csv").drop(COLS_TO_DROP, axis=1).T
    )
    df_cos_sim = pd.DataFrame(columns=["patient_id", "cosine_sim"])

    for col in df.columns:
        cos_sim = dot(inputs, df[col]) / (norm(inputs) * norm(df[col]))
        df_temp = pd.DataFrame([col, cos_sim]).T
        df_temp.columns = ["patient_id", "cosine_sim"]
        df_cos_sim = pd.concat([df_cos_sim, df_temp])
    df_cos_sim.patient_id = df_cos_sim.patient_id.astype(int)
    df_cos_sim.cosine_sim = df_cos_sim.cosine_sim.astype(float)
    df_cos_sim = df_cos_sim.reset_index()
    df_cos_sim = df_cos_sim.sort_values(by=["cosine_sim"], ascending=False).head(n)
    return df_cos_sim


def generate_scatter_plot(inputs):
    """Function to generate the scaatter plot of the Cosine Similarity scores

    Args:
        inputs (list): inference point features

    Returns:
        dcc.Figure: the scatterplot figure to be displayed on the dashboard
    """
    df_cos_sim = generate_cosine_sim(inputs, 20)

    fig = px.scatter(
        df_cos_sim,
        x="cosine_sim",
        y="index",
    )

    fig = fig.update_yaxes(visible=False, showticklabels=False)
    fig.update_traces(hoverinfo="none", hovertemplate=None)
    fig.update_traces(
        marker=dict(size=20),
    )
    return fig


def generate_heatmap_plot(inputs):
    """Function to generate the heatmap plot of the Cosine Similarity scores
    with the patient features and recurrence values

    Args:
        inputs (list): inference point features

    Returns:
        dcc.Figure: the figure to be displayed on the dashboard
    """
    df = pd.read_csv(f"{DATA_PATH}/training_data.csv")  # pylint: disable=invalid-name

    df = df.loc[:, COLS_ORDER]  # pylint: disable=invalid-name
    df_cos_sim = generate_cosine_sim(inputs, 20)
    cols = df.columns.to_list()
    cols.append("patient_id")
    cols.append("cosine_sim")

    df_final = pd.DataFrame(columns=cols)
    for idx, row in df_cos_sim.iterrows():
        df_temp = df.filter(items=[idx], axis=0)
        df_temp["cosine_sim"] = row["cosine_sim"]
        df_temp["patient_id"] = row["patient_id"]
        df_final = pd.concat([df_final, df_temp])

    df_3 = pd.DataFrame(df_final["Recurrence"]).rename(columns={"Recurrence": "Recur."})
    df_3 = df_3.reset_index(drop=True)

    df_2 = pd.DataFrame(df_final["cosine_sim"]).rename(
        columns={"cosine_sim": "SimScore"}
    )
    df_2 = df_2.reset_index(drop=True)

    df_1 = df_final.drop(COLS_TO_DROP + ["cosine_sim", "patient_id"], axis=1)

    fig = make_subplots(rows=1, cols=3)
    trace_1 = go.Table(
        header=dict(
            values=list(df_1.columns), fill_color="paleturquoise", align="left"
        ),
        cells=dict(
            values=[df_1[x] for x in df_1.columns],
            fill_color="lavender",
            align="left",
        ),
        domain=dict(x=[0, TABLE_RIGHT_BOUND], y=[TABLE_BOTTOM_BOUND, 1]),
    )

    trace_2 = go.Heatmap(df_to_plotly(df_2), xaxis="x1", yaxis="y1")
    trace_3 = go.Heatmap(
        df_to_plotly(df_3),
        xaxis="x2",
        yaxis="y2",
        colorscale=GREEN_RED_CMAP,
        showscale=False,
        text=df_3["Recur."].astype(str),
        texttemplate="%{text}",
        xgap=1,
        ygap=1,
    )

    layout = dict(
        xaxis1=dict(
            dict(
                domain=[MAP_1_LEFT_BOUND, MAP_1_RIGHT_BOUND],
                anchor="y1",
                visible=True,
            )
        ),
        xaxis2=dict(
            dict(
                domain=[MAP_2_LEFT_BOUND, MAP_2_RIGHT_BOUND],
                anchor="y2",
                visible=True,
            )
        ),
        yaxis1=dict(
            dict(
                domain=[MAPS_BOTTOM_BOUND, MAPS_TOP_BOUND],
                anchor="x1",
                visible=False,
                autorange="reversed",
            )
        ),
        yaxis2=dict(
            dict(
                domain=[MAPS_BOTTOM_BOUND, MAPS_TOP_BOUND],
                anchor="x2",
                visible=False,
                autorange="reversed",
            )
        ),
        margin=go.layout.Margin(
            l=5,  # left margin
            r=0,  # right margin
            b=0,  # bottom margin
            t=5,  # top margin
        ),
        height=480,
    )
    fig = go.Figure(data=[trace_1, trace_2, trace_3], layout=layout)
    fig.update_xaxes(tickangle=15)
    return fig
