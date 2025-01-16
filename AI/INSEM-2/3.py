import heapq

def dijkstra(graph, start):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    shortest_distances = {node: float('inf') for node in graph}
    shortest_distances[start] = 0
    previous_nodes = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > shortest_distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_distances, previous_nodes

def reconstruct_path(previous_nodes, start, target):
    path = []
    current_node = target

    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]

    path.reverse()
    return path if path[0] == start else []

# Get graph input from the user
def get_graph_input():
    print("Enter the graph as adjacency list:")
    print("Example input format: A B 1, A C 4, B C 2, B D 5, C D 1")
    graph_input = input("Enter edges (node1 node2 weight, ...): ")
    graph = {}
    edges = graph_input.split(",")

    for edge in edges:
        node1, node2, weight = edge.strip().split()
        weight = int(weight)

        if node1 not in graph:
            graph[node1] = []
        if node2 not in graph:
            graph[node2] = []

        graph[node1].append((node2, weight))
        graph[node2].append((node1, weight))  

    return graph

# Main program
print("Dijkstra's Algorithm - Shortest Path Finder")

graph = get_graph_input()
start_node = input("Enter the start node: ")
target_node = input("Enter the target node: ")

shortest_distances, previous_nodes = dijkstra(graph, start_node)
shortest_path = reconstruct_path(previous_nodes, start_node, target_node)

print("Shortest distances from start node:", shortest_distances)
print(f"Shortest path from {start_node} to {target_node}:", shortest_path)
