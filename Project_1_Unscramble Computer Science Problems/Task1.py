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
uniq_nums = set()
for number in texts:
    uniq_nums.add(number[0])  
    uniq_nums.add(number[1])

for number in calls:
    uniq_nums.add(number[0])  
    uniq_nums.add(number[1])

print(f"There are {len(uniq_nums)} different telephone numbers in the records")