import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app

# import header, footer from index_static_html
from index_static_html import header, footer
# import all the components here
from components.home_component import home_view as home

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    header(),
    html.Div(id='page-content'),
    footer()
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/app1':
         return home.layout
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)
