import csv
import pygal
with open('test.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    sample_list = []
    for line in csv_reader:
        sample_list.append(line)
    header = list(map(int, sample_list[0]))
    line_1 = list(map(float, sample_list[1]))
    for i in range(len(line_1)):
        if line_1[i] == 0:
            line_1[i] = None
line_chart = pygal.Line()
line_chart.title = 'Average alcohol expenditure per household in 2543 THB (adjusted for inflation)'
line_chart.x_labels = header
line_chart.add('Overall',line_1)
line_chart.render_to_file('graph_1.svg')
