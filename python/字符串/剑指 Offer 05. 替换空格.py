"""
用字符串+=，最大的问题是每次都要新开空间
"""
class Solution:
    def replaceSpace(self, s: str) -> str:
        res = ''
        for c in s:
            if c != ' ':
                res += c
            else:
                res += '%20'
        return res