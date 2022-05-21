import json


def isValid(word):
    s = set(word)
    return len(s) > 3 and len(s) < 6



source = open('source.txt', 'r')
sourceLines = source.readlines()

destination = open('final.txt', 'w+')

uniqueWords = []

count = 0

for sourceLine in sourceLines:
    sourceLine = sourceLine.strip()
    if isValid(sourceLine) :
        if sourceLine not in uniqueWords:
            uniqueWords.append(sourceLine)
            count += 1

result = json.dumps(uniqueWords, indent = 4)

destination.writelines(result)
destination.close()

print(count)

print(sourceLines[0], len(sourceLines[0]))