class MinStack:

    def __init__(self):
        self.nums = []
        self.mins = [float('inf')]  # 辅助栈，同步存放某个元素入栈后或出栈前的最小元素

    def push(self, val: int) -> None:
        current_min = self.getMin()

        if val < current_min:
            self.mins.append(val)
        else:
            self.mins.append(current_min)

        self.nums.append(val)

    def pop(self) -> None:
        self.mins.pop()
        return self.nums.pop()

    def top(self) -> int:
        return self.nums[-1]

    def getMin(self) -> int:
        return self.mins[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()