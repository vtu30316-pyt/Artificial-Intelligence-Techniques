# Graph coloring

graph = {
    1: [2, 3],
    2: [1, 3],
    3: [1, 2, 4],
    4: [3]
}

color = [1, 2, 3, 2]

valid = True

for vertex in graph:
    for neighbour in graph[vertex]:
        if color[vertex - 1] == color[neighbour - 1]:
            valid = False

print(*color)

if valid:
    print("Valid coloring")
else:
    print("Invalid coloring")
