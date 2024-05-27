import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

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

def draw_tree(tree, pos, title):
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.suptitle(title, x=0.2, y=0.9)  # Встановлення заголовку
    plt.show()

def update_node_color(tree, node_id, color):
    tree.nodes[node_id]['color'] = color

def count_nodes(node):
    """Рекурсивно підраховує кількість вузлів у дереві."""
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def generate_colors(n):
    """Генерація кольорів від темних до світлих."""
    return [f"#{i:02x}{i:02x}{i:02x}" for i in range(0, 256, 256 // n)]

def bfs(root, tree, pos, colors):
    """Обхід дерева в ширину (BFS) з візуалізацією."""
    if not root:
        return
    queue = deque([root])
    level = 0
    color_index = 0
    
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            update_node_color(tree, node.id, colors[color_index])
            color_index += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1

def dfs(root, tree, pos, colors, color_index=0):
    """Обхід дерева в глибину (DFS) з візуалізацією."""
    if not root:
        return color_index
    update_node_color(tree, root.id, colors[color_index])
    color_index += 1
    if root.left:
        color_index = dfs(root.left, tree, pos, colors, color_index)
    if root.right:
        color_index = dfs(root.right, tree, pos, colors, color_index)
    return color_index

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення початкового дерева
tree = nx.DiGraph()
pos = {root.id: (0, 0)}
tree = add_edges(tree, root, pos)
draw_tree(tree, pos, "Бінарне дерево")

# Виконання обходу в ширину (BFS) з візуалізацією
node_count = count_nodes(root)
colors = generate_colors(node_count)  # Генерація кольорів на основі кількості вузлів
bfs(root, tree, pos, colors)
draw_tree(tree, pos, "Обхід дерева в ширину (BFS)")

# Перестворення дерева для DFS обходу
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Виконання обходу в глибину (DFS) з візуалізацією
tree = nx.DiGraph()
pos = {root.id: (0, 0)}
tree = add_edges(tree, root, pos)
colors = generate_colors(node_count)  # Генерація кольорів для обходу
dfs(root, tree, pos, colors)
draw_tree(tree, pos, "Обхід дерева в глибину (DFS)")
