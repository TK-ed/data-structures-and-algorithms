class stack:
    def __init__(self):
        print("initializing")
        self.stack = []
        self.top = -1
    
    def push(self, item):
        self.top += 1
        self.stack.append(item)
        
    def pop(self):
        self.top -= 1
        self.stack.pop()
        
    def display(self):
        print(self.stack)
        
if __name__ == "__main__":
    s = stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.display()
    s.pop()
    s.pop()
    s.pop()
    s.display()