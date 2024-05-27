"""Наступний код виконує побудову бінарних дерев. Виконайте аналіз коду, щоб зрозуміти, як він працює.

Використовуючи як базу цей код, побудуйте функцію, що буде візуалізувати бінарну купу.
"""

import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def build_min_heap(array):
    """Функція для побудови мінімальної бінарної купи з масиву."""
    n = len(array)
    nodes = [Node(val) for val in array]

    # Перетворення масиву в мінімальну купу
    for i in range(n // 2 - 1, -1, -1):
        heapify(nodes, n, i)

    # Встановлення посилань на лівих і правих дітей
    for i in range(n):
        if 2 * i + 1 < n:
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < n:
            nodes[i].right = nodes[2 * i + 2]

    return nodes[0] if nodes else None

def heapify(nodes, n, i):
    """Допоміжна функція для забезпечення властивостей мінімальної купи."""
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and nodes[left].val < nodes[smallest].val:
        smallest = left
    if right < n and nodes[right].val < nodes[smallest].val:
        smallest = right

    if smallest != i:
        nodes[i].val, nodes[smallest].val = nodes[smallest].val, nodes[i].val  # Обмін значеннями
        heapify(nodes, n, smallest)

# Приклад використання
array = [10, 20, 5, 6, 1, 8, 9, 4]
min_heap_root = build_min_heap(array)

# Відображення бінарної купи
draw_tree(min_heap_root)
