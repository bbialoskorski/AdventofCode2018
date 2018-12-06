import sys

infinite = False

sys.setrecursionlimit(20000)

def manhattan(x, y):

    return abs(x[0] - y[0]) + abs(x[1] - y[1])

def bfs(row, col, num_rows, num_cols, grid, tag, visited):

    global infinite

    if row >= 0 and row < num_rows and col >= 0 and col < num_cols and not visited[row][col]:

        if grid[row][col] != tag:

            return 0

        visited[row][col] = True

        if row == 0 or row == num_rows - 1 or col == 0 or col == num_cols - 1:

            infinite = True

        area = 0
        # Up
        area += bfs(row - 1, col, num_rows, num_cols, grid, tag, visited) 
        # Right
        area += bfs(row, col + 1, num_rows, num_cols, grid, tag, visited)
        # Down
        area += bfs(row + 1, col, num_rows, num_cols, grid, tag, visited)
        # Left
        area += bfs(row, col - 1, num_rows, num_cols, grid, tag, visited)

        return area + 1

    return 0

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

    grid = [[0 for point in range(width)] for x in range(height)]
    
    for row in range(height):

        for column in range(width):

            current = (min_x + column, min_y + row)
            min_distance = manhattan(current, points[0])

            for point in range(len(points)):

                distance = manhattan(current, points[point])

                if distance == 0:

                    grid[row][column] = point
                    break

                if distance < min_distance:

                    min_distance = distance
                    grid[row][column] = point

            count = 0

            for point in range(len(points)):

                distance = manhattan(current, points[point])

                if distance == min_distance:

                    count += 1

            if count > 1: 

                grid[row][column] = -1

    visited = [[False for point in range(width)] for x in range(height)]

    points_areas = [0 for i in range(len(points))]

    for row in range(height):

        for col in range(width):

            if grid[row][col] != -1 and visited[row][col] == False:

                global infinite
                infinite = False
                area = bfs(row, col, height, width, grid, grid[row][col], visited)

                if not infinite:
                    points_areas[grid[row][col]] += area

    print(max(points_areas))

sol()
