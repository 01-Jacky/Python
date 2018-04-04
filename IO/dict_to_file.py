import json

# as requested in comment
exDict = {'one': 1,
          'two': 2}

with open('dict.txt', 'w') as file:
     file.write(json.dumps(exDict)) # use `json.loads` to do the reverse