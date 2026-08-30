from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        # Make min_idx the smaller index
        if min_idx > max_idx:
            min_idx, max_idx = max_idx, min_idx

        # Option 1: Remove from the front
        front = max_idx + 1

        # Option 2: Remove from the back
        back = n - min_idx

        # Option 3: Remove smaller index from front
        # and larger index from back
        middle = (min_idx + 1) + (n - max_idx)

        return min(front, back, middle)