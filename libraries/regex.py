"""
https://pymotw.com/2/re/
"""

import re

# """ EX 1 """
# pattern = re.compile(r"\w")
# string = "regex is awesome!"
#
# # Then call a matching method to match our pattern
# result = pattern.match(string)
# print(result.group()) # will print out 'r'

""" EX 2 """
# Replace the pattern variable with this
pattern = re.compile(r"\w+") # Notice the plus sign we just added

def regex(string):
    """This function returns at least one matching digit."""
    pattern = re.compile(r"\d{1,}") # For brevity, this is the same as r"\d+"
    result = pattern.match(string)
    if result:
        return  result.group()
    return None

# Call our function, passing in our string
print(regex("007 James Bond"))