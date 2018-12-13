import csv
import pygal
with open('database_for_alcohol.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    sample_list = []
    for line in csv_reader:
        sample_list.append(line)
    header = list(map(int, sample_list[0]))
    line_1 = list(map(float, sample_list[1]))
    line_2 = list(map(float, sample_list[2]))
    line_3 = list(map(float, sample_list[3]))
    for i in range(len(line_1)):
        if line_1[i] == 0:
            line_1[i] = None
    for i in range(len(line_2)):
        if line_2[i] == 0:
            line_2[i] = None
    for i in range(len(line_3)):
        if line_3[i] == 0:
            line_3[i] = None
line_chart_2 = pygal.Line()
line_chart_2.title = 'Alcohol expenditure as a percentage of total expenditure and income in 2543-2556'
line_chart_2.x_labels = header
line_chart_2.add('"%"of total expenditure', line_2)
line_chart_2.add('"%"of income', line_3)
line_chart_2.render_to_file('graph_2.svg')
