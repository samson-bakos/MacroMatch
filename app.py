import dash
from dash import dcc, html, Input, Output, dash_table
import pandas as pd
import altair as alt
import dash_bootstrap_components as dbc

# Load dataset
df = pd.read_csv("data/cleaned_dataset.csv", index_col=0)


app = dash.Dash(external_stylesheets=[dbc.themes.SANDSTONE])
app.layout = html.Div(
    [
        html.H1("MacroMatch"),
        html.Div(style={"height": "10px"}),
        html.H4("Enter Recipe Foods + Amounts in Grams"),
        html.Div(
            [
                html.Div(
                    [
                        dcc.Dropdown(
                            id="row-dropdown1",
                            options=[
                                {"label": row, "value": row} for row in df["Food name"]
                            ],
                            value="Deli meat, chicken breast, low fat",
                        )
                    ],
                    style={"width": "50%"},
                ),
                dcc.Input(
                    id="multiplier-input1",
                    type="number",
                    placeholder="Weight (Grams)",
                    value=100,
                ),
                dcc.Markdown("grams"),
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
                            value="Bread, rye",
                        )
                    ],
                    style={"width": "50%"},
                ),
                dcc.Input(
                    id="multiplier-input2",
                    type="number",
                    placeholder="Weight (Grams)",
                    value=100,
                ),
                dcc.Markdown("grams"),
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
                            value="Mustard",
                        )
                    ],
                    style={"width": "50%"},
                ),
                dcc.Input(
                    id="multiplier-input3",
                    type="number",
                    placeholder="Weight (Grams)",
                    value=20,
                ),
                dcc.Markdown("grams"),
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
                            value="Ketchup",
                        )
                    ],
                    style={"width": "50%"},
                ),
                dcc.Input(
                    id="multiplier-input4",
                    type="number",
                    placeholder="Weight (Grams)",
                    value=20,
                ),
                dcc.Markdown("grams"),
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
                            value="Pickles, cucumber, dill",
                        )
                    ],
                    style={"width": "50%"},
                ),
                dcc.Input(
                    id="multiplier-input5",
                    type="number",
                    placeholder="Weight (Grams)",
                    value=30,
                ),
                dcc.Markdown("grams"),
            ],
            style={"display": "flex", "width": "100%"},
        ),
        html.Div(style={"height": "35px"}),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.H4("Macros: Plot"),
                        html.Iframe(id="bar-chart", width="100%", height="500px"),
                    ],
                    style={"width": "50%", "float": "left"},
                ),
                html.Div(
                    children=[
                        html.H4("Macros: Numeric Sums"),
                        dash_table.DataTable(id="table"),
                    ],
                    style={"width": "50%", "float": "right"},
                ),
            ],
            style={"max-width": "1200px", "margin": "auto"},
        ),
    ]
)


@app.callback(
    Output("bar-chart", "srcDoc"),
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
    if (
        drop1 is not None
        and drop2 is not None
        and drop3 is not None
        and drop4 is not None
        and drop5 is not None
        and weight1 is not None
        and weight2 is not None
        and weight3 is not None
        and weight4 is not None
        and weight5 is not None
    ):
        filtered_df = pd.DataFrame(
            columns=["Protein", "Carbohydrate", "Total Fat", "Energy"]
        )
        for name, weight in zip(
            [drop1, drop2, drop3, drop4, drop5],
            [weight1, weight2, weight3, weight4, weight5],
        ):

            row = df[df["Food name"] == name]
            row = row[["Protein", "Carbohydrate", "Total Fat", "Energy"]]
            row = row / df[df["Food name"] == name].iloc[0]["Weight"] * weight
            filtered_df = filtered_df.append(row)

        sums = pd.DataFrame(filtered_df.sum()).T
        sums = sums.rename(columns={"Total Fat": "Fat"})

        macros = sums.drop(["Energy"], axis=1)
        melted_macros = macros.melt(var_name="Nutrient")

        sums = sums.rename(
            columns={
                "Protein": "Protein (grams)",
                "Carbohydrate": "Carbs (grams)",
                "Fat": "Fat (grams)",
                "Energy": "Energy (kcal)",
            }
        )

        chart = (
            alt.Chart(melted_macros)
            .mark_bar()
            .encode(
                x=alt.X("Nutrient", sort="-y"),
                y=alt.Y("value", title="Grams"),
                color="Nutrient",
            )
        ).properties(width=400)

        data = sums.round(1).to_dict("records")

        return chart.to_html(), data


if __name__ == "__main__":
    app.run_server(debug=True)
