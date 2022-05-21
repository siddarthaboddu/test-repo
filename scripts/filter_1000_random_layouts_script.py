import json
import random


f = open('combinationResult.json')

data = json.load(f)
dataLen = len(data)

print(dataLen)

finalData = []

for i in range(1000):
    pos = random.randint(0, dataLen-1)
    print(pos)
    finalData.append(data[pos])

print(len(finalData))

destination = open('combinationResult1000.json', 'w+')
destination.write(json.dumps(finalData, separators=(',', ':')))
destination.close()