class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        def generate(combination: list[str], num: int):
            if num == 2 * n:
                if self.is_valid(combination):
                    res.append(''.join(combination))
                return
            
            combination.append('(')
            generate(combination, num + 1)
            combination.pop()

            combination.append(')')
            generate(combination, num + 1)
            combination.pop()
        
        generate([], 0)
        return res
    
    def is_valid(self, combination: list[str]):
        bal = 0
        for c in combination:
            if c == '(':
                bal += 1
            else:
                bal -= 1
            
            if bal < 0:
                return False
        
        return bal == 0
            