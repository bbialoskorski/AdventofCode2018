import sys


def sol():

    ids = sys.stdin.readlines()

    id_len = len(ids[0]) - 1

    for i in range(len(ids)):

        for j in range(i + 1, len(ids), 1):

            distance = 0
            
            index = 0 
            
            for k in range(id_len):
 
                if ids[i][k] != ids[j][k]:

                    index = k
                    distance += 1

            if distance == 1:

                return ids[i][:index] + ids[i][index + 1:id_len]

print(sol())
