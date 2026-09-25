class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:

        def union(A, B):
            return A | B

        def concat(A, B):
            return {a + b for a in A for b in B}

        def parse(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                ch = expression[i]

                if ch == ',':
                    result |= current
                    current = {""}
                    i += 1

                elif ch == '{':
                    inside, i = parse(i + 1)
                    current = concat(current, inside)

                else:
                    current = {word + ch for word in current}
                    i += 1
            result |= current
            if i < len(expression) and expression[i] == '}':
                i += 1

            return result, i

        result, _ = parse(0)

        return sorted(result)