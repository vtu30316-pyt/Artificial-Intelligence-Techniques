from collections import deque

def bfs(graph, root):
    visited = set()
    queue = deque([root])
    visited.add(root)

    while queue:
        folder = queue.popleft()
        print(folder, end=" ")

        for subfolder in graph.get(folder, []):
            if subfolder not in visited:
                visited.add(subfolder)
                queue.append(subfolder)

graph = {
    "Root": ["Documents", "Pictures", "Downloads"],
    "Documents": ["Assignments", "Projects"],
    "Pictures": ["Photos", "Wallpapers"],
    "Downloads": ["Software", "Videos"],
    "Assignments": [],
    "Projects": [],
    "Photos": [],
    "Wallpapers": [],
    "Software": [],
    "Videos": []
}

print("BFS Folder Traversal:")
bfs(graph, "Root")
