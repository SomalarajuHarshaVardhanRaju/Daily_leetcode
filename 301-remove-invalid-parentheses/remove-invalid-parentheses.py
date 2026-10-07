class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(string):
            balance = 0
            for ch in string:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1
                    if balance < 0:
                        return False
            return balance == 0
        queue = {s}
        while queue:
            valid = []
            for string in queue:
                if is_valid(string):
                    valid.append(string)
            if valid:
                return valid
            next_level = set()
            for string in queue:
                for i in range(len(string)):
                    if string[i] in "()":
                        new_string = string[:i] + string[i + 1:]
                        next_level.add(new_string)
            queue = next_level
        return [""]