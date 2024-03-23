class Solution:
    def isValid(self, s: str) -> bool:
        map_sym = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        stack: list[str] = []

        for c in s:
            if not c in map_sym:
                stack.append(c)
            else:
                if not stack or stack[-1] != map_sym[c]:
                    return False
                else:
                    stack.pop()

        return not stack
