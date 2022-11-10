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

def _get_linked_list_sum()

def get_linked_list_sum(linked_list_1, linked_list_2):
    sum_1 = 0
    sum_2 = 0
    a = linked_list_1.head
    b = linked_list_2.head

    while a is not None:
        sum_1 = sum_1 * 10 + a.data
        a = a.next
    while b is not None:
        sum_2 = sum_2 * 10 + b.data
        b = b.next
    return sum_1 + sum_2

def _get_linked_list_sum()



linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)
linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)
print(get_linked_list_sum(linked_list_1, linked_list_2))
