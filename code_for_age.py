import csv
import pygal
from pygal.style import DarkStyle
with open('database_for_age.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    sample_list = []
    for line in csv_reader:
        sample_list.append(line)
    year = list(map(int, sample_list[0][1:]))
    adult = list(map(float, sample_list[1][1:]))
    officer = list(map(float, sample_list[2][1:]))
    grand = list(map(float, sample_list[3][1:]))
    overall = list(map(float, sample_list[4][1:]))
    for i in range(len(adult)):
        if adult[i] == 0:
            adult[i] = None
    for i in range(len(overall)):
        if overall[i] == 0:
            overall[i] = None
    for i in range(len(grand)):
        if grand[i] == 0:
            grand[i] = None
    for i in range(len(officer)):
        if officer[i] == 0:
            officer[i] = None
line_chart = pygal.Bar(fill=True, interpolate='cubic', style=DarkStyle)
line_chart.title = 'Consumption rate by age groups(in %)'
line_chart.x_labels = map(str, year)
line_chart.add(str(sample_list[1][0]), adult)
line_chart.add(str(sample_list[2][0]), officer)
line_chart.add(str(sample_list[3][0]), grand)
line_chart.add(str(sample_list[4][0]), overall)
line_chart.render_to_file('gender_age.svg')
