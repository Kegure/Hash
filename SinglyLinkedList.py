
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_size(self):
        return self.size

    def get_head(self):
        return self.head

    def isEmpty(self):
        return self.head is None

    def search_SLinkedList(self, data):
        if self.isEmpty():
            print("Lista está Vazia")
            return
        headAux = self.head
        while headAux is not None:
            if headAux.get_data() == data:
                return headAux
            headAux = headAux.get_next()

    def insert_SLinkedList(self, data):
        if self.isEmpty():
            self.head = self.tail = Node(data)
        else:
            self.tail.set_next(Node(data))
            self.tail = self.tail.get_next()
        self.size = self.size + 1

    def delete_SLinkedList(self, data):
        nodeToDelete = self.search_SLinkedList(data)
        auxHead = self.head
        if self.isEmpty():
            return
        while auxHead.get_data() is not None:
            if auxHead.get_data() == nodeToDelete.get_data():
                previousDeleteNode = auxHead
                auxHead = auxHead.get_next()
                previousDeleteNode.set_next(auxHead.get_next())
                self.size = self.size - 1
                return
            auxHead = auxHead.get_next()
    def print_SLinkedList(self):
        auxHead = self.head
        while auxHead is not None:
            print(auxHead.get_data())
            auxHead = auxHead.get_next()
