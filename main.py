import csv

data = []
with open("dataset_2.csv","r") as f:
    csvReader = csv.reader(f)
    for i in csvReader:
        data.append(i)

headers = data[0]
planet_data = data[1:]
for a in planet_data:
    a[2] = a[2].lower()
    
planet_data.sort(key = lambda planet_data:planet_data[2])

with open("dataset_sorted.csv", "a+") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planet_data)


