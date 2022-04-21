"""
Read file into texts or calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

impossible_telemarketer = set()

possible_telemarketer = set()

for call_data in calls:
    impossible_telemarketer.add(call_data[1])
    possible_telemarketer.add(call_data[0])

for text_data in texts:
    impossible_telemarketer.add(text_data[0])
    impossible_telemarketer.add(text_data[1])

telemarketer = possible_telemarketer.difference(impossible_telemarketer)



result = list(sorted(telemarketer))
print(f"These numbers could be telemarketers: ")

print(*result, sep = "\n")

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive recieving calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

