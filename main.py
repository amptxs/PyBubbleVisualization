import ExcelProcessor as ep
import plotly.express as px

df = ep.sheetsConcat(
    ep.createNames(
        ep.readExcel('data/Data.xlsx')))
fig = px.scatter(df.query("Дата==2016"), x="Добыча нефти,т", y="Добыча жидкости,т",
                 color="Способ", hover_name="Имя", log_x=True, size_max=60)

fig.show()
