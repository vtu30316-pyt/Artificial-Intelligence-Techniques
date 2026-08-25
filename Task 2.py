import numpy as np

coords = np.array([
    [0,0], [2,5], [5,2], [6,6], [5,3],
    [1,7], [6,3], [3,3], [5,5]
])

names = ["Hotel", "Beach", "Museum", "Temple", "Mountain",
         "Waterfall", "Gallery", "Garden", "Market"]

def get_cost(route):
    full = [0] + route + [0]
    return sum(np.linalg.norm(coords[full[i]] - coords[full[i+1]])
               for i in range(len(full)-1))

tour = list(range(1,9))
np.random.shuffle(tour)
cost = get_cost(tour)

print("Initial Route:", "Hotel ->",
      " -> ".join(names[i] for i in tour), "-> Hotel")
print(f"Initial Distance: {cost:.2f}\n")

iteration = 1

while True:
    improved = False

    for i in range(len(tour)):
        for j in range(i+1, len(tour)):
            neighbor = tour.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            n_cost = get_cost(neighbor)

            if n_cost < cost:
                tour, cost, improved = neighbor, n_cost, True

    if not improved:
        break

    iteration += 1

print("=" * 40)
print("OPTIMAL TRAVEL ROUTE FOUND")
print("=" * 40)
print("Hotel ->", " -> ".join(names[i] for i in tour), "-> Hotel")
print(f"Minimum Distance: {cost:.2f}")
