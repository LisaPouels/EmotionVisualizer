import data.database.database_interface as db
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from dash import Dash, dcc, html
from datetime import datetime, timedelta


app = Dash(__name__)
app.title = 'Reddit Emotions'

df = pd.DataFrame.from_dict(db.selectEmotions())

#define the layout of the app
app.layout = html.Div(children=[
    html.Div(children=[
        html.H1(children='Reddit Emotion Visualization', className='header-title'),
        html.Div(id='live-update-text', className='header-description'),
        ],
        className = 'header'
    ),
    html.Div(children=[
        html.Div(children=[
            html.Div(children='Select a region:', className = 'menu-title'),
            dcc.Dropdown(options = [
                {'label': 'All', 'value': 'All'},
                {'label': 'Africa', 'value': 'Africa'},
                {'label': 'Asia', 'value': 'Asia'},
                {'label': 'Europe', 'value': 'Europe'},
                {'label': 'North America', 'value': 'North America'},
                {'label': 'Oceania', 'value': 'Oceania'},
                {'label': 'South America', 'value': 'South America'},
                {'label': 'Artics', 'value': 'Artics'}
                ], 
                value='All',
                id='region_dropdown')],
                className = 'dropdown'
                ),
        html.Div(children=[
            html.Div(children='Select a time range:', className = 'menu-title'),
            dcc.DatePickerRange(
                id='date-picker-range',
                min_date_allowed=datetime(2022, 1, 1),
                max_date_allowed=datetime.now(),
                start_date=datetime.now() - timedelta(days=1),
                end_date=datetime.now()
            )]),
    ],
    className = 'menu'
    ),
    dcc.Interval(
        id='interval-component',
        interval=1*3600000, # in milliseconds
        n_intervals=0
    ),
    html.Div(children=[
        dcc.Graph(
        id='emotion_visualization',
        className='card'
        ),
        ], 
    className='wrapper'
    ),
    html.Div(children=[
        html.H1(children='This visualization was created using data from Reddit, specifically subreddits of countries.', className='text'),
        ])
])

#callback to update the graph every hour
@app.callback(Output('live-update-text', 'children'),
                Input('interval-component', 'n_intervals'))
def update_metrics(n):
    global df
    df = pd.DataFrame.from_dict(db.selectEmotions())
    return [
        html.Span('Last update: {}'.format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))) 
    ]

#callback to update the graph based on the dropdown and datepicker
@app.callback(Output('emotion_visualization', 'figure'),
                Input('region_dropdown', 'value'),
                Input('date-picker-range', 'start_date'),
                Input('date-picker-range', 'end_date')
                )
def update_graph_live(value, start_date, end_date):
    if value == 'All':
        selection = df
        y = 'continent'
    else:
        selection = df[df['continent'] == value]
        y = 'subreddit'
    fig = px.scatter(selection, x='time', y=y, color='emotion', size=[float(size) for size in selection['importance_scaled'].to_list()], 
    hover_name='subreddit', hover_data={'continent':False,'subreddit':False,'importance':True, 'emotion':True, 'time':True, 'importance_scaled': False}, category_orders={'emotion':['Happy', 'Fear', 'Surprise', 'Sad', 'Angry']},
    color_discrete_map={'Happy':'rgb(255,217,47)', 'Fear':'rgb(95,70,144)', 'Surprise':'#DA60CA', 'Sad':'rgb(136,204,238)', 'Angry':'#B82E2E'})
    fig.update_layout(xaxis_range=[start_date, end_date])
    fig.update_yaxes(type = 'category', categoryorder='category descending')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)