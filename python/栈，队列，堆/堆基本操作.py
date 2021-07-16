# 最大堆
class Heap:
    l = [float('inf')] # 先放一个很大的哨兵，顺便把l[0]位置占掉，让真正的堆从1下标开始

    def insert(self, item):
        self.l.append(item) # 这里不一定是item，但是就是先让数组size + 1，因为之后这个位置在下滤的过程中值可能被覆盖，不过没关系，值在item中保存着
        size = len(self.l) - 1

        i = size
        while self.l[i >> 1] < self.l[i]:
            self.l[i] = self.l[i >> 1]
            i >>= 1
        self.l[i] = item
    

    def delete(self):
        n = len(self.l)
        if n - 1 < 0:
            raise KeyError
        
        ret = self.l[1]
        temp = self.l[-1]
        size = n - 2 # 删除堆顶之后的大小
        
        parent = 1
        while parent * 2 <= size: # 还有孩子的时候
            child = parent * 2
            if child + 1 <= size and self.l[child + 1] > self.l[child]:
                child += 1
            
            if self.l[parent] > self.l[child]:
                break
            self.l[parent] = self.l[child]
            parent = child
        
        self.l[parent] = temp
        return ret        
        

        
        


h = Heap()
h.insert(58)
h.insert(25)
h.insert(44)
h.insert(14)
h.insert(16)
print(h.l)

print(h.delete())
print(h.delete())