from collections import deque
from helper import apply_action, get_actions

def dfs(initial_state, goal_state):
    """
    Finds a path from initial_state to goal_state using depth-first search.
    Returns the path as a list of actions (e.g., ["Up", "Left", "Down"]).
    If no path is found, returns None.
    """
    stack = [(initial_state, [])]
    visited = set()

    while stack:
        state, actions = stack.pop()

        if state == goal_state:
            return actions

        for action in reversed(get_actions(state)):
            new_state = apply_action(state, action)

            if tuple(map(tuple, new_state)) not in visited:
                visited.add(tuple(map(tuple, new_state)))
                stack.append((new_state, actions + [action]))

    return None