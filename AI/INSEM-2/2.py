def print_puzzle(puzzle):
    for i in range(9):
        if i % 3 == 0 and i > 0:
            print("")  
        print(str(puzzle[i]) + " ", end="") 
    print("")

# Function to calculate heuristic (misplaced tiles)
def calculate_heuristic(state, goal_state):
    heuristic = 0
    for i in range(9):
        if state[i] != 0 and state[i] != goal_state[i]:
            heuristic += 1
    return heuristic 

# Function to find the best move for the blank tile (0)
def find_best_move(possible_moves, zero_position, current_state, goal_state):
    min_heuristic = float('inf')  
    best_state = current_state.copy()

    for move in possible_moves: 
        temp_state = current_state.copy() 
        temp_state[zero_position], temp_state[move] = temp_state[move], temp_state[zero_position]
        current_heuristic = calculate_heuristic(temp_state, goal_state)
        if current_heuristic < min_heuristic:
            min_heuristic = current_heuristic
            best_state = temp_state.copy()

    return best_state, min_heuristic

def get_puzzle_state(prompt):
    while True:
        try:
            state = list(map(int, input(prompt).split()))
            if len(state) == 9 and set(state) == set(range(9)):
                return state
            else:
                print("Invalid input. Please enter 9 unique numbers (0-8).")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

print("8-Puzzle Solver")
print("Enter the puzzle states as 9 space-separated integers (0-8), where 0 represents the blank tile.")

initial_state = get_puzzle_state("Enter the initial state: ")
goal_state = get_puzzle_state("Enter the goal state: ")

# Initial heuristic value (misplaced tiles)

heuristic_value = calculate_heuristic(initial_state, goal_state)
level = 1  

# Print the initial state of the puzzle
print("\n------ Level " + str(level) + " ------")
print_puzzle(initial_state)
print("Misplaced Tiles: " + str(heuristic_value))
current_state = initial_state
while heuristic_value > 0:
    zero_position = current_state.index(0)
    level += 1
    if zero_position == 0:
        possible_moves = [1, 3]
    elif zero_position == 1:
        possible_moves = [0, 2, 4]
    elif zero_position == 2:
        possible_moves = [1, 5]
    elif zero_position == 3:
        possible_moves = [0, 4, 6]
    elif zero_position == 4:
        possible_moves = [1, 3, 5, 7]
    elif zero_position == 5:
        possible_moves = [2, 4, 8]
    elif zero_position == 6:
        possible_moves = [3, 7]
    elif zero_position == 7:
        possible_moves = [4, 6, 8]
    elif zero_position == 8:
        possible_moves = [5, 7]
    current_state, heuristic_value = find_best_move(possible_moves, zero_position, current_state, goal_state)
    print("\n------ Level " + str(level) + " ------")
    print_puzzle(current_state)
    print("Misplaced Tiles: " + str(heuristic_value))

print("\nPuzzle solved!")
