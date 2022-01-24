"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
total_time = 0
for number_data in calls:
    if int(number_data[-1]) > int(total_time):
        total_time = number_data[-1]
        telephone_number = number_data[0]
print(f"{telephone_number} spent the longest time, {total_time} seconds, on the phone during September 2016.")
