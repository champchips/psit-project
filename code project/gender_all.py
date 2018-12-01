import pygal
line_chart = pygal.Line()
line_chart.title = 'Consumption rate by genders (in %)'
line_chart.x_labels = map(str, range(2544, 2559))

line_chart.add('Overall',[32.61, None, None, 32.69, None, None, 30.02, None, None, None, 31.53, None, 32.22, 32.29, None])
line_chart.add('Male',[55.84, None, None, 55.47, None, None, 52.26, None, None, None, 53.37, None, 53.99, 52.96, None])
line_chart.add('Female',[9.76, None, None, 10.32, None, None, 9.09, None, None, None, 10.87, None, 11.79, 12.92, None])
line_chart.render_to_file('gender_2.svg')

