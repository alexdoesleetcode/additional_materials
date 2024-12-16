import heapq
from functools import cmp_to_key

class MyHeap:
    def __init__(self, lst, cmp=lambda a, b: a-b, reverse=False):
        if not reverse:
            self.cmp = cmp
        else:
            self.cmp = lambda a,b: cmp(b, a)
        self.s = list(map(cmp_to_key(self.cmp), lst))
        heapq.heapify(self.s)

    def pop(self):
        return heapq.heappop(self.s).obj

    def push(self, item):
        heapq.heappush(self.s, cmp_to_key(self.cmp)(item))

    def __str__(self):
        return str(list(map(lambda x: x.obj, heapq.nsmallest(len(self.s), self.s))))


def heapify(lst, cmp=lambda a, b: b-a):
    class Myheap(list):
        def __init__(self, other):
            super().__init__(other)
    # s = Myheap(map(cmp_to_key(cmp), lst))
    # s.cmp = cmp
    s = list(map(cmp_to_key(cmp), lst))
    s = Myheap(s)
    s.cmp = cmp
    heapq.heapify(s)
    return s

def heappop(lst):
    return heapq.heappop(lst).obj

def heappush(lst, x):
    heapq.heappush(lst, lst.cmp(x))

a = [1,3,4,6,2,7]
a = MyHeap(a, reverse=False)
print(a.pop())
print(a.pop())
print(a)
a.push(8)
print(a)
print(a.pop())
print(a.pop())

