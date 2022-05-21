import json

f = open('combinationResult.json')

data = json.load(f)
dataLen = len(data)

print(dataLen)

finalData = []

searchList = ['F', 'I', 'Y', 'O', 'E', 'N', 'W', 'T', 'R']

searchKey = set(searchList)

for row in data:
    rowSet = set(row[0])
    if rowSet.issubset(searchKey):
        finalData = row
        break

print(finalData)