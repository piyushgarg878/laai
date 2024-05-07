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

def recursive_dls(state, goal, actions, depth):
    if state == goal:
        return [state]
    if depth <= 0:
        return None

    for action in actions(state):
        new_state = apply_action(state, action)
        result = recursive_dls(new_state, goal, actions, depth - 1)
        if result is not None:
            return [state] + result
    return None

def depth_limited_dfs(state, goal, actions, depth):
    return recursive_dls(state, goal, actions, depth)

def iterative_deepening(initial, goal, actions):
    depth = 0
    while True:
        result = depth_limited_dfs(initial, goal, actions, depth)
        if result is not None:
            return result
        depth += 1

initial_state = {'A': 'table', 'B': 'table', 'C': 'B'}
goal_state = {'A': 'table', 'B': 'A', 'C': 'B'}

result_ids = iterative_deepening(initial_state, goal_state, actions)

if result_ids is not None:
    for state in result_ids:
        print(state)
    print("Goal achieved at depth:", len(result_ids) - 1)
else:
    print("No solution found.")
