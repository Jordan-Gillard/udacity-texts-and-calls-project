"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv


def get_area_code(number):
    area_code = ""
    if "(" in number:  # fixed line number
        area_code_start = number.find("(")
        area_code_end = number.find(")")
        area_code = number[area_code_start + 1: area_code_end]
    elif " " in number:  # cell phone number
        area_code = number[0:4]
    elif number.startswith("140"):
        area_code = "140"
    return area_code


def is_bangalore_number(number):
    bangalore_number_prefix = "(080)"
    return number.startswith(bangalore_number_prefix)


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    area_codes_called = set()
    call_count = 0
    to_bangalore_number_count = 0
    for call in calls:
        caller_number, receiver_number, *args = call
        if is_bangalore_number(caller_number):
            area_codes_called.add(get_area_code(receiver_number))
            call_count += 1

            if is_bangalore_number(receiver_number):
                to_bangalore_number_count += 1

    area_codes_list = list(area_codes_called)
    area_codes_list.sort()

    print("The numbers called by people in Bangalore have codes:")
    for number in area_codes_list:
        print(number)

    percent_of_calls_among_bangalore = "{:.2f}".format((to_bangalore_number_count / call_count) * 100)
    print(f"{percent_of_calls_among_bangalore} percent of calls from fixed lines in Bangalore are calls to other "
          f"fixed lines in Bangalore.")


"""
Time Complexity:
First, we iterate over all rows in the csv file. The call to .sort() is of O(nlogn) complexity. So the time complexity
is O(nlogn + n), which can be shortened to O(nlogn).
"""

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
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
