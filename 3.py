import heapq
import matplotlib.pyplot as plt
import networkx as nx

def dijkstra(graph, start):
    # Ініціалізація відстаней до всіх вершин як нескінченності
    distances = {vertex: float('inf') for vertex in graph}
    # Відстань до стартової вершини дорівнює 0
    distances[start] = 0
    # Ініціалізація пріоритетної черги
    priority_queue = [(0, start)]
    shortest_path_tree = {}  # Для збереження шляху
    visited = set()  # Для збереження відвіданих вершин

    while priority_queue:
        # Вилучаємо вершину з мінімальною відстанню
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо поточна вершина вже відвідана, пропускаємо
        if current_vertex in visited:
            continue

        # Відмічаємо вершину як відвідану
        visited.add(current_vertex)

        # Оновлення відстаней до сусідніх вершин
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Якщо знайдена коротша відстань, оновлюємо
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                shortest_path_tree[neighbor] = current_vertex

    return distances, shortest_path_tree

# Приклад використання
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1, 'E': 3},
    'D': {'B': 5, 'C': 1, 'E': 2},
    'E': {'C': 3, 'D': 2, 'F': 1},
    'F': {'E': 1, 'G': 5},
    'G': {'F': 5}
}

start_vertex = 'A'
shortest_paths, shortest_path_tree = dijkstra(graph, start_vertex)

print("Найкоротші шляхи від вершини", start_vertex, "до всіх інших вершин:")
for vertex, distance in shortest_paths.items():
    print(f"Відстань до вершини {vertex}: {distance}")

# Візуалізація графа та найкоротших шляхів
G = nx.DiGraph()

# Додавання вершин та ребер до графа
for vertex in graph:
    G.add_node(vertex)
    for neighbor, weight in graph[vertex].items():
        G.add_edge(vertex, neighbor, weight=weight)

pos = nx.spring_layout(G)  # розташування вершин на площині

# Малювання графа
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Малювання найкоротшого шляху
shortest_path_edges = [(shortest_path_tree[node], node) for node in shortest_path_tree]
nx.draw_networkx_edges(G, pos, edgelist=shortest_path_edges, edge_color='r', width=2)

plt.title('Найкоротші шляхи за допомогою алгоритму Дейкстри')
plt.show()
