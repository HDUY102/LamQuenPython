import heapq


class Node:
    def __init__(self, state, parent=None, g_score=0, h_score=0):
        self.state = state
        self.parent = parent
        self.g_score = g_score
        self.h_score = h_score
        self.f_score = g_score + h_score

    def __lt__(self, other):
        return self.f_score < other.f_score


def a_star(start_state, goal_state, get_neighbors_fn, heuristic_fn):
    open_set = []
    closed_set = set()

    start_node = Node(start_state, None, 0,
                      heuristic_fn(start_state, goal_state))
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.state == goal_state:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return list(reversed(path))

        closed_set.add(current_node.state)

        for neighbor_state in get_neighbors_fn(current_node.state):
            if neighbor_state in closed_set:
                continue

            g_score = current_node.g_score + 1
            h_score = heuristic_fn(neighbor_state, goal_state)
            # f_score = g_score + h_score

            neighbor_node = Node(
                neighbor_state, current_node, g_score, h_score)

            if neighbor_node not in open_set:
                heapq.heappush(open_set, neighbor_node)

    return None

# Example of using the function
# Hàm heuristic ước tính khoảng cách từ trạng thái hiện tại đến trạng thái kết thúc (Manhattan distance)


def heuristic(state, goal_state):
    return abs(state[0] - goal_state[0]) + abs(state[1] - goal_state[1])

# Hàm trả về các trạng thái hàng xóm của một trạng thái


def get_neighbors(state):
    x, y = state
    neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    return [(nx, ny) for nx, ny in neighbors if 0 <= nx < 5 and 0 <= ny < 5]


start_state = (0, 0)
goal_state = (3, 4)

path = a_star(start_state, goal_state, get_neighbors, heuristic)
print(path)
