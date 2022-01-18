import pandas as pd
import csv
df =pd.read_csv("wieght.csv")
import plotly.figure_factory as ff
figure = ff.create_distplot([df['Height(Inches)'].tolist()],['height'], show_hist=True)
#figure = ff.create_distplot([df['Weight(Pounds)'].tolist()],['weight'], show_hist=True)
figure.show()
