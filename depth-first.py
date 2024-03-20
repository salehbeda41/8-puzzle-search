from collections import deque

class PuzzleNode:
    #Class to represent a node in the 8 Puzzle problem.
    def __init__(self, state, parent=None):
       # Constructor to instantiate a PuzzleNode object.
        self.state = state
        self.parent = parent

def get_blank_position(state):
    #Helper function to get the position of the blank (zero) tile in the puzzle.
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
            
def get_children(node):
    #Function to generate child nodes from a given node by moving the blank tile.

    children = []
    row, col = get_blank_position(node.state)
    for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_state = [row[:] for row in node.state]
        if 0 <= row + i < 3 and 0 <= col + j < 3:
            new_state[row][col], new_state[row + i][col + j] = new_state[row + i][col + j], new_state[row][col]
            children.append(PuzzleNode(new_state, parent=node))
    return children

def depth_first_search(initial_state):
    #Function to solve the 8 Puzzle problem using Depth First Search algorithm.

    initial_node = PuzzleNode(initial_state)
    stack = [initial_node]
    visited = set()
    while stack:
        current_node = stack.pop()
        visited.add(tuple(map(tuple, current_node.state)))
        if current_node.state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]
        for child in get_children(current_node):
            if tuple(map(tuple, child.state)) not in visited:
                stack.append(child)
    return None
# Example of using the depth_first_search function:
initial_state = [[1, 2, 4], [3, 5, 6], [8, 7, 0]]
solution_path = depth_first_search(initial_state)
if solution_path:
    print("Solution Path:")
    for i, state in enumerate(solution_path):
        print(f"Move {i}:")
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")