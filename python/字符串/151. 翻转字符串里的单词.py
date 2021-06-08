class Solution:
    def reverseWords(self, s: str) -> str:
        # import re
        # s = s.strip()
        # s = re.sub(r'[ ]+', ' ', s)
        
        array_s = s.split()
        # print(array_s)
        return ' '.join(array_s[::-1])