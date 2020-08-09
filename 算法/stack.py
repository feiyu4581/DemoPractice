class Stack(object):
    MIN_CAPICITY = 20

    def __init__(self, capicity=MIN_CAPICITY):
        pass

    def push(self, val):
        pass

    def pop(self):
        pass

    @staticmethod
    def compute(expression):
        pass


if __name__ == "__main__":
    stack = Stack()
    for i in range(10):
        stack.push(i)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

    print(Stack.compute('22 * 19 + 20'))
    print(Stack.compute('22 * 19 + 20 / 2 + 3'))
    print(Stack.compute('12 + 22 * 19 + 20 / 2 + 3'))
    print(Stack.compute('(12 + 22) * 19 + 20 / 2 + 3'))
    print(Stack.compute('((12 + 22) * 19 + 20) / 2 + 3'))
    print(Stack.compute('((12 + 22) * 19 + 20) / (2 + 3)'))
