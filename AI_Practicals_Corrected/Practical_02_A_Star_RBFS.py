# PRACTICAL NO. 02
# AIM: To implement A* Search and Recursive Best-First Search (RBFS).

import heapq
import math

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2, 'G': 3},
    'E': {'B': 5, 'G': 2},
    'F': {'C': 3, 'G': 2},
    'G': {}
}

h = {'A': 6, 'B': 4, 'C': 4, 'D': 3, 'E': 2, 'F': 2, 'G': 0}
start = 'A'
goal = 'G'

def a_star():
    # Each entry: (estimated total cost, actual cost, node, path)
    queue = [(h[start], 0, start, [start])]
    best_cost = {start: 0}

    while queue:
        f, cost, node, path = heapq.heappop(queue)

        if cost > best_cost.get(node, math.inf):
            continue
        if node == goal:
            return path, cost

        for neighbor, distance in graph[node].items():
            new_cost = cost + distance
            if new_cost < best_cost.get(neighbor, math.inf):
                best_cost[neighbor] = new_cost
                heapq.heappush(
                    queue,
                    (new_cost + h[neighbor], new_cost, neighbor, path + [neighbor])
                )
    return None, math.inf

def rbfs(node, cost, path, f_limit, f_value):
    if node == goal:
        return path, cost, f_value

    successors = []
    for neighbor, distance in graph[node].items():
        if neighbor not in path:
            new_cost = cost + distance
            estimate = max(new_cost + h[neighbor], f_value)
            successors.append([estimate, neighbor, new_cost, path + [neighbor]])

    if not successors:
        return None, math.inf, math.inf

    while successors:
        successors.sort(key=lambda item: item[0])
        best = successors[0]

        if best[0] > f_limit:
            return None, math.inf, best[0]

        alternative = successors[1][0] if len(successors) > 1 else math.inf
        result_path, result_cost, new_f = rbfs(
            best[1], best[2], best[3], min(f_limit, alternative), best[0]
        )
        successors[0][0] = new_f

        if result_path is not None:
            return result_path, result_cost, new_f

    return None, math.inf, math.inf

a_path, a_cost = a_star()
r_path, r_cost, _ = rbfs(start, 0, [start], math.inf, h[start])

print("A* Search")
print("Path:", a_path)
print("Cost:", a_cost)

print("\nRBFS")
print("Path:", r_path)
print("Cost:", r_cost)
