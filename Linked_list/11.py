# Detect a loop in a linked list using Floyd’s Cycle Detection Algorithm.
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
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end="==>")
            current = current.next
        print("None")
    def create_cycle(self):
        current = self.head
        i = 0
        while i<3:
            current = current.next
            i+=1
        cycle_link = current
        while current.next:
            current = current.next
        current.next=cycle_link
    def detect_cycle(self):
        slow_p = self.head
        fast_p = self.head
        while fast_p!=None and fast_p.next!=None:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                print("Cycle present in linked list")
                return True
        return False


ll = LinkedList()
ll.insert_at_end(11)
ll.insert_at_end(12)
ll.insert_at_end(13) 
ll.insert_at_end(14)
ll.insert_at_end(15)
ll.insert_at_end(16)
ll.insert_at_end(17)
ll.print_list()
ll.create_cycle()
detect =ll.detect_cycle()
print(detect)
#ll.print_list()
