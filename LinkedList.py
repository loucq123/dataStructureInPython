class Node():
    def __init__(self, element=None, next=None):
        self.element = element
        self.next = next

    def __repr__(self):
        return repr(self.element)


class LinkedList():

    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front == None

    def insert(self, item):
        insertItem = Node(item, None)
        if self.is_empty():
            self.front = insertItem
            self.rear = insertItem
        else:
            self.rear.next = insertItem
            self.rear = insertItem

    def delete(self):
        if self.is_empty():
            print("The linked list is empty --- delete")
        else:
            first = self.front
            next = self.front.next.next
            while next != None:
                first = first.next
                next = next.next
            self.rear = first

    def count(self):
        times = 0
        first = self.front
        while first != None:
            first = first.next
            times += 1
        return times

    def first_node(self):
        if self.is_empty():
            print("The linked list is empty --- firstNode")
        else:
            print(self.__repr__())

    def last_node(self):
        if self.is_empty():
            print("The linked list is empty --- lastNode")
        else:
            print(self.__repr__())


def testNodeCreation():
    n = Node(element=10)
    assert n.element == 10


def testLinkedListCreation():
    testList = LinkedList()
    testList.insert(1)
    assert testList.front.element == 1 and testList.rear.element == 1
    testList.insert(2)
    assert testList.front.element == 1 and testList.rear.element == 2
    testList.delete()
    assert testList.front.element == 1 and testList.rear.element == 1


def test():
    testNodeCreation()
    testLinkedListCreation()


if __name__ == '__main__':
    test()



