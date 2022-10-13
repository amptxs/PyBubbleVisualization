import re
from numpy import arange, linspace, pi, sin

from bokeh.models import LinearAxis, Range1d, Title
from bokeh.plotting import figure, output_notebook, show

class LinearPlotter:
    
    def __init__(self, data, name):
        self.data = data.loc[data['Имя'] == name] 
        self.data = self.data.astype({'Дата': 'str'})
        self.data = self.data.loc[self.data['Дата'].str.len() != 4] # Выпиливаем строки с годами
        self.name = name
        
    def show(self):
        x_axis = self.create_main_x_axis(self.data)

        main_plot = figure(
            title=Title(text="Динамика технологических показателей скв. " + self.name, align='center'),
            sizing_mode="stretch_width",
            x_axis_label="Годы",
            x_range=x_axis,
            height=500
        )
        # pass
        main_plot = self.add_layouts(main_plot)
        show(main_plot)
    
    def add_layouts(self, plot):
        
        plot.extra_y_ranges = {
            "oil_debit": Range1d(start=0, end=150), 
            'liquid_debit': Range1d(start=0, end=100), 
            'water_cut': Range1d(start=0, end=100), 
            'pressure':  Range1d(start=0, end=500)
        }
        
        plot.add_layout(self.create_y_axis("water_cut", "Обводненность"), 'left')
        plot.add_layout(self.create_y_axis("liquid_debit", "Дебит, м3/сут"), 'left')
        plot.add_layout(self.create_y_axis("oil_debit", "Дебит, т/сут"), 'left')
        plot.add_layout(self.create_y_axis("pressure", "Давление, ат"), 'right')

        plot = self.create_line(self.data, 'Дата', 'Дебит_нефти,т/сут', plot, 'brown')
        plot = self.create_line(self.data, 'Дата', 'Дебит_жидкости,м3/сут', plot, 'green')
        plot = self.create_line(self.data, 'Дата', 'Обводненность вес.,%', plot, 'blue')
        plot = self.create_line(self.data, 'Дата', 'Давление на ВДП_пластовое', plot, 'green')
        
        plot = self.create_circle(self.data, 'Дата', 'Давление на ВНК_пластовое', plot, 'green')
        
        plot = self.create_bar(self.data, 'Дата', 'Давление на ВНК_пластовое', plot, 'green')
        
        
        return plot
    
    def create_y_axis(self, name, label):
        return LinearAxis(y_range_name=name, axis_label=label, axis_label_text_font_style='normal')
    
    def create_line(self, data, x_label, y_label, plot, color="black"):
        x = []
        y = []
        
        for index, row in data.iterrows():
            
            x_value = row[x_label] 
            if (x_value[-4] == '.'):
                x_value = x_value + "0"
                
            x.append(x_value)
            y.append(500 + row[y_label])
            
            # Дебит_нефти,т/сут
            
        plot.line(x, y, legend_label=y_label, color=color)
        return plot
    
    def create_circle(self, data, x_label, y_label, plot, color='black'):
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
            
        plot.circle(x, y, legend_label=y_label, color=color)
        return plot
    
    def create_bar(self, data, x_label, y_label, plot, color='black'):
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
            
        plot.rect(x, y, legend_label=y_label, width=0.4, height=y, color=color)
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
        # return years__axis