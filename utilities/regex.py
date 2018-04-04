import re

regex = r"([a-zA-Z]+) (\d+)"
regex = r"^\d{5}(?:[-\s]\d{4})?$"
msg = "90249 abc street"

match = re.search(regex, msg)

if match:
    print("Match at index %s, %s" % (match.start(), match.end()))
    print("Full match: %s" % (match.group(0)))

    for i in range(1, match.lastindex+1):
        print(match.group(i))
else:
    print("The regex pattern does not match. :(")


