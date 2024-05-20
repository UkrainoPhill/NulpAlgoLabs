"""
The task is to find the minimum length of communication lines to connect all wells.
The communication lines can be laid only between wells.
"""
from typing import List, Tuple, Dict


def read_input(file_path: str) -> List[Tuple[int, str, str]]:
    """
    Read list of wells and distances between them from the input file

    :param file_path: string, path to the input file
    :return: List of tuples (distance, well1, well2), where each tuple contains distance between well1 and well2,
     and wells themselves
    """
    edges = []
    with open(file_path, 'r') as file:
        for line in file:
            well1, well2, distance = line.strip().split(', ')
            distance = int(distance)
            edges.append((distance, well1, well2))
    return edges


def find(well: str, parents: Dict[str, str]) -> str:
    """
    Find parent of the well in the disjoint set

    :param well: str, well name. Example: 'K1'
    :param parents: dict str: str, dictionary where key is well name and value is parent of this well.
    Example: {'K1': 'K1'}
    :return: str, parent of the well
    """
    if parents[well] != well:
        parents[well] = find(parents[well], parents)
    return parents[well]


def union(well1: str, well2: str, parents: Dict[str, str], rank: Dict[str, int]) -> None:
    """
    Union two wells in the disjoint set

    :param well1: str, well name. Example: 'K1'
    :param well2: str, well name. Example: 'K2'
    :param parents: dict str: str, dictionary where key is well name and value is parent of this well.
     Example: {'K1': 'K1'}
    :param rank: dict str: int, dictionary where key is well name and value is rank of this well. Example: {'K1': 0}
    :return: None, we untie two wells depending on their rank, which is higher we attach to the lower
    """
    root1 = find(well1, parents)
    root2 = find(well2, parents)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parents[root2] = root1
        else:
            parents[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1


def kruskal(edges: List[Tuple[int, str, str]]) -> int:
    """
    Find minimum length of communication lines to connect all wells

    :param edges: list of tuples (distance, well1, well2), where each tuple contains distance between well1 and well2,
     and wells themselves. Example [(1, 'K1', 'K2'), (2, 'K2', 'K3')]
    :return: int, minimum length of communication lines to connect all wells
    """
    parents = {}
    rank = {}
    for i, well1, well2 in edges:
        parents[well1] = well1
        parents[well2] = well2
        rank[well1] = 0
        rank[well2] = 0
    total_distance = 0
    for distance, well1, well2 in sorted(edges):
        if find(well1, parents) != find(well2, parents):
            union(well1, well2, parents, rank)
            total_distance += distance
    final_graphs = set()
    for well in parents:
        final_graphs.add(find(well, parents))
    if len(final_graphs) > 1:
        return -1
    return total_distance
