import sys


def sol():

    poly = sys.stdin.read()

    shortest = len(poly) - 1

    for letter in range(65, 91, 1):

        left = 0
        right = 1
        # This adds unnecessary constant.
        polymer = poly.replace(chr(letter), '')
        polymer = polymer.replace(chr(letter + 32), '')
        length = len(polymer) - 1

        jumps = dict()

        while left < right and right < len(polymer) - 1:
     
            if abs(ord(polymer[left]) - ord(polymer[right])) == 32:

                length -= 2

                new_left = left - 1

                while new_left > 0 and new_left in jumps:

                    new_left -= jumps[new_left]

                if new_left in jumps or new_left < 0:

                    new_left = right

                new_right = right + 1

                if new_left < left:

                    jumps[right] = right - new_left

                else:

                    jumps[right] = right

                jumps[left] = new_right - left

                right = new_right
                left = new_left

            else:
            
                left = right

                right += 1

        if length < shortest:

            shortest = length

    return shortest

print(sol())
