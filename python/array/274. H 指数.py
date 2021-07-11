class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        if n == 0:
            return 0
        if n == 1:
            return min(citations[0], 1)
        
        low = 0
        high = n + 1

        def check(x):
            count = 0
            for i in citations:
                if i >= x:
                    count += 1
            
            return count - x

        # [low, high)
        while low < high:
            mid = int((low + high) / 2)
            dirc = check(mid)
            # print(f'mid = {mid}, dirc = {dirc}')
            if dirc == 0:
                return mid
            elif dirc < 0:
                high = mid
            else:
                last = mid
                low = mid + 1

        return last
