import pygal
line_chart = pygal.Line()
line_chart.title = 'Consumption rate by genders (Always)(in %)'
line_chart.x_labels = map(str, range(2544, 2559))

line_chart.add('Overall',[35.08, None, None, 38.24, None, None, 40.89, None, None, None, 44.22, None, 41.45, 42.41, None])
line_chart.add('Male',[37.93, None, None, 41.78, None, None, 44.36, None, None, None, 48.94, None, 46.15, 48.78, None])
line_chart.add('Female',[19.09, None, None, 19.55, None, None, 22.15, None, None, None, 22.31, None, 21.28, 17.94, None])
line_chart.render_to_file('gender_3.svg')