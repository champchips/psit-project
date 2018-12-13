import csv
import pygal
from pygal.style import DarkStyle
from pygal.style import CleanStyle
with open('database_gender.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    sample_list = []
    for line in csv_reader:
        sample_list.append(line)
    year = list(map(int, sample_list[0][1:]))
    male = list(map(float, sample_list[1][1:]))
    overall = list(map(float, sample_list[2][1:]))
    female = list(map(float, sample_list[3][1:]))
    always_male = list(map(float, sample_list[4][1:]))
    always_overall = list(map(float, sample_list[5][1:]))
    always_female = list(map(float, sample_list[6][1:]))
    for i in range(len(male)):
        if male[i] == 0:
            male[i] = None
    for i in range(len(overall)):
        if overall[i] == 0:
            overall[i] = None
    for i in range(len(female)):
        if female[i] == 0:
            female[i] = None
    for i in range(len(always_male)):
        if always_male[i] == 0:
            always_male[i] = None
    for i in range(len(always_overall)):
        if always_overall[i] == 0:
            always_overall[i] = None
    for i in range(len(always_female)):
        if always_female[i] == 0:
            always_female[i] = None
    # creat new list men sometime
    male_sometime = []
    for i in range(len(male)):
        if male[i] != None and always_male[i] != None:
            male_sometime.append('%.2f' %(male[i]-always_male[i]))
        else:
            male_sometime.append(0)
    male_sometime = list(map(float, male_sometime))
    for i in range(len(male_sometime)):
        if male_sometime[i] == 0:
            male_sometime[i] = None
    # creat new list female sometime
    female_sometime = []
    for i in range(len(female)):
        if female[i] != None and always_female[i] != None:
            female_sometime.append('%.2f' %(abs(female[i]-always_female[i])))
        else:
            female_sometime.append(0)
    female_sometime = list(map(float, female_sometime))
    for i in range(len(female_sometime)):
        if female_sometime[i] == 0:
            female_sometime[i] = None
#all
line_chart = pygal.Bar(fill=True, interpolate='cubic', style=DarkStyle)
line_chart.title = 'Consumption rate by genders(in %)'
line_chart.x_labels = map(str, year)
line_chart.add(str(sample_list[1][0]), male)
line_chart.add(str(sample_list[2][0]), overall)
line_chart.add(str(sample_list[3][0]), female)
line_chart.render_to_file('gender_all.svg')
#amoung drinker
gender_always = pygal.Bar(fill=True, interpolate='cubic', style=DarkStyle)
gender_always.title = 'Percentage of regular drinkers amoung drinkers(in %)'
gender_always.x_labels = map(str, year)
gender_always.add(str(sample_list[4][0]), always_male)
gender_always.add(str(sample_list[5][0]), always_overall)
gender_always.add(str(sample_list[6][0]), always_female)
gender_always.render_to_file('gender_always.svg')
#male two different
male_vs_always = pygal.Bar(fill=True, interpolate='cubic', style=CleanStyle)
male_vs_always.title = 'Percentage of regular drinkers amoung drinkers(in %)[Male]'
male_vs_always.x_labels = map(str, year)
male_vs_always.add('Male amoung drinkers', always_male)
male_vs_always.add('Male regular drinkers', male_sometime)
male_vs_always.render_to_file('male_vs_always.svg')
#female two different
female_vs_always = pygal.Bar(fill=True, interpolate='cubic', style=CleanStyle)
female_vs_always.title = 'Percentage of regular drinkers amoung drinkers(in %)[Female]'
female_vs_always.x_labels = map(str, year)
female_vs_always.add('Female amoung drinkers', always_female)
female_vs_always.add('Female regular drinkers', female_sometime)
female_vs_always.render_to_file('female_vs_always.svg')