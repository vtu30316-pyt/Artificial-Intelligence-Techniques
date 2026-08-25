import heapq

graph = {
    'A': [('B', 4), ('C', 3)],
    'B': [('D', 5), ('E', 2)],
    'C': [('F', 4)],
    'D': [('G', 3)],
    'E': [('G', 9), ('F', 2)],
    'F': [('G', 3)],
    'G': []
}

h = {'A': 11, 'B': 6, 'C': 7, 'D': 3, 'E': 4, 'F': 3, 'G': 0}

def astar(start, goal):
    q = [(h[start], 0, start, [start])]

    while q:
        f, cost, node, path = heapq.heappop(q)

        if node == goal:
            return path, cost

        for next_node, d in graph[node]:
            new_cost = cost + d
            heapq.heappush(q, (
                new_cost + h[next_node],
                new_cost,
                next_node,
                path + [next_node]
            ))

path, cost = astar('A', 'G')

print("Shortest Path:", " -> ".join(path))
print("Distance:", cost, "m")
