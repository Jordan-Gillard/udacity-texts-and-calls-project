"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from collections import defaultdict

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    telephone_number_times = defaultdict(int)

    for call in calls:
        caller, receiver, _, time = call
        time = int(time)
        telephone_number_times[caller] += time
        telephone_number_times[receiver] += time
    max_phone_number = max(telephone_number_times, key=telephone_number_times.get)
    max_time = telephone_number_times[max_phone_number]

    print(f"{max_phone_number} spent the longest time, {max_time} seconds, on the phone during September 2016.")

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
