# Delete a node at a given position.
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
    def insert_at_position(self,data,position):
        count = 0
        new_node = Node(data)
        temp = self.head
        while temp and count <position -1:
            temp = temp.next
            count+=1
        new_node.next = temp.next
        temp.next = new_node
    def delete_at_position(self,position):
        count =0
        temp = self.head
        while temp and count<position-1:
            temp = temp.next
            count+=1
        temp.next= temp.next.next


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
ll.insert_at_front(11)
ll.print_list()
ll.insert_at_position(700,2)
ll.print_list()
ll.delete_at_position(3)
ll.print_list() 