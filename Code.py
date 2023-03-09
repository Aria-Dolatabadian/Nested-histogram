from bokeh.palettes import Spectral5
from bokeh.plotting import figure, show
from bokeh.transform import factor_cmap
import pandas as pd

df = pd.read_csv("FileName.csv")

df.company = df.company.astype(str)

group = df.groupby(['company', 'cultivar'])

index_cmap = factor_cmap('company_cultivar', palette=Spectral5, factors=sorted(df.company.unique()), end=1)

p = figure(width=1800, height=600, title="Mean score by company and cultivar",
           x_range=group, toolbar_location=None, tooltips=[("SCORE", "@score_mean"), ("Company, Cultivar", "@company_cultivar")])

p.vbar(x='company_cultivar', top='score_mean', width=1, source=group,
       line_color="gray", fill_color= index_cmap)

p.y_range.start = 0
p.x_range.range_padding = 0.05
p.xgrid.grid_line_color = None
p.xaxis.axis_label = "Cultivar grouped by company"
p.xaxis.major_label_orientation = 1.2
p.outline_line_color = None

show(p)
