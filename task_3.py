import heapq
import networkx as nx
import matplotlib.pyplot as plt


def dijkstra(graph, start_point):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start_point] = 0

    queue = [(0, start_point)]

    while queue:
        # беремо найменший елемент купи
        current_distance, current_vertex = heapq.heappop(queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


def main():
    graph = {
        "Kyiv": {"Vinnytsia": 5, "Lutks": 10},
        "Vinnytsia": {"Kyiv": 5, "Ternopil": 3},
        "Lutks": {"Kyiv": 10, "Ternopil": 2},
        "Ternopil": {"Vinnytsia": 3, "Lutks": 2, "Lviv": 4},
        "Lviv": {"Ternopil": 4},
    }

    start_point = "Kyiv"
    short_distances = dijkstra(graph, start_point)
    print(f"Початкова вершина {start_point}")

    result = 0
    for vertex, distance in short_distances.items():
        result += distance
        print(f"{vertex}: {distance}", end=" ")
    print(
        f"\nНайкоротших шляхів від початкової вершини {start_point} до всіх інших складає:",
        result,
    )

    G = nx.Graph()

    G.add_nodes_from(graph.keys())
    for key, neighbors in graph.items():
        for neighbor in neighbors.items():
            G.add_edge(key, neighbor[0], weight=neighbor[1])

    pos = nx.fruchterman_reingold_layout(G, iterations=100, k=0.3)

    nx.draw_networkx_nodes(G, pos, node_size=800, node_color="skyblue")
    nx.draw_networkx_labels(G, pos, font_size=12)

    nx.draw_networkx_edges(G, pos, width=1)
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

    plt.show()


if __name__ == "__main__":
    main()
