import sys

def sol():

    countof2s = 0
    countof3s = 0

    for line in sys.stdin:

        letter_counts = [0] * 26

        for letter in line[:len(line) - 1]:

            letter_counts[ord(letter) - ord('a')] += 1

        had2 = False
        had3 = False

        for count in letter_counts:

            if not had2 and count == 2:

                countof2s += 1
                had2 = True

            if not had3 and count == 3:
                
                countof3s += 1
                had3 = True

    return countof2s * countof3s

print(sol())

