class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        arr = []
        for i,(l,r,w) in enumerate(intervals):
            arr.append((l,r,w,i))
        arr.sort()
        starts = [x[0] for x in arr]
        nxt = [0] * n
        for i in range(n):
            r = arr[i][1]
            nxt[i] = bisect_right(starts, r)
        memo = {}
        def solve(i, cnt):
            if i >= n or cnt == 4:
                return (0, ())
            if (i, cnt) in memo:
                return memo[(i, cnt)]
            skip_score, skip_indices = solve(i + 1, cnt)
            take_score, take_indices = solve(nxt[i], cnt + 1)

            take_score += arr[i][2]
            take_indices = tuple(sorted(take_indices + (arr[i][3],)))
            if take_score > skip_score:
                result = (take_score, take_indices)

            elif take_score < skip_score:
                result = (skip_score, skip_indices)

            else:
                result = min(
                    (take_score, take_indices),
                    (skip_score, skip_indices),
                    key=lambda x: x[1]
                )

            memo[(i, cnt)] = result
            return result

        return list(solve(0, 0)[1])
        