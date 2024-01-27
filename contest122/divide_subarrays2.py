from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        # Restart the problem
        first = nums[0]
        nums = nums[1:]
        k -= 1
        # Solve the sliding window problem
        # Start with leftmost window
        window = nums[:dist+1]
        window.sort()
        best = curr = sum(window[:k])
        # Slide window to the right
        for i in range(dist+1, len(nums)):
            # Remove the left item from the old window
            old = nums[i-dist-1]
            old_idx = bisect_left(window, old)
            del window[old_idx]
            if old_idx < k:
                curr -= old
                if len(window) > k-1:
                    curr += window[k-1]
            # Add the right item from the new window
            new = nums[i]
            new_idx = bisect_right(window, new)
            window.insert(new_idx, new)
            if new_idx < k:
                curr += new
                if len(window) > k:
                    curr -= window[k]
            # Update best
            if curr < best:
                best = curr
        return best + first