'''
Solution 2 for leetcode problem from Contest 119
9 Dec 2023
https://leetcode.com/contest/biweekly-contest-119/problems/number-of-possible-sets-of-closing-branches

This uses a dynamic programming solution.
'''

from copy import deepcopy
from math import inf
import time


soln2Steps = 0

class Solution:
  # Keeps track of vertices have been checked for validity
  # This way we can avoid checking the same set of vertices multiple times.
  verticesMemo = {}

  # Helper function to check if this adjacency matrix is valid
  # A matrix is considered valid if all the vertices are no more than 
  # maxDistance from each other. Assume that matrix[i][j] already contains the
  # shortest path distance between i and j, or math.inf if they are 
  # unreachable from each other.
  # This function is memoized so we don't have to check the same set of 
  # vertices multiple times.
  def valid(self, matrix, vertices, maxDistance):
    global soln2Steps
    # Sorting ensures same set of vertices in different order are the same key
    key = str(sorted(vertices))
    if key in self.verticesMemo:
      return self.verticesMemo[key]
    for i in vertices:
      for j in vertices:
        soln2Steps += 1
        if matrix[i][j] > maxDistance:
          self.verticesMemo[key] = False
          return False
    self.verticesMemo[key] = True
    return True

  def numberOfSets(self, n, maxDistance, roads):
    # Turn roads into adjacency matrix
    matrix = [[inf] * n for _ in range(n)]
    for u, v, weight in roads:
      if weight < matrix[u][v]:
        matrix[u][v] = matrix[v][u] = weight
    for i in range(n):
      matrix[i][i] = 0
    # Reset checkedMatrix
    self.verticesMemo = {}
    # Call recursive function
    return self.helper(n, maxDistance, set(), set(), matrix)

  # Main function used to calculate the solution
  # This function is recursive and takes additional arguments, so it is created
  # separatedly from numberOfSets().
  def helper(self, n, maxDistance, use, noUse, matrix):
    global soln2Steps

    if len(use) + len(noUse) == n:
      return 1
    # Unallocated vertices are those not assigned to either use or noUse.
    unallocated = [x for x in range(n) if (x not in use and x not in noUse)]
    # Find an unallocated vertex which keeps the matrix valid when added.
    for next in unallocated:
      m2 = deepcopy(matrix)
      for k in use:
        for dest in use:
          soln2Steps += 1
          m2[dest][next] = m2[next][dest] = min(m2[next][dest], m2[next][k] + m2[k][dest])
      v = self.valid(m2, use | {next}, maxDistance)
      if v:
        a = self.helper(n, maxDistance, use | {next}, noUse, m2)
        b = self.helper(n, maxDistance, use, noUse | {next}, matrix)
        res = a+b
        return res
    return 1


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
    print(f"Test 4 passed in {soln2Steps} steps")
  else:
    print("Test 4 failed")

  # Test case 5
  if 10 == s.numberOfSets(5, 10, [[4,0,38],[4,0,11],[2,0,24],[3,0,5],[2,1,18],[2,0,38],[1,0,7],[2,1,3],[2,1,2],[3,1,36]]):
    print(f"Test 5 passed in {soln2Steps} steps")
  else:
    print("Test 5 failed")

  # Test case 6
  start = round(time.time() * 1000)
  if 16 == s.numberOfSets(10, 149, [[9,7,232],[7,1,109],[6,1,98],[2,0,342],[8,7,186],[3,2,563],[1,0,401],[1,0,404],[3,2,91],[1,0,391],[8,3,422],[2,0,436],[7,0,22],[1,0,518],[0,4,172],[0,5,188]]):
    print(f"Test 6 passed in {soln2Steps} steps")
    stop = round(time.time() * 1000)
    print(f"Took {stop-start}ms")
  else:
    print("Test 6 failed")
  

