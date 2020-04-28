"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

has_made_calls = set()
has_sent_texts = set()
has_received_calls = set()
has_received_texts = set()

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for text in texts:
        sender, receiver, *args = text
        has_sent_texts.add(sender)
        has_received_texts.add(receiver)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        sender, receiver, *args = call
        has_made_calls.add(sender)
        has_received_calls.add(receiver)

not_telemarketer = has_sent_texts.union(has_received_texts, has_received_calls)
telemarketers = has_made_calls.difference(not_telemarketer)
telemarketers_sorted = sorted(telemarketers)
print("These numbers could be telemarketers: ")
print(*telemarketers_sorted, sep='\n')

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
