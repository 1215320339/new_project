class Stack:
    def __init__(self):
        self.__list_stack = []

    def push(self, element):
        self.__list_stack.append(element)

    def pop(self):
        return self.__list_stack.pop()

    def show(self):
        for item in self.__list_stack:
            print(item)


if __name__ == '__main__':
    s = Stack()
    # s.push(10)
    # s.push(20)
    # s.push(30)
    print(s.pop())
    print(s.pop())
    # s.show()
