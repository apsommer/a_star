import math

def shortest_path(M, start, goal):

    adjacency = M.roads
    positions = M.intersections

    x_goal = positions[goal][0]
    y_goal = positions[goal][1]

    frontier = [(0, 0, 0, start, [])]
    path = []

    while len(frontier) > 0:

        cost_path, cost_step, cost_estimate, node, path = frontier.pop()
        path.append(node)

        if node == goal:
            return path

        x_node = positions[node][0]
        y_node = positions[node][1]
        neighbors = adjacency[node]

        for neighbor in neighbors:

            if neighbor in path:
                continue

            x_neighbor = positions[neighbor][0]
            y_neighbor = positions[neighbor][1]

            g = cost_step + math.sqrt((x_neighbor - x_node)**2 + (y_neighbor - y_node)**2)
            h = math.sqrt((x_neighbor - x_goal)**2 + (y_neighbor - y_goal)**2)
            f = g + h

            frontier.append((f, g, h, neighbor, path.copy()))

        frontier.sort(key = lambda x: x[0], reverse = True)

    print("nothing found")

            
