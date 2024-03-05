class queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def push(self, x: int) -> None:
        self.stack1.append(x)
        
    def pop(self):
        while self.stack1:
            x = self.stack1.pop()
            self.stack2.append(x)
            print(self.stack2)
        y = self.stack2.pop()
        print("popped_element:", y)
        
    def peek(self):
        while self.stack2:
            top_element = self.stack2.pop()
        print("The top element:", top_element)
    
                
    def display(self):
        print(self.stack1, self.stack2)
        
    def empty(self):
        if not self.stack1 and not self.stack2:
            print("The Queue is empty!!")
            return
        print("The Queue is not empty")
        
if __name__ == "__main__":
    q = queue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    q.display()
    q.pop()
    q.pop()
    q.peek()
    q.empty()
    q.display()