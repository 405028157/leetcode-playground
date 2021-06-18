class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operator_hash = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y)
        }

        stack = []
        for token in tokens:
            if token not in '+-*/':
                num = int(token)
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                num = operator_hash[token](num1, num2)
                # print(f'token = {token}, num1 = {num1}, num2 = {num2}, num = {num}')
            stack.append(num)
        
        return stack.pop()