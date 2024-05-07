from collections import deque

def actions(state):
  possible_actions = []
  for block,location in state.items():
    if location != 'table':
      possible_actions.append((block,'table'))
    for other_block,other_location in state.items():
      if other_block!=block and other_location != 'table':
        possible_actions.append((block,other_block))
  return possible_actions

def apply_action(state,action):
  block , location  = action
  new_state = state.copy()
  new_state[block]=location
  return new_state

def bfs(initial, goal, actions):
    queue = deque([(initial, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path + [state]

        visited.add(tuple(state.items()))

        for action in actions(state):
            new_state = apply_action(state, action)
            if tuple(new_state.items()) not in visited:
                queue.append((new_state, path + [state]))

    return None

initial_state = {'A': 'table', 'B': 'table', 'C': 'B'}
goal_state = {'A': 'table', 'B': 'A', 'C': 'B'}

result_bfs = bfs(initial_state, goal_state, actions)

if result_bfs is not None:
    for state in result_bfs:
        print(state)
else:
    print("No solution found.")
