class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class IsEmpty(Exception):
    pass


class StackLink:
    def __init__(self):
        self.__top = None

    def push(self, element):
        node = Node(element)
        node.next = self.__top
        self.__top = node

    def pop(self):
        if not self.__top:
            raise IsEmpty("stacklink is empty")
        result = self.__top.val
        self.__top = self.__top.next
        return result

    def show(self):
        p = self.__top
        while p:
            print(p.val)
            p = p.next


if __name__ == '__main__':
    sl = StackLink()
    sl.push(10)
    sl.push(20)
    sl.push(30)
    print(sl.pop())
    print(sl.pop())
    print(sl.pop())
    # sl.show()
