class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        
        result = []
        while sum >= 9:
            result.append('9')
            sum -= 9
        if sum > 0:
            result.append(str(sum))
        result.extend(['0'] * (num - len(result)))

        return ''.join(result)        