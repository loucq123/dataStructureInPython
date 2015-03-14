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
            return self.front

    def last_node(self):
        if self.is_empty():
            print("The linked list is empty --- lastNode")
        else:
            return self.rear


def testNodeCreation():
    n = Node(element=10)
    assert n.element == 10


def testLinkedListInsertCreation():
    testList = LinkedList()
    testList.insert(1)
    assert testList.first_node().element == 1 and testList.last_node().element == 1
    testList.insert(2)
    assert testList.first_node().element == 1 and testList.last_node().element == 2


def testLinkedListCountCreation():
    testList = LinkedList()
    assert testList.count() == 0
    testList.insert(111)
    assert testList.count() == 1


def testLinkedListDeleteCreation():
    testList = LinkedList()
    testList.insert(1)
    testList.insert(2)
    testList.delete()
    assert testList.first_node().element == 1 and testList.last_node().element == 1


def testLinkedListFirst_nodeCreation():
    testList = LinkedList()
    testList.insert(1)
    assert testList.first_node() == testList.front


def testLinkedListLast_nodeCreation():
    testList = LinkedList()
    testList.insert(1)
    testList.insert(2)
    assert testList.last_node() == testList.rear


def testLinkedListCreation():
    testLinkedListInsertCreation()
    testLinkedListCountCreation()
    testLinkedListDeleteCreation()
    testLinkedListFirst_nodeCreation()
    testLinkedListLast_nodeCreation()


def test():
    testNodeCreation()
    testLinkedListCreation()


if __name__ == '__main__':
    test()




