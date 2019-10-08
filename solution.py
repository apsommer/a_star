# built-in library provides square root function
import math

# shortest path between two nodes in a graph using A*
def shortest_path(M, start, goal):

    # unpack the map input
    adjacency = M.roads
    positions = M.intersections

    # the position of the goal (destination) node is constant
    x_goal = positions[goal][0]
    y_goal = positions[goal][1]

    # track the path of intersections to the goal
    # the frontier is the outer most nodes of the explored region with neighbors that have not yet been considered
    path = []
    frontier = [(start, path, 0, 0)]

    # a simple list is chosen so the minimum cost path can be easily selected
    # this convenience costs O(n) runtime to find the minimum value since every element must be compared

    # a minimum binary heap implementation using the built-in heapq library has better complexity
    # with O(log(n)) for insertion and heapify reorganization after popping the min root

    # loop until either the goal is popped off the frontier, or all nodes have been visited
    while len(frontier) > 0:

        # unpack the frontier tuple and add this node to the path
        node, path, cost_step, cost_path = frontier.pop()
        path.append(node)

        # terminate algorithm if we are at the destination node
        if node == goal:
            print(path) # testing
            return path

        # unpack the coordinates and neighbors for this node
        x_node = positions[node][0]
        y_node = positions[node][1]
        neighbors = adjacency[node]

        # add each neighbor, along with its cost and the path to get there, to the frontier list
        for neighbor in neighbors:

            # small optimization: no reason to go backwards
            if neighbor in path:
                continue

            # unpack the coordinates
            x_neighbor = positions[neighbor][0]
            y_neighbor = positions[neighbor][1]

            # the heart of the A* algorithm: f = g + h
            # f = hueristic for the best path composed of two cost components
            # g = raw path cost for this node = sum of all steps to get to the node
            # h = straight line distance to the goal, this is an "admissable heuristic" since
            # it is always less than the true distance to the goal
            g = cost_step + math.sqrt((x_neighbor - x_node)**2 + (y_neighbor - y_node)**2)
            h = math.sqrt((x_neighbor - x_goal)**2 + (y_neighbor - y_goal)**2)
            f = g + h

            # add this node and its relevant parameters to the frontier
            frontier.append((neighbor, path.copy(), g, f))

        # again, this can be replaced with a minimum binary heap for faster implementation, for now simply find
        # the minimum f to continue with the "best estimated total path cost first"
        frontier.sort(key = lambda x: x[-1], reverse = True)
            
