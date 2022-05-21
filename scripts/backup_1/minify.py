import json

source = open('combinationResult.json', 'r')
destination = open('combinationResult_minify.json', 'w+')

sourceData = json.load(source)

result = json.dumps(sourceData, separators=(',', ':'))

destination.write(result)
destination.close()