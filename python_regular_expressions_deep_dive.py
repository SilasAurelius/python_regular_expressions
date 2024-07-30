"""Problem Statement: You have a script that extracts email addresses from a text but needs to be refined to exclude certain domains (e.g., '[exclude.com](http://exclude.com/)'). Modify the script to extract all email addresses except those from the specified domain.
"""
import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print("Unaltered list", emails)
print()
#Adapt the regex pattern to exclude email addresses from '[exclude.com](http://exclude.com/)'.

#Ensure the script still extracts all other valid email addresses. 

# Updated regex pattern to exclude emails from 'exclude.com'
pattern = r"\b[A-Za-z0-9._%+-]+@(?!exclude\.com\b)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
# Had to use a negative lookahead assertion ?!.

emails = re.findall(pattern, text)
print("Modified list: ", emails)

print()
