class Stack:
    def __init__(self):
        self.stack = []
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        return self.stack.pop()
    def show(self):
        return self.stack
        
def reverse(string):
    stack_obj = Stack()
    for i in string:
        stack_obj.push(i)
    print(stack_obj.show())
    rev_str=''
    for i in string:
        rev_str+=stack_obj.pop()
    return rev_str

