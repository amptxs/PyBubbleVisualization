import ExcelProcessor as ep
from math import pi

import pandas as pd

from bokeh.io import output_file, show
from bokeh.layouts import row
from bokeh.palettes import Category20c
from bokeh.plotting import figure
from bokeh.transform import cumsum


Map = figure(title="Pie map", plot_width=1500, plot_height=700)
df = ep.normalize(ep.readExcel())

year = 2016
for name in df.keys():
    localPie = df[name].loc[df[name]['Дата'] == year]
    if not localPie.empty:
        if 'X' in localPie:
            X = localPie['X'].values[0]
            Y = localPie['Y'].values[0]
            debitFluid = localPie['Дебит_жидкости,т/сут'].values[0]
            debitPetrol = localPie['Дебит_нефти,т/сут'].values[0]

            percent = debitPetrol / debitFluid
            pieFigure = figure(x_range=(-1, 1), y_range=(-1, 1))
            starts = [pi / 2, pi * 2 * percent + pi / 2]
            ends = [pi / 2 + pi * 2 * percent, pi / 2 + 2 * pi]
            pieColors = ['brown', 'blue']

            # TODO legend field
            Map.wedge(x=X, y=Y, radius=100,
                      start_angle=starts, end_angle=ends,
                      line_color="white", color=pieColors)




#Map.wedge(x=0, y=1, radius=0.1,
#        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
#        line_color="white", fill_color='color', legend='country', source=data)



show(Map)
