import heapq
from helper import apply_action, get_actions, number_of_misplaced_tiles

def greedy(initial_state, goal_state):
    """
    Finds a path from initial_state to goal_state using greedy best-first search with the Manhattan distance heuristic.
    Returns the path as a list of actions (e.g., ["Up", "Left", "Down"]).
    If no path is found, returns None.
    """
    queue = [(number_of_misplaced_tiles(initial_state, goal_state), initial_state, [])]
    visited = set()

    while queue:
        _, state, actions = heapq.heappop(queue)

        if state == goal_state:
            return actions

        if tuple(map(tuple, state)) in visited:
            continue

        visited.add(tuple(map(tuple, state)))

        for action in get_actions(state):
            new_state = apply_action(state, action)

            if tuple(map(tuple, new_state)) not in visited:
                heapq.heappush(queue, (number_of_misplaced_tiles(new_state, goal_state), new_state, actions + [action]))

    return None