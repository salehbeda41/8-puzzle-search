from queue import Queue
import threading

class PuzzleTile:
    
    def __init__(self, state, parent=None, action=""):
        self.state = state
        self.parent = parent
        self.action = action

def explore_breadth_first(initial_state):
    
    def determine_valid_moves(tile):
      
        moves = []
        zero_index = tile.state.index(0)
        zero_row, zero_col = zero_index // 3, zero_index % 3

        if zero_row > 0:
            moves.append('Move UP')
        if zero_row < 2:
            moves.append('Move DOWN')
        if zero_col > 0:
            moves.append('Move LEFT')
        if zero_col < 2:
            moves.append('Move RIGHT')

        return moves

    def execute_move(state, move):
        new_state = state.copy()
        zero_index = new_state.index(0)
        zero_row, zero_col = zero_index // 3, zero_index % 3

        if move == 'Move UP':
            new_state[zero_index], new_state[zero_index - 3] = new_state[zero_index - 3], new_state[zero_index]
        elif move == 'Move DOWN':
            new_state[zero_index], new_state[zero_index + 3] = new_state[zero_index + 3], new_state[zero_index]
        elif move == 'Move LEFT':
            new_state[zero_index], new_state[zero_index - 1] = new_state[zero_index - 1], new_state[zero_index]
        elif move == 'Move RIGHT':
            new_state[zero_index], new_state[zero_index + 1] = new_state[zero_index + 1], new_state[zero_index]

        return new_state

    def display_moves(tile):
        moves = []
        while tile.parent is not None:
            moves.append(tile.action)
            tile = tile.parent

        moves.reverse()
        print("Sequence of moves:")
        for move in moves:
            print(move)

    def solve_puzzle():
        q = Queue()
        visited = set()

        root = PuzzleTile(initial_state)
        q.put(root)
        visited.add(tuple(initial_state))

        while not q.empty():
            tile = q.get()

            if tile.state == target_state:
                print("Puzzle Solved!")
                display_moves(tile)
                return

            for move in determine_valid_moves(tile):
                new_state = execute_move(tile.state, move)
                if tuple(new_state) not in visited:
                    new_tile = PuzzleTile(new_state, tile, move)
                    q.put(new_tile)
                    visited.add(tuple(new_state))

    # Define the target state for the 8 Puzzle
    target_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    # Start solving the puzzle using multiple threads
    thread1 = threading.Thread(target=solve_puzzle)
    thread2 = threading.Thread(target=solve_puzzle)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

# Example of using the explore_breadth_first function to solve the 8 Puzzle
initial_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]
explore_breadth_first(initial_state)