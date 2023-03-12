from collections import deque
from helper import apply_action, get_actions

def bfs(initial_state, goal_state):
    """
    Finds a path from initial_state to goal_state using breadth-first search.
    Returns the path as a list of actions (e.g., ["Up", "Left", "Down"]).
    If no path is found, returns None.
    """
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        state, actions = queue.popleft()

        if state == goal_state:
            return actions

        for action in get_actions(state):
            new_state = apply_action(state, action)

            if tuple(map(tuple, new_state)) not in visited:
                visited.add(tuple(map(tuple, new_state)))
                queue.append((new_state, actions + [action]))

    return None