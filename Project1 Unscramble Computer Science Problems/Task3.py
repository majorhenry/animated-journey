"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from os import sep

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
list_of_codes = []
count = 0
for call_data in calls[:]:
    if call_data[0][:5] == '(080)':
      if call_data[1][0] == '(' and call_data[1][1] == '0' :
        list_of_codes.append(call_data[1].split(')')[0]+')')
      if ' ' in call_data[1]:
        list_of_codes.append(call_data[1].split(' ')[0])
      if '(' not in call_data[1] and ' '  not in call_data[1] and call_data[1][:3] == '140':
        list_of_codes.append(call_data[1][:3])
result = sorted( set(list_of_codes))
print(f"The numbers called by people in Bangalore have codes:")
print( *result, sep = "\n")

result2 = sorted(list_of_codes)
for fixed_line in result2:
  
  if fixed_line == '(080)':
    count += 1
print(f" {'{0:.2g}'.format(count/len(result2))} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")