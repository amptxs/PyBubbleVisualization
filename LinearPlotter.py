import re
from numpy import arange, linspace, pi, sin
import numpy as np

from bokeh.models import LinearAxis, Range1d, Title, NumeralTickFormatter, FactorRange, SingleIntervalTicker
from bokeh.models.ranges import DataRange1d
from bokeh.plotting import figure, output_notebook, show


class LinearPlotter:

    def __init__(self, data, name):
        self.data = data.loc[data['Имя'] == name]
        self.data = self.data.astype({'Дата': 'str'})
        self.data = self.data.loc[self.data['Дата'].str.len() != 4]  # Выпиливаем строки с годами
        self.name = name

    def show(self):
        x_axis = self.create_main_x_axis(self.data)

        main_plot = figure(
            title=Title(text="Динамика технологических показателей скв. " + self.name, align='center'),
            sizing_mode="stretch_width",
            height=750,
            x_axis_label="Годы",
            x_range=x_axis,
            # x_range=FactorRange(*x_axis),
            y_range=None
        )
        # pass
        main_plot.xaxis.major_label_orientation = "vertical"
        main_plot = self.add_layouts(main_plot)
        return main_plot

    def add_layouts(self, plot):

        plot.extra_y_ranges = {
            "oil_debit": Range1d(start=0, end=150),
            'liquid_debit': Range1d(start=0, end=100),
            'water_cut': Range1d(start=0, end=1),
            'pressure': Range1d(start=0, end=500)
        }

        plot = self.create_line(self.data, 'Дата', 'Дебит_нефти,т/сут', plot, 'brown', 'oil_debit')
        plot = self.create_line(self.data, 'Дата', 'Дебит_жидкости,м3/сут', plot, 'green', 'liquid_debit')
        plot = self.create_line(self.data, 'Дата', 'Обводненность вес.,%', plot, 'blue', 'water_cut')
        # plot = self.create_line(self.data, 'Дата', 'Давление на ВДП_пластовое', plot, 'green', 'pressure')

        plot = self.create_circle(self.data, 'Дата', 'Давление на ВНК_пластовое', plot, 'green', 'pressure')

        plot = self.create_bar(self.data, 'Дата', 'Давление на ВНК_пластовое', plot, 'green', 'pressure')

        plot.add_layout(self.create_y_axis("water_cut", "Обводненность"), 'left')
        plot.add_layout(self.create_y_axis("oil_debit", "Дебит, т/сут"), 'left')
        plot.add_layout(self.create_y_axis("liquid_debit", "Дебит, м3/сут"), 'left')
        plot.add_layout(self.create_y_axis("pressure", "Давление, ат"), 'right')

        return plot

    def create_y_axis(self, name, label):
        if (label == 'Обводненность'):
            return LinearAxis(y_range_name=name, axis_label=label, axis_label_text_font_style='normal',
                              formatter=NumeralTickFormatter(format='0 %'))
        elif (label == 'Дебит, т/сут'):
            return LinearAxis(y_range_name=name, axis_label=label, axis_label_text_font_style='normal',
                              ticker=SingleIntervalTicker(interval=15))
        else:
            return LinearAxis(y_range_name=name, axis_label=label, axis_label_text_font_style='normal')

    def create_line(self, data, x_label, y_label, plot, color="black", y_range_name='default'):
        x = []
        y = []

        # y_range_name = 'default'

        for index, row in data.iterrows():

            x_value = row[x_label]
            if (x_value[-4] == '.'):
                x_value = x_value + "0"

            x.append(x_value)

            if y_range_name == 'water_cut':
                y.append(row[y_label] / 100)
            else:
                y.append(row[y_label])

            # Дебит_нефти,т/сут

        if y_range_name != '':
            line = plot.line(x, y, legend_label=y_label, color=color, x_range_name='default', y_range_name=y_range_name)
        else:
            line = plot.line(x, y, legend_label=y_label, color=color)

        # plot.renderers = plot.renderers.append(line)

        return plot

    def create_circle(self, data, x_label, y_label, plot, color='black', y_range_name='default'):
        x = []
        y = []

        for index, row in data.iterrows():

            x_value = row[x_label]
            if (x_value[-4] == '.'):
                x_value = x_value + "0"

            x.append(x_value)
            y.append(row[y_label])

            # Дебит_нефти,т/сут

        plot.circle(x, y, legend_label=y_label, color=color, y_range_name=y_range_name)
        return plot

    def create_bar(self, data, x_label, y_label, plot, color='black', y_range_name='default'):
        x = []
        y = []

        for index, row in data.iterrows():

            x_value = row[x_label]
            if (x_value[-4] == '.'):
                x_value = x_value + "0"

            x.append(x_value)
            y.append(row[y_label])
            # y.append(100 + row[y_label])

            # Дебит_нефти,т/сут
        y = np.array(y)
        plot.rect(x, 500, legend_label=y_label, width=0.4, height=-y, color=color, y_range_name=y_range_name)
        return plot

    def create_main_x_axis(self, data):

        years = data['Дата']
        years_x_axis = []
        just_months = []
        for year in years:
            string_year = str(year)
            if string_year[-4] == ".":
                string_year = string_year + "0"

            if len(string_year) != 4:
                just_months.append(string_year)
                years_x_axis.append((string_year[-4:], string_year))

        return just_months
        # return years_x_axis