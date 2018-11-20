import pygal
line_chart = pygal.Line()
line_chart.title = 'Consumption rate by genders (in %)'
line_chart.x_labels = map(str, range(2550, 2558))
line_chart.add('Overall',[30.02, None, None, None, 31.53, None, 32.22, 32.29])
line_chart.add('Male',[52.26, None, None, None, 53.37, None, 53.99, 52.96])
line_chart.add('Female',[9.09, None, None, None, 10.87, None, 11.79, 12.92])
line_chart.render_to_file('gender.svg')
