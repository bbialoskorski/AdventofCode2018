import operator
import sys


def sol():

    records = sys.stdin.readlines()

    events = list()

    for record in records:

        timestamp = record.split(']')[0].replace('[', '')
        event = record.split(']')[1]
        event = event[1:len(event) - 1]

        events.append((timestamp, event))

    events.sort(key=lambda event: event[0])

    minute_stats = dict()
    minutes_slept = dict()

    fell_asleep = 0
    guard_id = 0

    for event in events: 

        if event[1][0] == 'G':

            guard_id = int(event[1].split(' ')[1][1:])

        if event[1][0] == 'f':

            fell_asleep = int(event[0][(len(event[0])) - 2:])

        if event[1][0] == 'w':

            woke_up = int(event[0][(len(event[0]) - 2):])

            if guard_id not in minutes_slept:

                minutes_slept[guard_id] = 0
                minute_stats[guard_id] = list()

                for i in range(60):

                    minute_stats[guard_id].append(0)
                
            minutes_slept[guard_id] += woke_up - fell_asleep

            for minute in range(fell_asleep, woke_up, 1):
                
               minute_stats[guard_id][minute] += 1 

    laziest = max(minutes_slept.items(), key=operator.itemgetter(1))[0]

    minute = minute_stats[laziest].index(max(minute_stats[laziest]))

    return laziest * minute

print(sol())
