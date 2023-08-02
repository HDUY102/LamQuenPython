from collections import defaultdict


class Graph:
    """
    Create graph for condition statements
    Ex: A -> B
    """

    def __init__(self):
        self.graph = defaultdict(list)

    def add_condition_statement(self, arg1, arg2):
        self.graph[arg1].append(arg2)

    def print_graph(self):
        for k, v in self.graph.items():
            print(k)
            for i in v:
                print(' |-> ' + i)
            print('\n')

    def get_graph(self):
        return self.graph


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None


def law_of_syllogism(graph, start, dest):

    queue = []
    tree = {}

    flag = None

    visited = []

    # Create BFS tree
    tree[start] = Node(start)

    queue.append(start)
    visited.append(start)

    while queue:
        s = queue.pop(0)

        for i in graph[s]:
            if i not in visited:
                queue.append(i)
                visited.append(i)
                # Add adjacent to Tree BFS
                tree[i] = Node(i)
                tree[i].parent = tree[s]

    if dest not in tree.keys():
        flag = False
    else:
        flag = True

    return flag


def modus_ponens(graph, arg1, arg2, antecedent_list):
    premise = '1. ' + arg1 + ' -> ' + arg2 + '\n' + \
        '2. ' + arg1 + '\n' + '-' * 20 + '\n' + '3. '

    if not law_of_syllogism(graph, arg1, arg2):
        return "Don't exist the conclusion"
    else:
        if arg1 not in antecedent_list:
            return "Don't exist the conclusion"
        else:
            return premise + arg2


def modus_tollens(graph, arg1, arg2, negative_consequent_list):
    premise = '1. ' + arg1 + ' -> ' + arg2 + '\n' + \
        '2. ¬' + arg2 + '\n' + '-' * 20 + '\n' + '3. '

    if not law_of_syllogism(graph, arg1, arg2):
        return "Don't exist the conclusion"
    else:
        if arg2 not in negative_consequent_list:
            return "Don't exist the conclusion"
        else:
            return premise + '¬' + arg1


if __name__ == '__main__':
    g = Graph()
    g.add_condition_statement('P', 'Q')
    g.add_condition_statement('Q', 'R')
    ant_list = ['P', 'Q']

    cons_list = ['Q', 'R']

    conclusion1 = modus_ponens(g.get_graph(), 'P', 'R', ant_list)
    print(conclusion1)

    print('\n\n')

    conclusion2 = modus_ponens(g.get_graph(), 'P', 'K', ant_list)
    print(conclusion2)

    print('\n\n')

    conclusion3 = modus_tollens(g.get_graph(), 'P', 'Q', cons_list)
    print(conclusion3)

    print('\n\n')

    conclusion4 = modus_tollens(g.get_graph(), 'P', 'A', cons_list)
    print(conclusion4)
