class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur.next is not None:
            print(cur.data)
            cur = cur.next

linked_list = LinkedList(3)
linked_list.append(4)
linked_list.append(5)
linked_list.print_all()