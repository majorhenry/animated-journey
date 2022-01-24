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

possible_telemarketer = []
recieving_call = []
outgoing_text = []
recieving_text = []
for call_data in calls:
    possible_telemarketer.append(call_data[0])
    recieving_call.append(call_data[1])

for text_data in texts:
    outgoing_text.append(text_data[0])
    recieving_text.append(text_data[1])

for marketer in possible_telemarketer:
    if marketer in recieving_call or marketer in outgoing_text or marketer in recieving_text:
        possible_telemarketer.remove(marketer)
result = list(set(sorted(possible_telemarketer)))
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

