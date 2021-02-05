class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# class IsEmpty(Exception):
#     pass


class NewList:
    def __init__(self):
        self.__node = Node(None)

    def init_list(self, target):
        p = self.__node
        for item in target:
            p.next = Node(item)
            p = p.next
            
    # def is_empty(self):
    #     return self.__node.next
            
    def append(self, element):
        p = self.__node
        while p.next:
            p = p.next
        p.next = Node(element)

    def remove(self, element):
        p = self.__node
        while p.next:
            if p.next.val == element:
                p.next = p.next.next
                break
            p = p.next
        else:
            raise ValueError("x not in list")

    def list_lenth(self):
        p = self.__node
        count = 0
        while p.next:
            p = p.next
            count += 1
        return count

    def delete(self, index):
        p = self.__node
        count = 0
        while index >= 0 and index < self.list_lenth():
            if count == index:
                p.next = p.next.next
                break
            p = p.next
            count += 1
        else:
            raise IndexError("list assignment index out of range")

    def update(self, target, element):
        p = self.__node
        while p.next:
            if p.next.val == target:
                p.next.val = element
            p = p.next
        else:
            raise ValueError("not equally element")

    def insert(self, index, element):
        p = self.__node
        node = Node(element)
        count = 0
        while index >= 0 and index <= self.list_lenth():
            if index == count:
                node.next = p.next
                p.next = node
                break
            p = p.next
            count += 1
        else:
            raise IndexError("list assignment index out of range")



    def show(self):
        p = self.__node
        while p.next:
            p = p.next
            print(p.val)

if __name__ == '__main__':
    # l = [1, 2, 3]
    l = []
    nl = NewList()
    nl.init_list(l)
    nl.append(4)
    # nl.show()
    # nl.remove(2)
    # nl.show()
    # print(nl.list_lenth())
    # nl.delete(0)
    # nl.update(5, 5)
    # nl.insert(4, 0)
    nl.show()

        