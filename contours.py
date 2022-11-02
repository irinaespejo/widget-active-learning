from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

# Marks for sliders
mdm_list = [100, 200, 500, 1000, 1200]
gx_list = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]

# Theme
app = Dash(__name__, external_stylesheets=[dbc.themes.LUMEN])

# Layout
app.layout = html.Div(
    [
        # Title
        html.H1(
            children=dcc.Markdown(
                "Active Learning for Mono-H($b\\bar{b}$) search", mathjax=True
            ),
            className="text-center p-3",
            style={"color": "black"},
        ),
        html.H2(
            children="Visualize the 4D exclusion contour",
            className="text-center p-3",
            style={"color": "black"},
        ),
        dbc.Label(style={"margin-left": "600px"}),
        dbc.Label(dcc.Markdown("$\mathrm{M}_\chi\,\,\mathrm{[GeV]}$", mathjax=True)),
        # First slider
        html.Div(
            [
                dcc.Slider(
                    100,
                    1200,
                    step=None,
                    value=100,
                    marks={
                        int(mdm) if mdm % 1 == 0 else mdm: "{}".format(mdm)
                        for mdm in mdm_list
                    },
                    id="mdm-slider",
                    vertical=False,
                )
            ],
            style={"padding-left": "40%", "padding-right": "0%"},
        ),
        dbc.Label(style={"margin-left": "600px"}),
        html.Label(dcc.Markdown("$g_\chi$", mathjax=True)),
        html.Div(
            [
                # Second slider
                dcc.Slider(
                    0.5,
                    2.0,
                    step=None,
                    value=0.5,
                    marks={
                        int(gx) if gx % 1 == 0 else gx: "{}".format(gx)
                        for gx in gx_list
                    },
                    id="gx-slider",
                    vertical=False,
                )
            ],
            style={"padding-left": "40%", "padding-right": "0%"},
        ),
        # The image
        html.Div(
            [html.Img(id="graph-with-slider", style={"height": "50%", "width": "50%"})],
            style={"textAlign": "center"},
            id="plot_div",
        ),
    ]
)


@app.callback(
    Output("graph-with-slider", "src"),
    [Input("gx-slider", "value"), Input("mdm-slider", "value")],
)

# Plot on the fly a plot for the current slider configuration
# Just load an image where the model has been pre-evaluated
def update_figure(gx, mdm):

    if type(gx) == int:  # freaking bug in dash
        image_file = f"assets/m_{mdm}_gx_{gx}.0.jpg"
    else:
        image_file = f"assets/m_{mdm}_gx_{gx}.jpg"

    return image_file


if __name__ == "__main__":
    app.run_server(debug=True)
