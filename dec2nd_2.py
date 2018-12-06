def sol():

    frequencies = set()

    frequency = 0

    while True:

        with open("inputs/dec2nd.in") as input:

            for line in input:
                
                frequencies.add(frequency)

                if line[0] == "-":

                    frequency -= int(line[1:])

                else:

                    frequency += int(line[1:])

                if frequency in frequencies:

                    return frequency

print(sol())

                    
