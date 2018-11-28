import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.2/css/bulma.min.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.Div(className='columns', children=[
        html.Div(className='column', children=[
            dcc.Input(id='input_id', value=None, debounce=True, type='text'),
        ]),
    ]),

    html.Div(className='columns', children=[
        html.Div(className='column', children=[
            html.Div(id='output_div'),
        ]),
    ]),
], className='container')


@app.callback(
    Output(component_id='output_div', component_property='children'),
    [Input(component_id='input_id', component_property='value')]
)
def update_output_div(input_value):
    if input_value:
        message = '不合格'
        if input_value.isdigit() and int(input_value) >= 80:
            message = '合格'

        return html.Div(className='output-area', children=[
            html.Span(message)
        ])

    else:
        html.Div()


if __name__ == '__main__':
    app.run_server(debug=True)
