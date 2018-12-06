import sys


def manhattan(x, y):

    return abs(x[0] - y[0]) + abs(x[1] - y[1])

def sol():

    points  = list()

    coordinates = sys.stdin.readlines()

    for line in coordinates:

        split_line = line.split(',')
        x = int(split_line[0])
        y = int(split_line[1])

        points.append((x,y))

    min_x = points[0][0]
    max_x = points[0][0]
    min_y = points[0][1]
    max_y = points[0][1]

    for point in points:

        if point[0] < min_x:

            min_x = point[0]

        if point[0] > max_x:

            max_x = point[0]

        if point[1] < min_y:

            min_y = point[1]

        if point[1] > max_y:

            max_y = point[1]

    width = max_x - min_x + 1
    height = max_y - min_y + 1

    area = 0

    for row in range(height):

        for column in range(width):

            current = (min_x + column, min_y + row)
            distance_sum = 0

            for point in range(len(points)):

                distance_sum += manhattan(current, points[point])


            if distance_sum < 10000:

                area += 1
            
    print(area)


sol()
