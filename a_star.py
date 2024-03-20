from queue import PriorityQueue

class PuzzleNode:
   
    def __init__(self, state, parent=None, cost=0, heuristic=0):
       
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
      
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def get_blank_position(state):

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def a_star_search(initial_state, goal_state):

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    moves = ['RIGHT', 'LEFT', 'DOWN', 'UP']

    def calculate_heuristic(state, goal_state):
 
        heuristic = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != goal_state[i][j]:
                    x, y = divmod(state[i][j] - 1, 3)
                    heuristic += abs(x - i) + abs(y - j)
        return heuristic

    initial_node = PuzzleNode(initial_state)
    initial_node.heuristic = calculate_heuristic(initial_state, goal_state)

    priority_queue = PriorityQueue()
    priority_queue.put(initial_node)

    while not priority_queue.empty():
        current_node = priority_queue.get()

        if current_node.state == goal_state:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        blank_row, blank_col = get_blank_position(current_node.state)

        for direction, move in zip(directions, moves):
            new_state = [row[:] for row in current_node.state]
            new_row, new_col = blank_row + direction[0], blank_col + direction[1]

            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state[blank_row][blank_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_row][blank_col]
                new_node = PuzzleNode(new_state, current_node, current_node.cost + 1)
                new_node.heuristic = calculate_heuristic(new_state, goal_state)
                priority_queue.put(new_node)

    return None

# Example of using the a_star_search function:

initial = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
goal = [[1, 2, 3], [4, 5, 0], [6, 7, 8]]

path_to_goal = a_star_search(initial, goal)
if path_to_goal:
    print("Path to reach the goal state:")
    for idx, state in enumerate(path_to_goal):
        print(f"Step {idx + 1}:")
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")