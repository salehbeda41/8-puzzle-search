from queue import PriorityQueue

class PuzzleNode:
   
    ##Class to represent a node in the 8 Puzzle problem.

    def __init__(self, state, parent=None, cost=0, heuristic=0):
        ##Constructor to instantiate a PuzzleNode object.
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        ##Less than comparison method used for PriorityQueue ordering.
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def get_blank_position(state):
    ##Helper function to get the position of the blank (zero) in the puzzle board.
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def h(state, goal):
    ##Heuristic function to calculate the Manhattan distance between the current state and the goal state.
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                x, y = divmod(state[i][j] - 1, 3)
                distance += abs(x - i) + abs(y - j)
    return distance

def get_children(node):
    #Function to generate child nodes from a given parent node.
    
    children = []
    row, col = get_blank_position(node.state)

    for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_state = [row[:] for row in node.state]
        if 0 <= row + i < 3 and 0 <= col + j < 3:
            new_state[row][col], new_state[row + i][col + j] = new_state[row + i][col + j], new_state[row][col]
            children.append(PuzzleNode(new_state, parent=node, cost=node.cost + 1, heuristic=h(new_state, goal)))

    return children

def greedy_search(start_state, goal_state):
   ## Function to solve the 8 Puzzle problem using Greedy Search.
    
    start_node = PuzzleNode(start_state, heuristic=h(start_state, goal_state))
    frontier = PriorityQueue()
    frontier.put(start_node)

    while not frontier.empty():
        current_node = frontier.get()

        if current_node.state == goal_state:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        for child in get_children(current_node):
            frontier.put(child)

    return None

# Example of using the greedy_search function:

start = [[1, 2, 3], [0, 6, 5], [7, 4, 8]]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
path_to_goal = greedy_search(start, goal)
print("Path from start to goal:")
for state in path_to_goal:
    for row in state:
        print(row)
    print()