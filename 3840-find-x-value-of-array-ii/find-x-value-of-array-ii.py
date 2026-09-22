class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)
        size = 1
        while size < n:
            size *= 2

        tree = [(1 % k, [0] * k) for _ in range(2 * size)]

        def make_node(value):
            rem = value % k
            cnt = [0] * k
            cnt[rem] = 1
            return rem, cnt

        def merge(left, right):
            lp, lc = left
            rp, rc = right
            product = (lp * rp) % k

            cnt = [0] * k
            for r in range(k):
                cnt[r] += lc[r]
            for a in range(k):
                if lc[a] == 0:
                    continue

                for b in range(k):
                    if rc[b] == 0:
                        continue

                    new_r = (a * rp) % k
                    break
            for b in range(k):
                if rc[b]:
                    new_r = (lp * b) % k
                    cnt[new_r] += rc[b]

            return product, cnt
        for i in range(n):
            tree[size + i] = make_node(nums[i])
        def combine(a, b):
            if a is None:
                return b
            if b is None:
                return a

            ap, ac = a
            bp, bc = b

            product = (ap * bp) % k
            cnt = ac[:]
            for r in range(k):
                if bc[r]:
                    nr = (ap * r) % k
                    cnt[nr] += bc[r]

            return product, cnt

        for i in range(size - 1, 0, -1):
            tree[i] = combine(tree[2 * i], tree[2 * i + 1])

        def update(pos, value):
            p = size + pos
            tree[p] = make_node(value)

            p //= 2
            while p:
                tree[p] = combine(tree[2 * p], tree[2 * p + 1])
                p //= 2

        def query(l, r):
            # Query [l, r)
            left_part = None
            right_part = None

            l += size
            r += size

            while l < r:
                if l & 1:
                    left_part = combine(left_part, tree[l])
                    l += 1

                if r & 1:
                    r -= 1
                    right_part = combine(tree[r], right_part)

                l //= 2
                r //= 2

            return combine(left_part, right_part)

        answer = []

        for index, value, start, x in queries:
            update(index, value)
            _, cnt = query(start, n)

            answer.append(cnt[x])

        return answer