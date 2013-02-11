import csv
import os
import json
from collections import defaultdict

all = defaultdict(int)
names = defaultdict(lambda: defaultdict(int))

with open(os.getcwd() + "/data/dogs_WNYC.csv", 'rb') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        if row[0] != 'dog_name':
            if len(row[3].split('-')) > 1:
                yr = int(row[3].split('-')[1])
                all[row[0].title()] += 1
                names[yr][row[0].title()] += 1

#only want names that appear N times, arbitrarily chosen to get 25 names
N = 275
tops = sorted([k for k,v in all.items() if v >= N])
tops.remove("N/A")

with open(os.getcwd() + '/data/dognames.csv', 'wb') as csvfile:
    f = csv.writer(csvfile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    f.writerow(["year"] + tops + ["total"])
    for year in range(12):
        total = 0
        dogs = names[year]
        data = [year]
        for name in tops:
            total += int(dogs[name])
            data.append(0 if name not in dogs else dogs[name])
        data.append(total)
        f.writerow(data)

#make JSON of all names for good measure
f = open(os.getcwd() + "/data/dognames.json", "w")
f.write(json.dumps(names, indent=2, sort_keys=True))
f.close()