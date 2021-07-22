class Stack(object):
    MIN_CAPACITY = 20

    def __init__(self, capacity=MIN_CAPACITY):
        self.size = capacity
        self.length = 0
        self.stacks = [None] * self.size

    def push(self, val):
        if self.length >= self.size:
            return False

        self.stacks[self.length] = val
        self.length += 1
        return True

    def is_empty(self):
        return self.length == 0

    def pop(self) -> object:
        if self.is_empty():
            raise KeyError('Empty Stack')

        self.length -= 1
        return self.stacks[self.length]

    def top(self):
        if self.is_empty():
            raise KeyError('Empty Stack')

        return self.stacks[self.length - 1]

    @staticmethod
    def get_priority(operator):
        return {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2
        }.get(operator)

    @staticmethod
    def sub_compute(expression, start, operator_stacks=None, num_stacks=None):
        operator_stacks = operator_stacks or Stack(100)
        num_stacks = num_stacks or Stack(100)

        def handle_operator(priority=0):
            # 如果后续的优先级低于栈上最新的操作符优先级，那么执行这个操作，并且将结果压入数据栈中
            if not operator_stacks.is_empty() and Stack.get_priority(operator_stacks.top()) >= priority:
                operator = operator_stacks.pop()
                try:
                    right_num, left_num = num_stacks.pop(), num_stacks.pop()
                except KeyError:
                    raise AttributeError('UnRegular Formula')

                if operator == '/':
                    num = left_num / right_num
                elif operator == '*':
                    num = left_num * right_num
                elif operator == '+':
                    num = left_num + right_num
                elif operator == '-':
                    num = left_num - right_num

                num_stacks.push(num)
                handle_operator(priority)

        def collect_nums(sub_nums):
            # 将收集到数据拼接起来
            if sub_nums:
                num_stacks.push(float(''.join(sub_nums)))
                return []

            return sub_nums

        index = start
        nums = []
        while index < len(expression):
            unit = expression[index]
            if unit.isdigit() or unit == '.':
                nums.append(unit)
            elif unit == ' ':
                nums = collect_nums(nums)
            elif unit in ('*', '/'):
                nums = collect_nums(nums)
                operator_stacks.push(unit)
            elif unit in ('+', '-'):
                nums = collect_nums(nums)
                handle_operator(Stack.get_priority(unit))

                operator_stacks.push(unit)
            elif unit == '(':
                # 当存在一个 ( ) 的时候，自动开启一个子计算，将 括号内的数据单独计算后的结果插入栈汇总
                nums = collect_nums(nums)
                index = Stack.sub_compute(expression, index + 1, num_stacks=num_stacks)
            elif unit == ')':
                # 遇到 ) 的时候表示一个子计算已经完成了，此时返回新的位置
                nums = collect_nums(nums)
                handle_operator()
                return index + 1

            index += 1

        collect_nums(nums)
        # 当表达式遍历完成后，再次执行次操作、
        handle_operator()
        # 返回堆栈中的结果值
        return num_stacks.pop()

    @staticmethod
    def compute(expression):
        return Stack.sub_compute(expression, 0)


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
