'''
Solution for leetcode problem from Contest 119
9 Dec 2023
https://leetcode.com/contest/biweekly-contest-119/problems/number-of-possible-sets-of-closing-branches

This uses a brute force solution backed by Floyd-Warshall.
'''

from copy import deepcopy
from itertools import chain, combinations
from math import inf
import time


soln1Steps = 0

# Generate a powerset, ie all combinations of items in s
def powerset(s):
  return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

# Run Floyd-Warshall on an adjacency matrix on given vertices
# Updates the adjacency matrix to have the shortest path between any two 
# vertices. Assumes that if vertices i,j cannot reach each other, then 
# matrix[j][j] = matrix[j][i] = math.inf.
def floydWarshall(matrix, vertices):
  global soln1Steps
  m2 = deepcopy(matrix)
  for k in vertices:
    for i in vertices:
      for j in vertices:
        m2[i][j] = min(m2[i][j], m2[i][k] + m2[k][j])
        soln1Steps += 1
  return m2

class Solution:
  # Helper function to check if this adjacency matrix is valid
  # A matrix is considered valid if all the vertices are no more than 
  # maxDistance from each other. Assume that matrix[i][j] already contains the
  # shortest path distance between i and j, or math.inf if they are 
  # unreachable from each other.
  def valid(self, matrix, vertices, maxDistance):
    global soln1Steps
    for i in vertices:
      for j in vertices:
        soln1Steps+= 1
        if matrix[i][j] > maxDistance:
          return False
    return True

  # Main function to produce the solution
  def numberOfSets(self, n, maxDistance, roads):
    # Transform roads into an adjacency matrix.
    matrix = [[inf] * n for _ in range(n)]
    for u, v, weight in roads:
      if weight < matrix[u][v]:
        matrix[u][v] = matrix[v][u] = weight
    for i in range(n):
      matrix[i][i] = 0
    # Now generate the power set and iterate over each combination.
    count = 0
    for s in powerset(range(n)):
      # Find the shortest paths between all vertices in this combination.
      m2 = floydWarshall(matrix, s)
      # Check if this combination is valid, aka every branch is at most
      # maxDistance from every other branch.
      if self.valid(m2, s, maxDistance):
        count += 1
    return count


if __name__ == "__main__":
  s = Solution()
  # # Assert test cases
   # Test case 1
  if 7 == s.numberOfSets(3, 5, [[0,1,100],[0,2,1],[1,2,1]]):
    print("Test 1 passed")
  else:
    print("Test 1 failed")

  # Test case 2
  if 5 == s.numberOfSets(3, 12, [[1,0,11],[1,0,16],[0,2,13]]):
    print("Test 2 passed")
  else:
    print("Test 2 failed")

  # Test case 3
  if 10 == s.numberOfSets(5, 10, [[4,0,38],[4,0,11],[2,0,24],[3,0,5],[2,1,18],[2,0,38],[1,0,7],[2,1,3],[2,1,2],[3,1,36]]):
    print("Test 3 passed")
  else:
    print("Test 3 failed")

  # Test case 4
  if 12 == s.numberOfSets(4, 5, [[1,0,3],[1,2,3],[0,3,1],[3,1,1]]):
    print(f"Test 4 passed in {soln1Steps} steps")
  else:
    print("Test 4 failed")

  # Test case 5
  if 10 == s.numberOfSets(5, 10, [[4,0,38],[4,0,11],[2,0,24],[3,0,5],[2,1,18],[2,0,38],[1,0,7],[2,1,3],[2,1,2],[3,1,36]]):
    print(f"Test 5 passed in {soln1Steps} steps")
  else:
    print("Test 5 failed")

  # Test case 6
  start = round(time.time() * 1000)
  if 16 == s.numberOfSets(10, 149, [[9,7,232],[7,1,109],[6,1,98],[2,0,342],[8,7,186],[3,2,563],[1,0,401],[1,0,404],[3,2,91],[1,0,391],[8,3,422],[2,0,436],[7,0,22],[1,0,518],[0,4,172],[0,5,188]]):
    print(f"Test 6 passed in {soln1Steps} steps")
    stop = round(time.time() * 1000)
    print(f"Took {stop-start}ms")
  else:
    print("Test 6 failed")

