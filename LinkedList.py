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

    def insert_after(self, item):
        insertItem = Node(item, None)
        if self.is_empty():
            self.front = insertItem
            self.rear = insertItem
        else:
            self.rear.next = insertItem
            self.rear = insertItem

    def insert_before(self, item):
        insertItem = Node(item, None)
        if self.is_empty():
            self.front = insertItem
            self.rear = insertItem
        else:
            insertItem.next = self.front
            self.front = insertItem
    
    def find(self, item):
        first = self.front
        while first != None:
            if first.element is item:
                return first
            first = first.next
        return None

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


def testLinkedListInsert_afterCreation():
    testList = LinkedList()
    testList.insert_after(1)
    assert testList.first_node().element == 1 and testList.last_node().element == 1
    testList.insert_after(2)
    assert testList.first_node().element == 1 and testList.last_node().element == 2


def testLinkedListInsert_beforeCreation():
    testList = LinkedList()
    testList.insert_before(1)
    assert testList.first_node().element == 1 and testList.last_node().element == 1
    testList.insert_before(2)
    assert testList.first_node().element == 2 and testList.last_node().element == 1


def testLinkedListFindCreation():
    testList = LinkedList()
    testList.insert_after(1)
    testList.insert_after(2)
    assert testList.find(2) == testList.rear and testList.find(3) == None


def testLinkedListCountCreation():
    testList = LinkedList()
    assert testList.count() == 0
    testList.insert_after(111)
    assert testList.count() == 1


def testLinkedListDeleteCreation():
    testList = LinkedList()
    testList.insert_after(1)
    testList.insert_after(2)
    testList.delete()
    assert testList.first_node().element == 1 and testList.last_node().element == 1


def testLinkedListFirst_nodeCreation():
    testList = LinkedList()
    testList.insert_after(1)
    assert testList.first_node() == testList.front


def testLinkedListLast_nodeCreation():
    testList = LinkedList()
    testList.insert_after(1)
    testList.insert_after(2)
    assert testList.last_node() == testList.rear


def testLinkedListCreation():
    testLinkedListInsert_afterCreation()
    testLinkedListInsert_beforeCreation()
    testLinkedListFindCreation()
    testLinkedListCountCreation()
    testLinkedListDeleteCreation()
    testLinkedListFirst_nodeCreation()
    testLinkedListLast_nodeCreation()


def test():
    testNodeCreation()
    testLinkedListCreation()


if __name__ == '__main__':
    test()




