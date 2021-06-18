import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator_hash = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: math.floor(x / y)
        }

        stack = []
        for token in tokens:
            try:
                num = int(token)
            except:
                num2 = stack.pop()
                num1 = stack.pop()
                num = operator_hash[token](num1, num2)
                print(f'token = {token}, num1 = {num1}, num2 = {num2}, num = {num}')
            stack.append(num)
        
        return stack.pop()