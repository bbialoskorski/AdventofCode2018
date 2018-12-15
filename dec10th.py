import sys
from collections import deque

def simulate(player_count, last_marble):

    circle = deque([0])
    score = [0 for i in range(player_count)]
    player = 0

    for marble in range(1, last_marble + 1, 1): 
       
        if marble % 23 != 0:

            circle.rotate(-1)
            circle.append(marble)
        
        else:

            score[player] += marble
            circle.rotate(7)
            removed_marble = circle.pop()
            circle.rotate(-1)
            score[player] += removed_marble

        player = (player + 1) % player_count

    return max(score)

def sol():

    input_str = sys.stdin.readline()
    input_str = input_str.split(' ')
    player_count = int(input_str[0])
    last_marble = int(input_str[6])

    print(simulate(player_count, last_marble))
    print(simulate(player_count, last_marble*100)) 

sol()
