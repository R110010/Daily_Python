# Reverse a linked list (iteratively).

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def insert_at_front(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def reverse_list_iter(self):
        prev = None
        next = None
        curr = self.head
        while curr!=None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

        
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" --")
            temp = temp.next
        print("None")

ll = LinkedList()
ll.insert_at_end(40)
ll.insert_at_end(44)
ll.insert_at_end(56)
ll.print_list()
#ll.insert_at_front(11)
ll.reverse_list_iter()
ll.print_list()
