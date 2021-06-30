# Class Stack is used only for Stack management i.e. for undo and redo operations
class Stack:

    def __init__(self, text):
        self.stack = []
        self.stack.append(text)

    def add(self, dataval):
        # Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    # Use list pop method to remove element
    def remove(self):
        if len(self.stack) <= 1:
            return "No element in the Stack"
        else:
            return self.stack.pop()

    #  It gives the top element of stack
    def peek(self):
        if len(self.stack) == 1:
            return self.stack[0]
        else:
            return self.stack[-1]

    #  It prints all  element of stack
    def print_all(self):
        length = len(self.stack) - 1
        while self.stack:
            print(self.stack[length])
            length -= 1

    #  It return the size of the  stack
    def size(self):
        return len(self.stack)

    #  It clears the  stack
    def clear_stack(self):
        return self.stack.clear()

    #  It returns the particular element of the stack
    def ele(self, index):
        return self.stack[index]
