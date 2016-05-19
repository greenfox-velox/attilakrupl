# Create a `Stack` class that stores elements
# It should have a `size` method that returns number of elements it has
# It should have a `push` method that adds an element to the stack
# It should have a `pop` method that returns the last element form the stack and also deletes it from it
# please don`t use the built in methods


class Stack:
    stack1 = []

    def __init__(self, *args):
        for i in args:
            self.stack1.insert(len(self.stack1), i)
         
    def size(self):
        return len(self.stack1)
    
    def push(self, x):
        self.stack1.insert(len(self.stack1), x)
     
    def pop(self):
        last = self.stack1[len(self.stack1)-1]
        self.stack1 = self.stack1[:-1]
        return last
        
        
        
tomb = Stack("alma", "korte", "szilva")
print(tomb.stack1)
print(tomb.size())
tomb.push("barack")
print(tomb.size())
print(tomb.stack1)
print(tomb.pop())
print(tomb.size())
print(tomb.stack1)
        
