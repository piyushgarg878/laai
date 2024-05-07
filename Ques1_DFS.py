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

def dfs(initial,goal,actions,path=[]):
  if initial==goal:
    return path + [initial]
  for action in actions(initial):
    state = apply_action(initial,action)
    if state not in path:
      new_path = dfs(state,goal,actions,path+[state])
      if new_path is not None:
        return new_path

initial_state = {'A': 'B', 'B': 'table', 'C': 'B'}
goal_state = {'A': 'table', 'B': 'A', 'C': 'B'}

result = dfs(initial_state,goal_state,actions)
if result is not None:
    for state in result:
        print(state)
else:
    print("No solution found.")