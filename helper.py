# Helper functions 
def get_actions(state):
    actions = []

    row, col = find_blank(state)

    if row > 0:
        actions.append("Up")
    if row < 2:
        actions.append("Down")
    if col > 0:
        actions.append("Left")
    if col < 2:
        actions.append("Right")

    return actions


def apply_action(state, action):
    new_state = [row[:] for row in state]

    row, col = find_blank(new_state)

    if action == "Up":
        new_state[row][col], new_state[row-1][col] = new_state[row-1][col], new_state[row][col]
    elif action == "Down":
        new_state[row][col], new_state[row+1][col] = new_state[row+1][col], new_state[row][col]
    elif action == "Left":
        new_state[row][col], new_state[row][col-1] = new_state[row][col-1], new_state[row][col]
    elif action == "Right":
        new_state[row][col], new_state[row][col+1] = new_state[row][col+1], new_state[row][col]

    return new_state


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] is None:
                return i, j

def manhattan_distance(state, goal_state):
    """
    Calculates the Manhattan distance heuristic for the given state and goal state.
    """
    distance = 0

    for i in range(3):
        for j in range(3):
            if state[i][j] is not None:
                row, col = find_tile(goal_state, state[i][j])
                distance += abs(i - row) + abs(j - col)

    return distance

def find_tile(state, tile):
    """
    Returns the row and column indices of the given tile in the given state.
    """
    for i in range(3):
        for j in range(3):
            if state[i][j] == tile:
                return i, j