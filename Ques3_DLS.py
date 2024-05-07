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

def dls(state, goal, actions, depth):
    if state == goal:
        return [state]
    if depth <= 0:
        return None

    for action in actions(state):
        new_state = apply_action(state, action)
        result = dls(new_state, goal, actions, depth - 1)
        if result is not None:
            return [state] + result
    return None

initial_state = {'A': 'table', 'B': 'table', 'C': 'A'}
goal_state = {'A': 'table', 'B': 'A', 'C': 'B'}

result_dls = dls(initial_state, goal_state, actions, depth=1)

if result_dls is not None:
    for state in result_dls:
        print(state)
    print("Complete for depth=1")
else:
    print("No solution found for depth=1. Incomplete.")
