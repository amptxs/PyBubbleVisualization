import ExcelProcessor as ep
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)
app.layout = html.Div([
    html.P("Год:"),
    dcc.Slider(id='yearSlider', min=2016, max=2021, step=1, value=2016,
               marks={x: str(x) for x in [2016, 2017, 2018, 2019, 2020, 2021]}),
    html.P("Размер:"),
    dcc.Slider(id='sizeSlider', min=10, max=130, step=5, value=60,
               marks={x: str(x) for x in [10, 30, 50, 70, 90, 110, 130]}),
    dcc.Graph(id="graph")
])

df = ep.sheetsConcat(
        ep.normalize(
            ep.readExcel('data/Data.xlsx')))


@app.callback(
    Output("graph", "figure"),
    [Input('yearSlider', 'value'), Input('sizeSlider', 'value')])
def update_figure(year, size):
    fig = px.scatter(df.query("Дата==" + str(year)), x="Дебит_нефти,т/сут", y="Дебит_жидкости,т/сут",
                     size="Дебит_жидкости,т/сут", color="Способ", hover_name="Имя", log_x=True, size_max=size,
                     height=600)

    return fig


app.run_server(debug=True)
