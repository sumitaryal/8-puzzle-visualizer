import heapq
from helper import apply_action, get_actions, manhattan_distance

def a_star(initial_state, goal_state):
    """
    Finds a path from initial_state to goal_state using A* search.
    Returns the path as a list of actions (e.g., ["Up", "Left", "Down"]).
    If no path is found, returns None.
    """
    queue = [(manhattan_distance(initial_state, goal_state), initial_state, [])]
    visited = set()

    while queue:
        _, state, actions = heapq.heappop(queue)

        if state == goal_state:
            return actions

        if state in visited:
            continue
        visited.add(state)

        for action in get_actions(state):
            new_state = apply_action(state, action)
            if new_state in visited:
                continue
            new_actions = actions + [action]
            new_cost = len(new_actions) + manhattan_distance(new_state, goal_state)
            heapq.heappush(queue, (new_cost, new_state, new_actions))

    return None