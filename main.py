
class Stack:
    def __init__(self, obj: str):
        self.obj = obj
        self.flag = True
        self.lis = ['', ')', '}', ']', '[', '{', '(']
        self.dictt2 = {
            '[': [], '{': [], '(': []
        }
        self.dictt1 = {
            ')': [], '}': [], ']': [],
        }

    def __str__(self):
        return self.obj

    def is_empty(self):
        if len(self.obj) == 0:
            return True
        else:
            return False

    def push(self, smith):
        self.obj += smith

    def pop(self):
        self.obj = self.obj[0: len(self.obj)-1]
        return self.obj[len(self.obj)-1]

    def peek(self):
        return self.obj[len(self.obj)-1]

    def revers(self):
        while self.obj:
            if self.peek() in self.dictt1:
                self.dictt1[self.peek()].append(self.peek())
                self.obj = self.obj[0: len(self.obj)-1]
            else:
                self.dictt2[self.peek()].append(self.peek())
                self.obj = self.obj[0: len(self.obj)-1]

    def size(self):
        return int(len(self.obj))

    def is_balanced(self):
        self.revers()
        for i in range(1, 4):
            if self.lis[i] in self.dictt1 and self.lis[-i] in self.dictt2:
                if len(self.dictt1[self.lis[i]]) != len(self.dictt2[self.lis[-i]]):
                    self.flag = False
        if self.flag:
            return 'Сбалансированно'
        else:
            return 'Несбалансированно'


stack = Stack('(((([{}]))))')
print(stack.is_balanced())
