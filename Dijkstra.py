import heapq

def dijkstra(graph, start):
    # Priority queue to store (cost, node)
    queue = [(0, start)]
    shortest_path = {start: 0}
    visited = set()

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if neighbor not in shortest_path or distance < shortest_path[neighbor]:
                shortest_path[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return shortest_path

# Example graph as an adjacency list
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('C', 3)],
    'C': []
}

start_node = 'A'
print("Shortest paths from A:", dijkstra(graph, start_node))
