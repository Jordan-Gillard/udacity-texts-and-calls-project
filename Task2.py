"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    max_time = 0
    telephone_number = None
    for call in calls:
        number_of_caller = call[0]
        time_of_call = int(call[3])
        if time_of_call > max_time:
            max_time = time_of_call
            telephone_number = number_of_caller
    print(f"{telephone_number} spent the longest time, {max_time} seconds, on the phone during September 2016.")

"""
Time Complexity:
Because we have to iterate over all rows in the calls.csv file, the time complexity is O(n).
"""

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
