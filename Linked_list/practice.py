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
            self.head=new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def insert_at_front(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
    def insert_at_position(self,data,position):
        if position <0:
            print("Enter a valid position")
            return
        new_node = Node(data)
        current = self.head
        if position ==0:
            self.insert_at_front(data)
            return
        count =0
        while current and count < position-1:
            current = current.next
            count+=1
        if not current:
            return "positon out of bound"
        new_node.next = current.next
        current.next = new_node
    def delete_by_value(self,value):
        current =self.head
        if current.data == value:
            current=current.next
        while current.next and current.next.data != value:
            current = current.next
        current.next = current.next.next
    def reverse_list_iteratively(self)-> None:
        current = self.head
        prev = None
        while current !=None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    def reverse_list_recursive(self):
        def _reverse_list_recursive(current,prev):
            if current == None:
                return prev
            next = current.next
            current.next = prev
            return _reverse_list_recursive(next,current)
        self.head = _reverse_list_recursive(self.head,None)



    def print_list(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(17)
ll.insert_at_front(7)
ll.insert_at_position(8,1)
ll.insert_at_front(24)
ll.print_list()
ll.delete_by_value(10)
ll.print_list()
ll.reverse_list_iteratively()
ll.print_list()