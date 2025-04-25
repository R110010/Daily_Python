# Create a singly linked list and implement append() and print_list() methods.

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_last(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" - ")
            temp = temp.next
        print("None")

ll= LinkedList()
ll.insert_at_last(10)
ll.insert_at_last(20)
ll.insert_at_last(30)
ll.print_list()