class Node:
    def __init__(self, state, operator, children):
        self.state = state
        self.operator = operator
        self.children = children


def is_goal(state):
    return state == "Goal"


def breadth_first_search(start_node):
    queue = [start_node]

    while queue:
        current_node = queue.pop(0)

        if is_goal(current_node.state):
            return current_node.state

        if current_node.operator == "And":
            queue.extend(current_node.children)
        elif current_node.operator == "Or":
            for child in current_node.children:
                queue.insert(0, child)

# Example of using the algorithm


A = Node("A", "Proposition", [])
B = Node("B", "Proposition", [])
C = Node("C", "Proposition", [])

Or_node = Node("Or", "Or", [B, C])
And_node = Node("And", "And", [A, Or_node])

result = breadth_first_search(And_node)
print(result)  # Output: "Goal"
