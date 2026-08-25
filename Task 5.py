import random
import math

points = [(0, 10), (2, 13), (5, 14), (6, 11), (3, 10)]

n = len(points)
iterations = 5

def dist(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

best_route = None
best_distance = float('inf')

for _ in range(iterations):
    unvisited = list(range(1, n))
    route = [0]

    while unvisited:
        current = route[-1]
        next_point = min(
            unvisited,
            key=lambda x: dist(points[current], points[x])
        )
        route.append(next_point)
        unvisited.remove(next_point)

    route.append(0)

    total = sum(
        dist(points[route[i]], points[route[i+1]])
        for i in range(len(route)-1)
    )

    if total < best_distance:
        best_distance = total
        best_route = route

print("Best Route:", best_route)
print("Minimum Distance:", round(best_distance, 2))
