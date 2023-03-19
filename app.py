import dash
from dash import dcc, html, Input, Output, dash_table
import pandas as pd
import altair as alt

# Load dataset
df = pd.read_csv("data/cleaned_dataset.csv")


app = dash.Dash(__name__)
app.layout = html.Div(
    [
        html.H2("Recipe Macros"),
        html.Div(
            [
                html.Div(
                    [
                        dcc.Dropdown(
                            id="row-dropdown1",
                            options=[
                                {"label": row, "value": row} for row in df["Food name"]
                            ],
                            placeholder="Select a Food",
                        )
                    ],
                    style={"width": "50%"},
                ),
                dcc.Input(
                    id="multiplier-input1",
                    type="number",
                    placeholder="Weight (Grams)",
                ),
            ],
            style={"display": "flex", "width": "100%"},
        ),
        html.Div(
            [
                html.Div(
                    [
                        dcc.Dropdown(
                            id="row-dropdown2",
                            options=[
                                {"label": row, "value": row} for row in df["Food name"]
                            ],
                            placeholder="Select a Food",
                        )
                    ],
                    style={"width": "50%"},
                ),
                dcc.Input(
                    id="multiplier-input2",
                    type="number",
                    placeholder="Weight (Grams)",
                ),
            ],
            style={"display": "flex", "width": "100%"},
        ),
        html.Div(
            [
                html.Div(
                    [
                        dcc.Dropdown(
                            id="row-dropdown3",
                            options=[
                                {"label": row, "value": row} for row in df["Food name"]
                            ],
                            placeholder="Select a Food",
                        )
                    ],
                    style={"width": "50%"},
                ),
                dcc.Input(
                    id="multiplier-input3",
                    type="number",
                    placeholder="Weight (Grams)",
                ),
            ],
            style={"display": "flex", "width": "100%"},
        ),
        html.Div(
            [
                html.Div(
                    [
                        dcc.Dropdown(
                            id="row-dropdown4",
                            options=[
                                {"label": row, "value": row} for row in df["Food name"]
                            ],
                            placeholder="Select a Food",
                        )
                    ],
                    style={"width": "50%"},
                ),
                dcc.Input(
                    id="multiplier-input4",
                    type="number",
                    placeholder="Weight (Grams)",
                ),
            ],
            style={"display": "flex", "width": "100%"},
        ),
        html.Div(
            [
                html.Div(
                    [
                        dcc.Dropdown(
                            id="row-dropdown5",
                            options=[
                                {"label": row, "value": row} for row in df["Food name"]
                            ],
                            placeholder="Select a Food",
                        )
                    ],
                    style={"width": "50%"},
                ),
                dcc.Input(
                    id="multiplier-input5",
                    type="number",
                    placeholder="Weight (Grams)",
                ),
            ],
            style={"display": "flex", "width": "100%"},
        ),
        dcc.Graph(id="bar-chart"),
        html.H3("Sums"),
        dash_table.DataTable(id="table"),
    ]
)


@app.callback(
    Output("bar-chart", "figure"),
    Output("table", "data"),
    Input("row-dropdown1", "value"),
    Input("row-dropdown2", "value"),
    Input("row-dropdown3", "value"),
    Input("row-dropdown4", "value"),
    Input("row-dropdown5", "value"),
    Input("multiplier-input1", "value"),
    Input("multiplier-input2", "value"),
    Input("multiplier-input3", "value"),
    Input("multiplier-input4", "value"),
    Input("multiplier-input5", "value"),
)
def update_table_plot(
    drop1, drop2, drop3, drop4, drop5, weight1, weight2, weight3, weight4, weight5
):
    filtered_df = pd.DataFrame()
    for input in [
        (drop1, weight1),
        (drop2, weight2),
        (drop3, weight3),
        (drop4, weight4),
        (drop5, weight5),
    ]:
        row = df["Food name"].loc[input[0]]
        row = row / df["Food name"].loc[input[0], "Weight"] * input[1]
        filtered_df = filtered_df.append(row)

    filtered_df = filtered_df[["Protein", "Carbohydrate", "Total Fat", "Energy"]]
    sums = filtered_df.sum()
    chart = (
        alt.Chart(sums.reset_index())
        .mark_bar()
        .encode(
            x="index",
            y="sum",
        )
    )
    return chart.to_html(), sums


if __name__ == "__main__":
    app.run_server(debug=True)
