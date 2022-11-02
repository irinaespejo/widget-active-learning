from email.mime import image
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import numpy as np
from skimage import io
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import sys
import matplotlib.pyplot as plt
import mycode
from mycode.plotting import snapPlot
import base64
import plotly
mdm_list = [100,200,500,1000,1200]
PATH = "/Users/irinaespejo/Documents/AL_Exotics_notebooks/gifs/1/"

colors = {
    'black' : '#1A1B25',
    'red' : '#F8C271E',
    'white' : '#EFE9E7',
    'background' : '#333333',
    'text' : '#FFFFFF'
}
plot_dict={
    'contours': {"exp": ['reco4'],
                 "obs": ['reco4']
                }, 
    'suggestions': [],
    'sigma': {'reco4': 1}, 
    'evals': [], 
    'entropy': [],
    'var': []
}

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.LUMEN]
)


app.layout = html.Div([
    html.H1(children = dcc.Markdown('Active Learning for Mono-H($b\\bar{b}$) search', mathjax=True), className = "text-center p-3", style = {'color': 'black'}),
    html.H2(children = "Visualize the 4D exclusion contour", className = "text-center p-3", style = {'color': 'black'}),
    
    dbc.Label(style={"margin-left": "600px"}),
    dbc.Label(dcc.Markdown('$\mathrm{M}_\chi\,\,\mathrm{[GeV]}$', mathjax=True)),
    html.Div([
    dcc.Slider(
        100,
        1200,
        step=None,
        value=100,
        marks={int(mdm) if mdm % 1 == 0 else mdm: '{}'.format(mdm) for mdm in mdm_list},
        id='mdm-slider',
        vertical=False,
    )],
    style={'padding-left':'40%', 'padding-right':'0%'}
    ),
    dbc.Label(style={"margin-left": "600px"}),
    html.Label(dcc.Markdown('$g_\chi$', mathjax=True)),
    html.Div([
    dcc.Slider(
        0.5,
        2.0,
        step=None,
        value=0.5,
        marks={int(gx) if gx % 1 == 0 else gx: '{}'.format(gx) for gx in [0.5, 0.75, 1.0, 1.25, 1.5,1.75, 2.0]},

        id='gx-slider',
        vertical=False,
    )],
     style={'padding-left':'40%', 'padding-right':'0%'}
    ),
    
    html.Div([html.Img(id = 'graph-with-slider', style={'height':'50%', 'width':'50%'})],
             style={'textAlign': 'center'},id='plot_div')
    
    # html.Div([
    # dcc.Graph(id='graph-with-slider')
    # ], style={'padding-left':'25%', 'padding-right':'25%'})
])




@app.callback(
    Output('graph-with-slider', 'src'),
    [Input('gx-slider', 'value'),  Input('mdm-slider', 'value')]
)

def update_figure(gx, mdm):
    
    if(type(gx)==int): #freaking bug in dash
        image_file = f"assets/m_{mdm}_gx_{gx}.0.jpg"
    else:
        image_file = f"assets/m_{mdm}_gx_{gx}.jpg"
    
    # #fig = html.Img(image_file)
    # img = io.imread(image_file)
    # fig = px.imshow(img, height=800, width=800)
    # fig.update_layout(showlegend=False)
    # fig.update_xaxes(visible=False)
    # fig.update_yaxes(visible=False)
    # fig.update_layout(transition_duration=1)
    
    return image_file


if __name__ == '__main__':
    app.run_server(debug=True)