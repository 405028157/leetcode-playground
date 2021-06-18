class Solution:
    def isValid(self, s: str) -> bool:
        left = ['(', '{', '[']
        right = [')', '}', ']']
        dic = {')': '(', '}': '{', ']': '['}
        stack = []

        for c in s:
            if c in left:
                stack.append(c)
            else:
                if not stack:
                    return False
                if dic[c] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(c)
    
        return not bool(stack)