import csv
dataset1 = []
dataset2 = []

with open("dataset_1.csv", "r") as f:
    csvReader = csv.reader(f)
    for i in csvReader:
        dataset1.append(i)

with open("dataset_sorted.csv", "r") as f:
    csvReader = csv.reader(f)
    for i in csvReader:
        dataset2.append(i)

header1 = dataset1[0]
planetData1 = dataset1[1:]

header2 = dataset2[0]
planetData2 = dataset2[1:]

headers = header1 + header2
planetData = []

for a,data in enumerate(planetData1):
    planetData.append(planetData1[a] + planetData1[a] )

with open("mergedData.csv", "a+") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planetData)
    
    

