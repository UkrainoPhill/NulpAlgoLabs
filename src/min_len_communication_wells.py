def read_input(file_path):
    edges = []
    with open(file_path, 'r') as file:
        for line in file:
            well1, well2, distance = line.strip().split(', ')
            distance = int(distance)
            edges.append((distance, well1, well2))
    return edges


def find(well, parent):
    if parent[well] != well:
        parent[well] = find(parent[well], parent)
    return parent[well]


def union(well1, well2, parent, rank):
    root1 = find(well1, parent)
    root2 = find(well2, parent)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1


def kruskal(edges):
    parent = {}
    rank = {}
    for i, well1, well2 in edges:
        parent[well1] = well1
        parent[well2] = well2
        rank[well1] = 0
        rank[well2] = 0
    total_distance = 0
    for distance, well1, well2 in sorted(edges):
        if find(well1, parent) != find(well2, parent):
            union(well1, well2, parent, rank)
            total_distance += distance
    roots = set()
    for well in parent:
        roots.add(find(well, parent))
    if len(roots) > 1:
        return -1
    return total_distance
