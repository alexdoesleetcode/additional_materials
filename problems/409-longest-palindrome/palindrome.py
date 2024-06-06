from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Count how many times each character appears
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        # Count many pairs of characters are there
        count = 0
        for c in freq.values():
            if c % 2 == 0:
                count += c
            else:
                count += c-1
        # If there are letters leftover, use one for the middle
        if count < len(s):
            count += 1
        return count