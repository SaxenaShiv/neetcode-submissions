class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if not stack:
                stack.append(ch)
            else:
                tos = stack[-1]
                if (tos == '{' and ch == '}') or \
                    (tos == '(' and ch == ')') or \
                    (tos == '[' and ch == ']'):
                    stack.pop()
                else :
                    stack.append(ch)
        return len(stack) == 0