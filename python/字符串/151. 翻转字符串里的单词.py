"""
本题也可以先把s整体翻转（双指针原地就可），再把每个单词原地翻转，就得到结果
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        # import re
        # s = s.strip()
        # s = re.sub(r'[ ]+', ' ', s)
        
        array_s = s.split()
        # print(array_s)
        return ' '.join(array_s[::-1])