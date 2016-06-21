import collections
population_dict = collections.defaultdict(int)
population_growth = collections.defaultdict(float)

with open('datafiles/continent-90m.csv', 'rU') as inputFile:
    header = next(inputFile)
    for line in inputFile:
        base = 0
        future = 0
        line = line.rstrip().split(',')
        line[5] = int(line[5])
        line[6] = int(line[6])
        if line[1] == 'Total National Population':
            base += line[5]
            future += line[6]
            population_dict[line[0]] += (future - base)
            # print("%s %s %s %s" % (line[0], line[5], line[6]))
inputFile.close()
# print(population_dict)

with open('datafiles/pop_diff.csv', 'w') as outputFile:
    outputFile.write('continent,2010_2100_diff\n')

    for k, v in population_dict.items():
        outputFile.write(k + ',' + str(v) + '\n')

with open('datafiles/pop_2010.csv', 'rU') as inputFile:
    header2 = next(inputFile)
    for line in inputFile:
        line = line.rstrip().split(',')
        for k, v in population_dict.items():
            if k == line[0]:
                growth = float(int(v)/int(line[1]))
                population_growth[line[0]] = growth
                print("{} {} {} {}".format(line[0], line[1], v, growth))
inputFile.close()

with open('datafiles/pop_growth.csv', 'w') as outputFile:
    outputFile.write('continent, 2010_2100_Growth\n')

    for k, v in population_growth.items():
        outputFile.write(k + ',' + str(v) + '\n')
