class MyQueue:

    def __init__(self):
        self.container = []
        self.final = []
        self.length = 0

    def push(self, x: int) -> None:
        self.container.append(x)
        self.length += 1

    def pop(self) -> int:
        if self.final != []:
            self.length -= 1
            return self.final.pop()
        if self.length == 0 :
            return 0
        while len(self.container) != 0 :
            self.final.append(self.container.pop())
        self.length -= 1
        return self.final.pop()
        

    def peek(self) -> int:
        if self.final != []:
            return self.final[-1]
        else:
            return self.container[0]

    def empty(self) -> bool:
        if self.length == 0:
            return True
        return False
    
#[[],[1],[2],[3],[4],[],[5],[],[],[],[]]
q = MyQueue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
print(q.pop())
q.push(5)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())