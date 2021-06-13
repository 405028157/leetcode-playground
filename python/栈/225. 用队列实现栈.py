from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = deque()
        self.queue2 = deque()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.append(x)
        # print(f'stack1 after push: {self.queue1}')


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        last = None
        while self.queue1:
            last = self.queue1.popleft()
            # 如果last不是最后一个元素，不需要删，放回queue2队列
            if self.queue1:
                self.queue2.append(last)
        
        self.queue1, self.queue2 = self.queue2, self.queue1

        # print(f'stack1 after pop: {self.queue1}')
        return last

    def top(self) -> int:
        """
        Get the top element.
        """
        last = None
        while self.queue1:
            last = self.queue1.popleft()
            self.queue2.append(last)
        self.queue1, self.queue2 = self.queue2, self.queue1
        
        # print(f'stack1 after top: {self.queue1}')
        return last


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not bool(self.queue1)



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()