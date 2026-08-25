import heapq

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('C', 1), ('D', 7)],
    'C': [('F', 5)],
    'D': [('G', 1)],
    'E': [('G', 6)],
    'F': [('G', 2)]
}

heuristic = {
    'A': 7, 'B': 6, 'C': 4, 'D': 1,
    'E': 3, 'F': 2, 'G': 0
}

def astar(start, goal):
    queue = [(heuristic[start], 0, start, [start])]
    visited = set()

    while queue:
        f, cost, node, path = heapq.heappop(queue)

        if node == goal:
            return path, cost

        if node in visited:
            continue
        visited.add(node)

        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                new_cost = cost + weight
                heapq.heappush(
                    queue,
                    (new_cost + heuristic[neighbor],
                     new_cost, neighbor, path + [neighbor])
                )

path, cost = astar('A', 'G')

print("Path:", " -> ".join(path))
print("Total Cost:", cost)
