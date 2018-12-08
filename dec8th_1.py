from heapq import *
import sys


def sol():

    inputs = sys.stdin.readlines()

    graph = [set() for i in range(26)]
    indegrees = [0 for i in range(26)]

    for job in inputs:

        beginning = ord(job[5]) - ord('A')
        end = ord(job[36]) - ord('A')

        graph[beginning].add(end)
        indegrees[end] += 1

    Q = []

    answer = ''

    for vertex in range(26):

        if indegrees[vertex] == 0:

            heappush(Q, vertex)

    while Q:

        popped = heappop(Q)
        
        answer += chr(popped + ord('A'))

        for vertex in graph[popped]:
            
            indegrees[vertex] -= 1

            if indegrees[vertex] == 0:

                heappush(Q, vertex)

        graph[popped].clear()

    print(answer)



sol()
