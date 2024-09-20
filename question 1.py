# Q1. Reverse a Stack You are given a stack of integers. Your task is to 
# reverse the order of the elements in the stack using only stack 
# operations (push and pop) and without using any additional data 
# structures. Ex. stack = [1, 2, 3, 4, 5] reverse Stack(stack) print(stack) 
# Output should be [5, 4, 3, 2, 1]. 




class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def reverse(self):
        if self.is_empty():
            return

        temp = self.pop()
        self.reverse()
        self.insert_at_bottom(temp)

    def insert_at_bottom(self, x):
        if self.is_empty():
            self.push(x)
            return

        temp = self.pop()
        self.insert_at_bottom(x)
        self.push(temp)

    def print_stack(self):
        print(self.stack)


# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print("Original Stack:")
stack.print_stack()

stack.reverse()

print("Reversed Stack:")
stack.print_stack()



