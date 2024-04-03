/*
Solution for LeetCode problem 2444
Author: alex.does.leetcode@gmail.com
Last updated: 03 Apr 2024

See:
https://leetcode.com/problems/count-subarrays-with-fixed-bounds/
*/


class Solution {
    private int[] nums;
    private int minK, maxK;
    private boolean black(int n) {
        return nums[n] < minK || nums[n] > maxK;
    }
    private boolean red(int n) {
        return nums[n] == minK;
    }
    private boolean blue(int n) {
        return nums[n] == maxK;
    }
    public long countSubarrays(int[] nums, int minK, int maxK) {
        // Set up helper functions.
        this.nums = nums;
        this.minK = minK;  this.maxK = maxK;
        // Initialize count
        long count = 0;
        int start = 0;
        while (true) {
            // Move start to the next white sequence
            while (start < nums.length && black(start)) {
                start += 1;
            }
            if (start >= nums.length) {
                // If there are no more segments, terminate
                break;
            }
            int end = start;
            // Special case when minK == maxK
            if (minK == maxK) {
              while (end < nums.length && !black(end)) {
                end += 1;
              }
              long l = end - start;
              count += (l * (l+1)) / 2;
              start = end + 1;
              continue;
            }
            // Count how many fixed-bounds subarrays there are in this sequence
            int r = -1, b = -1;  // Initialize red and blue pointers
            while (true) {
                // Everytime we see a non-white block:
                if (end >= nums.length || black(end) || red(end) || blue(end)) {
                    // 1. add to count
                    if (r != -1 && b != -1) {
                        int large = Math.max(r, b);
                        int small = Math.min(r, b);
                        count += (small-start+1) * (end-large);
                    }
                    if (end >= nums.length) {
                      break;
                    }
                    // 2. Update red and blue pointers
                    if (red(end)) {
                        r = end;
                    } else if (blue(end)) {
                        b = end;
                    // 3 . This segment is complete, go on to next one
                    } else if (black(end)) {
                        break;
                    }
                }
                end += 1;
            }
            start = end + 1;
        }
        return count;
    }
}
