from dash import dash, html, dcc, Input, Output


app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.H1("MacroMatch"),
        "Enter Your First Recipe",
        dcc.Dropdown(
            options=["NYC", "MTL", "SF", "None"],
            value="None",
            placeholder="Enter Food",
        ),
        dcc.Dropdown(
            options=["NYC", "MTL", "SF", "None"],
            value="None",
            placeholder="Enter Food",
        ),
        dcc.Dropdown(
            options=["NYC", "MTL", "SF", "None"],
            value="None",
            placeholder="Enter Food",
        ),
        dcc.Dropdown(
            options=["NYC", "MTL", "SF", "None"],
            value="None",
            placeholder="Enter Food",
        ),
        dcc.Dropdown(
            options=["NYC", "MTL", "SF", "None"],
            value="None",
            placeholder="Enter Food",
        ),
        "Enter Your Second Recipe",
        dcc.Dropdown(
            options=["NYC", "MTL", "SF", "None"],
            value="None",
            placeholder="Enter Food",
        ),
        dcc.Dropdown(
            options=["NYC", "MTL", "SF", "None"],
            value="None",
            placeholder="Enter Food",
        ),
        dcc.Dropdown(
            options=["NYC", "MTL", "SF", "None"],
            value="None",
            placeholder="Enter Food",
        ),
        dcc.Dropdown(
            options=["NYC", "MTL", "SF", "None"],
            value="None",
            placeholder="Enter Food",
        ),
        dcc.Dropdown(
            options=["NYC", "MTL", "SF", "None"],
            value="None",
            placeholder="Enter Food",
        ),
    ]
)
if __name__ == "__main__":
    app.run_server(debug=True)
