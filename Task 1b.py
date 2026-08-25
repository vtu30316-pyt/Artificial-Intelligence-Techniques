def dfs(graph, folder, visited):
    visited.add(folder)
    print(folder, end=" ")

    for subfolder in graph.get(folder, []):
        if subfolder not in visited:
            dfs(graph, subfolder, visited)

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

visited = set()

print("DFS Folder Traversal:")
dfs(graph, "Root", visited)
