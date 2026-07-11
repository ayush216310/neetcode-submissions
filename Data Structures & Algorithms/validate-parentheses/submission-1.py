class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {')' : '(', ']':'[','}':'{'}
        for c in s:
            if c not in pair:
                stack.append(c)
            else:
                if not stack or stack.pop() != pair[c]:
                    return False
        return len(stack) == 0