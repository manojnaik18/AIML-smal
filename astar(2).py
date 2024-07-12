  def heuristic(n):
        H_dist = {'A': 11, 'B': 6, 'C': 5, 'D': 7, 'E': 3, 'F': 6, 'G': 5, 'H': 3, 'I': 1, 'J': 0}
        return H_dist[n]


def a_star(start, stop, graph):
    open_set = {start}
    g = {start: 0}
    parents = {start: None}

    while open_set:
        n = min(open_set, key=lambda v: g[v] + heuristic(v))
        if n == stop:
            path = []
            while n:
                path.append(n)
                n = parents[n]
            return path[::-1]

        open_set.remove(n)
        for (m, weight) in graph.get(n, []):
            new_g = g[n] + weight
            if m not in g or new_g < g[m]:
                g[m] = new_g
                parents[m] = n
                open_set.add(m)

    return "Path does not exist!"

graph = {
    'A': [('B', 6), ('F', 3)], 
    'B': [('A', 6), ('C', 3), ('D', 2)], 
    'C': [('B', 3), ('D', 1), ('E', 5)],
    'D': [('B', 2), ('C', 1), ('E', 8)], 
    'E': [('C', 5), ('D', 8), ('I', 5), ('J', 5)],
    'F': [('A', 3), ('G', 1), ('H', 7)],
    'G': [('F', 1), ('I', 3)], 
    'H': [('F', 7), ('I', 2)], 
    'I': [('E', 5), ('G', 3), ('H', 2), ('J', 3)]
}

print(a_star('A', 'J', graph))
