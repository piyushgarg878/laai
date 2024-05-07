class Node:
    def __init__(self, state, heuristic, node_type):
        self.state = state
        self.heuristic = heuristic
        self.node_type = node_type
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


def ao_star(root_node, goal_state):
    open_list = [(root_node, root_node.heuristic)]
    closed_list = set()

    while open_list:
        current_node, f_value = open_list.pop(0)

        if current_node.state == goal_state:
            return current_node.heuristic

        closed_list.add(current_node)

        for child_node in current_node.children:
            if child_node not in closed_list:
                f_child = child_node.heuristic
                open_list.append((child_node, f_child))
                open_list.sort(key=lambda x: x[1])

    return None


goal_state = 'G'

node_A = Node('A', 100, "")
node_B = Node('B', 6, "AND")
node_C = Node('C', 12, "AND")
node_D = Node('D', 10, "OR")
node_G = Node('G', 5, "")

node_A.add_child(node_B)
node_A.add_child(node_C)
node_A.add_child(node_D)
node_B.add_child(node_G)

min_cost = ao_star(node_A, goal_state)

if min_cost is not None:
    print("Minimum cost to reach the goal node:", min_cost)
else:
    print("Goal node not reachable")
