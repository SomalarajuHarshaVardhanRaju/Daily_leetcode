
class Solution:
    def palindromePath(self, n: int, edges: list[list[int]],
                       s: str, queries: list[str]) -> list[bool]:

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = n.bit_length()
        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        # Iterative DFS: compute parents, depths, and Euler intervals.
        stack = [(0, -1, 0)]
        while stack:
            u, p, state = stack.pop()

            if state == 0:
                tin[u] = timer
                timer += 1
                parent[u] = u if p == -1 else p

                stack.append((u, p, 1))
                for v in graph[u]:
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1

        # Binary lifting table for LCA.
        up = [parent[:]]
        for k in range(1, LOG):
            prev = up[k - 1]
            up.append([prev[prev[u]] for u in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            bit = 0
            while diff:
                if diff & 1:
                    u = up[bit][u]
                diff >>= 1
                bit += 1

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]

            return parent[u]

        # Fenwick tree supporting range XOR updates and point queries.
        bit = [0] * (n + 2)

        def add(i, value):
            i += 1
            while i <= n + 1:
                bit[i] ^= value
                i += i & -i

        def range_xor(left, right, value):
            add(left, value)
            add(right + 1, value)

        def point_query(i):
            i += 1
            result = 0
            while i > 0:
                result ^= bit[i]
                i -= i & -i
            return result

        def char_mask(c):
            return 1 << (ord(c) - ord('a'))

        chars = list(s)

        # Each character contributes to the root-path mask
        # of every node in its subtree.
        for u in range(n):
            range_xor(tin[u], tout[u], char_mask(chars[u]))

        answer = []

        for query in queries:
            parts = query.split()

            if parts[0] == "update":
                u = int(parts[1])
                new_char = parts[2]

                delta = char_mask(chars[u]) ^ char_mask(new_char)

                range_xor(tin[u], tout[u], delta)
                chars[u] = new_char

            else:
                u = int(parts[1])
                v = int(parts[2])

                ancestor = lca(u, v)

                mask_u = point_query(tin[u])
                mask_v = point_query(tin[v])

                path_mask = (
                    mask_u ^ mask_v ^ char_mask(chars[ancestor])
                )

                # A palindrome permutation allows at most one odd count.
                answer.append((path_mask & (path_mask - 1)) == 0)

        return answer
