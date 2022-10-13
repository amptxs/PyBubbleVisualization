from bokeh.models import WheelZoomTool

from LinearPlotter import LinearPlotter
import ExcelProcessor as ep
from math import pi
from bokeh.io import output_file, show
from bokeh.plotting import figure, curdoc
from bokeh.models import CustomJS, RadioButtonGroup, Slider, Button
from bokeh.layouts import column


# Map = figure(title="Pie map", plot_width=1500, plot_height=700)
# Map.toolbar.active_scroll = Map.select_one(WheelZoomTool)

# year = 2016
# defaultRadiusMultiplier = 1.2

# # TODO преобразовать в функцию расчет паев (снизу в цикле) и сделать вызов функции по выбранному году
# # TODO возможно для этого придется использовать Bokeh Server или переводить расчеты в CustomJS
# LABELS = ["2016", "2017", "2018", "2019", "2020", "2021"]
# radio_button_group = RadioButtonGroup(labels=LABELS, active=0)
# slider = Slider(start=0.1, end=4, step=0.01, value=1.2)


# df = ep.normalize(ep.readExcel())

# for name in df.keys():
#     localPie = df[name].loc[df[name]['Дата'] == year]
#     if not localPie.empty:
#         if 'X' in localPie:
#             X = localPie['X'].values[0]
#             Y = localPie['Y'].values[0]

#             debitFluid = localPie['Дебит_жидкости,т/сут'].values[0]
#             debitPetrol = localPie['Дебит_нефти,т/сут'].values[0]
#             debitWater = debitFluid - debitPetrol

#             radius = debitFluid * defaultRadiusMultiplier

#             percent = debitPetrol / debitFluid
#             pieFigure = figure(x_range=(-1, 1), y_range=(-1, 1))
#             starts = [pi / 2, pi * 2 * percent + pi / 2]
#             ends = [pi / 2 + pi * 2 * percent, pi / 2 + 2 * pi]
#             pieColors = ['brown', 'blue']

#             # TODO legend field, hover
#             # На point можно цеплять евенты
#             point = Map.wedge(x=X, y=Y, radius=radius,
#                       start_angle=starts, end_angle=ends,
#                       line_color="white", color=pieColors)

#             slider.js_on_change('value',
#                                 CustomJS(args=dict(other=point.glyph,size=debitFluid),
#                                          code="other.radius = this.value * size"))


# show(column(radio_button_group, slider, Map))

## Проверка графика


df = ep.sheetsConcat(ep.normalize(ep.readExcel()))
# print(df.loc[df['Имя'] == "15015Г"])
plotter = LinearPlotter(df, "15015Г")
plotter.show()