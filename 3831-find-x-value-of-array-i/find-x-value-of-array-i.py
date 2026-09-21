class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k
            rem = num % k
            new_dp[rem] += 1

            for r in range(k):
                if dp[r] > 0:
                    new_rem = (r * rem) % k
                    new_dp[new_rem] += dp[r]
            for r in range(k):
                result[r] += new_dp[r]
            dp = new_dp
        return result        