def sol():

    frequency = 0; 

    with open ("inputs/dec2nd.in") as input:

        for line in input:

            if line[0] == "-":

                frequency -= int(line[1:])

            else:

                frequency += int(line[1:])

    print(frequency)

sol()
