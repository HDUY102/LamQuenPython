class Node:
    def __init__(self, state, parent=None, g_cost=0, final_state=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.g_cost = g_cost
        self.h_cost = h_cost(state, final_state)
        self.f_cost = self.g_cost + self.h_cost


def h_cost(state, final_state):
    num_disks_left = len(state[0])
    return num_disks_left


def move_disc(source, target):
    if source and (not target or source[-1] < target[-1]):
        target.append(source.pop())


def generate_children(node):
    for i in range(3):
        for j in range(3):
            if i != j:
                child_state = [list(peg) for peg in node.state]
                move_disc(child_state[i], child_state[j])
                if child_state != node.state:
                    node.children.append(Node(child_state, parent=node))


def a_star_search(initial_state, final_state):
    open_list = [Node(initial_state, final_state=final_state)]
    closed_list = set()

    while open_list:
        node = min(open_list, key=lambda n: n.f_cost)
        open_list.remove(node)
        closed_list.add(tuple(map(tuple, node.state)))

        if node.state == final_state:
            return node

        generate_children(node)
        for child in node.children:
            if tuple(map(tuple, child.state)) not in closed_list:
                open_list.append(child)

    return None

# Dẫn đường


def print_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    for step, state in reversed(list(enumerate(path))):
        print(f"Bước {len(path) - step -1}: {state}")


def generate_disks(num_disks):
    return list(range(num_disks, 0, -1))


def initialize_state():
    num_disks = int(input("Nhập số lượng đĩa: "))
    initial_state = [generate_disks(num_disks), [], []]  # Trạng thái ban đầu
    return initial_state


def main():
    initial_state = initialize_state()
    final_state = [[], [], initial_state[0]]

    result_node = a_star_search(initial_state, final_state)

    if result_node:
        print('Đã đạt được trạng thái đích')
        print_path(result_node)
    else:
        print('Không tìm thấy đường dẫn đến trạng thái đích')


if __name__ == '__main__':
    main()
