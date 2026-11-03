class Solution:
    def minMoves(self, nums: list[int]) -> int:
        target = max(nums)
        moves = 0

        for num in nums:
            moves += target - num

        return moves