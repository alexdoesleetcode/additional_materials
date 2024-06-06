'''
Common graph algorithms

Contents:
- edgelist_to_adjmatrix  # Converts an edgelist to an adjacency matrix
- reachable  # Compute set of reachable nodes from src
- dijkstra  # Implementation of Dijkstra's shortest path algorithm
'''

from typing import List
import difflib
import heapq


# Converts an edgelist to an adjacency matrix
# When weighted=True, assume that the input edges contains a list of 
#  length-three-lists (ie [src, dest, weight]).
# When weighted=False, assume that the input edges contains a list of
#  length-two-lists (ie [src, dest]).
# Two nodes might have more than one edge connecting them, and if so we take
# the shortest (there is a flag to flip this around).
def edgelist_to_adjmatrix(edges: List[List[int]], weighted=False, directed=False, default_weight=None):
    matrix = {}
    if weighted:
        for u, v, w in edges:
            if not u in matrix:
                matrix[u] = {}
            if v in matrix[u]:   # This edge already exists
                matrix[u][v] = min(matrix[u][v], w)
            else:
                matrix[u][v] = w
            if not directed:
                if not v in matrix:
                    matrix[v] = {}
                matrix[v][u] = matrix[u][v]
    else:  # not weighted
        for u, v in edges:
            if not u in matrix:
                matrix[u] = set()
            matrix[u].add(v)
            if not directed:
                if not v in matrix:
                    matrix[v] = set()
                matrix[v].add(u)
    return matrix

# Compute set of reachable nodes from src
# This works whether the adjacency matrix is weighted
# (dict[int, dict[int, int]]) or unweighted (dict[int, set[int]])
def reachable(edges, src):
    reached = set([src])
    todo = [src]
    while len(todo) > 0:
        node = todo.pop()
        if node in edges:
            for neigh in edges[node]:
                if neigh in reached:
                    continue
                else:
                    reached.add(neigh)
                    todo.append(neigh)
    return reached

# Implementation of Dijkstra's shortest path algorithm
# Takes an adjacency matrix and a vertex, returns a dict[int,int] of costs
# Assume that edges is weighted. Does not assume if it is directed or not.
def dijkstra(edges, src, dest=None):
    costs = {}
    todo = [(0, src)]
    heapq.heapify(todo)
    while len(todo) > 0:
        cost, u = heapq.heappop(todo)
        if u in costs:
            continue
        costs[u] = cost
        if u == dest:
            break
        if u in edges:
            for v in edges[u]:
                if v in costs:
                    continue
                heapq.heappush(todo, (cost+edges[u][v], v))
    return costs



edges = [[13,29,77],[19,13,94],[10,13,27],[7,10,7],[2,29,89],[18,19,55],[5,29,90],[20,5,14],[6,19,58],[1,13,11],[22,6,71],[32,29,41],[11,7,65],[12,13,76],[0,7,7],[26,12,36],[30,32,53],[14,30,68],[17,29,53],[16,0,36],[33,17,93],[9,19,26],[27,29,45],[23,9,67],[34,27,56],[3,12,80],[21,14,74],[31,14,66],[28,5,33],[24,23,83],[15,16,79],[25,5,8],[4,7,42],[8,20,56],[1,26,28],[8,13,11],[22,34,52],[19,22,64],[13,21,90],[16,26,93],[8,3,23],[6,0,6],[9,33,97],[7,22,18],[9,4,80],[9,14,92],[27,22,66],[7,26,65],[16,24,99],[16,6,24],[2,20,92],[33,16,70],[2,33,18],[32,1,66],[33,22,95],[18,26,99],[4,30,20],[28,6,73],[4,12,50],[23,18,63],[1,30,13],[15,32,2],[6,29,52],[4,24,67],[15,17,52],[20,30,56],[1,2,72],[30,29,19],[6,8,30],[6,5,85],[17,5,21],[32,16,23],[9,3,71],[28,16,92],[26,21,100],[8,2,36],[21,28,58],[12,32,27],[34,21,31],[19,34,82],[22,15,78],[17,16,90],[13,6,38],[33,19,54],[14,4,41],[18,24,83],[21,8,94],[16,9,59],[26,3,29],[3,1,65],[27,31,93],[33,0,17],[18,17,77],[2,21,39],[11,4,13],[24,5,7],[30,23,67],[2,16,59],[6,17,77],[10,3,95],[9,13,39],[17,1,62],[31,4,38],[12,15,83],[7,16,22],[11,9,100],[15,21,89],[23,33,70],[8,31,73],[19,4,27],[4,2,26],[31,0,34],[8,26,60],[9,24,36],[28,32,62],[19,15,52],[2,0,8],[21,9,70],[33,27,21],[7,19,94],[29,12,36],[28,23,36],[28,31,7],[16,27,53],[30,31,11],[18,21,42],[11,33,87],[12,20,56],[19,30,95],[34,32,16],[26,19,66],[21,7,72],[22,17,54],[27,10,42],[7,28,71],[23,15,24],[4,16,32],[11,8,11],[22,24,95],[10,16,90],[9,7,33],[14,8,11],[32,27,5],[25,20,67],[20,15,49],[15,10,31],[29,22,22],[24,31,94],[12,1,26],[24,19,92],[16,31,81],[22,16,81],[3,31,36],[20,9,72],[12,34,93],[6,3,7],[2,3,89],[14,20,61],[13,14,95],[1,27,96],[10,8,58],[11,30,81],[31,32,72],[31,26,89],[24,7,25],[23,4,87],[24,2,75],[2,30,3],[4,32,6],[28,15,32],[34,33,90],[29,20,4],[21,27,91],[21,25,92],[0,18,50],[14,3,5],[27,7,68],[15,4,5],[20,7,25],[23,11,29],[26,0,19],[0,28,82],[17,4,61],[3,17,64],[21,4,79],[22,5,38],[11,16,35],[3,0,37],[5,32,93],[22,4,64],[10,5,38],[11,29,12],[7,18,91],[0,9,85],[24,3,60],[3,20,55],[11,6,9],[5,15,94],[16,14,74],[11,22,52],[34,7,12],[20,1,89],[29,34,69],[2,9,100],[32,7,98],[3,34,89],[23,10,22],[32,24,12],[21,12,48],[25,9,41],[28,19,54],[22,20,28],[12,17,61],[6,18,50],[26,32,39],[8,29,31],[17,10,84],[7,29,40],[10,4,7],[31,22,89],[7,30,33],[28,8,12],[13,26,81],[11,27,43],[27,18,37],[9,31,64],[0,22,84],[34,9,34],[33,7,6],[5,30,64],[11,32,15],[18,25,88],[15,24,100],[6,32,75],[25,17,53],[23,21,63],[9,27,76]]
costs = dijkstra(edgelist_to_adjmatrix(edges, weighted=True), 0, 34)
costs = dict(sorted(costs.items()))
print(costs)
expected = {0: 0, 2: 8, 3: 13, 6: 6, 7: 7, 10: 14, 11: 15, 14: 18, 26: 19, 30: 11, 33: 13, 34: 19}
for node, cost in expected.items():
    if cost != costs[node]:
        print(f"diff at {node}: want {cost}, got {costs[node]}")