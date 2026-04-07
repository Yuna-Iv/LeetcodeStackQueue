from collections import deque

class FreqStack:
    def __init__(self):
        self.freq = {}
        self.group = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        if val not in self.freq:
            self.freq[val] = 0

        self.freq[val] += 1
        frequency = self.freq[val]

        if frequency not in self.group:
            self.group[frequency] = deque()

        self.group[frequency].append(val)

        if frequency > self.max_freq:
            self.max_freq = frequency

    def pop(self) -> int:
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1

        if not self.group[self.max_freq]:
            self.max_freq -= 1

        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
