class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class IsEmpty(Exception):
    pass

class QueueLink:
    def __init__(self):
        self.__head = self.__tail = Node(None)

    def __is_empty(self):
        return self.__head is self.__tail

    def enqueue(self, element):
        self.__tail.next = Node(element)
        self.__tail = self.__tail.next

    def dequeue(self):
        if self.__is_empty():
            raise IsEmpty("queue is empty")
        self.__head = self.__head.next
        return self.__head.val

    def clear(self):
        self.__head = self.__tail

    # def show(self):
    #     p = self.__head
    #     while p.next:
    #         p = p.next
    #         print(p.val)

if __name__ == '__main__':
    ql = QueueLink()
    ql.enqueue(10)
    ql.enqueue(20)
    print(ql.dequeue())
    # ql.clear()
    print(ql.dequeue())
    # print(ql.dequeue())
