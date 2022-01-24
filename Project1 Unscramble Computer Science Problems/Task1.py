"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
record_list = []
for number in texts:
    if number[0] not in record_list:
        record_list.append(number[0])
    if number[1] not in record_list:
        record_list.append(number[0])
for number in calls:
    if number[0] not in record_list:
        record_list.append(number[0])
    if number[1] not in record_list:
        record_list.append(number[1])

print(f"There are {len(record_list)} different telephone numbers in the records")