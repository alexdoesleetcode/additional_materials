'''
Solution for LeetCode problem 76
Author: alex.does.leetcode@gmail.com
Last updated: 10 Feb 2024

See:
https://leetcode.com/problems/minimum-window-substring
'''

from collections import deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Count frequency of each character in t
        freqs = defaultdict(int)
        for c in t:
            freqs[c] += 1
        # Initialize some values
        best = (0, inf)          # Best result seen so far
        curr = defaultdict(int)  # Frequency of chars in current window
        prev = deque()           # prev[0] is the left side of current window
        # How many chars from t are still missing from current window
        unfinished = len(freqs)
        # Iterate over s. i is the right side of the window
        for i in range(len(s)):
            c = s[i]
            if c not in freqs:
                continue
            prev.append(i)
            curr[c] += 1
            if curr[c] == freqs[c]:
                unfinished -= 1
            # shorten if possible
            p = s[prev[0]]
            while curr[p] > freqs[p]:
                prev.popleft()
                curr[p] -= 1
                p = s[prev[0]]
            # check if done
            if not unfinished:
                if i+1-prev[0] < best[1]-best[0]:
                    best = (prev[0], i+1)
        if best[1] == inf:
            return ""
        else:
            return s[best[0]:best[1]]
