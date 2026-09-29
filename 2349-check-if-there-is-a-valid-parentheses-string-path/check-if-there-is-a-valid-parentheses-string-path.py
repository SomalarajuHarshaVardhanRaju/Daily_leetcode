class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        if (m + n - 1) % 2 == 1:
            return False
        dp = [set() for _ in range(n)]

        for i in range(m):
            for j in range(n):
                new_balances = set()

                if i == 0 and j == 0:
                    new_balances.add(1 if grid[i][j] == '(' else -1)

                else:
                    if i > 0:
                        new_balances.update(dp[j])

                    if j > 0:
                        new_balances.update(dp[j - 1])

                    if grid[i][j] == '(':
                        new_balances = {b + 1 for b in new_balances}
                    else:
                        new_balances = {b - 1 for b in new_balances}
                dp[j] = {b for b in new_balances if b >= 0}

        return 0 in dp[n - 1]