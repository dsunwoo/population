import collections
population_dict = collections.defaultdict(int)
population_density = collections.defaultdict(float)

with open('datafiles/continent-90m.csv', 'rU') as inputFile:
    header = next(inputFile)
    for line in inputFile:
        line = line.rstrip().split(',')
        # Grab each continent's land area data
        line[7] = int(line[7])
        if line[1] == 'Total National Population':
            population_dict[line[0]] += line[7]
            # print("%s %s %s %s" % (line[0], line[5], line[6]))
inputFile.close()
# print(population_dict)

with open('datafiles/land_area.csv', 'w') as outputFile:
    outputFile.write('continent,land_area\n')

    for k, v in population_dict.items():
        outputFile.write(k + ',' + str(v) + '\n')

with open('datafiles/pop_2010.csv', 'rU') as inputFile:
    header2 = next(inputFile)
    # Loop through each continent in the 2010 population file
    for line in inputFile:
        line = line.rstrip().split(',')
        # Match up Continent in land area file and calc. density
        for k, v in population_dict.items():
            if k == line[0]:
                density = float(int(line[1])/int(v))
                population_density[line[0]] = density
                print("{} {} {} {}"
                    .format(line[0], line[1], v, density))
inputFile.close()

with open('datafiles/pop_density.csv', 'w') as outputFile:
    outputFile.write('continent, 2010_PopDensity\n')

    for k, v in population_density.items():
        outputFile.write(k + ',' + str(v) + '\n')
