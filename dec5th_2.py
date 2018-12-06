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

    fell_asleep = 0
    guard_id = 0

    for event in events: 

        if event[1][0] == 'G':

            guard_id = int(event[1].split(' ')[1][1:])

        if event[1][0] == 'f':

            fell_asleep = int(event[0][(len(event[0]) - 2):])

        if event[1][0] == 'w':

            woke_up = int(event[0][(len(event[0]) - 2):])

            if guard_id not in minute_stats:

                minute_stats[guard_id] = list()

                for i in range(60):

                    minute_stats[guard_id].append(0)
                

            for minute in range(fell_asleep, woke_up, 1):
                
               minute_stats[guard_id][minute] += 1 

    max_id = 0
    max_minute = 0
    max_frequency = 0

    for i in range(60):

        local_max_id = 0
        local_max_frequency = 0

        for guard in minute_stats.items():

            if guard[1][i] > local_max_frequency:

                local_max_frequency = guard[1][i]
                local_max_id = guard[0]

        if local_max_frequency > max_frequency:

            max_frequency = local_max_frequency
            max_minute = i
            max_id = local_max_id
  
    return max_id * max_minute


print(sol())
