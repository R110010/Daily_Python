# Find the node in the linked list from where cycle begins.
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head==None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def print_list(self):
        current = self.head
        while current:
            print(current.data,end=" ==>")
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
    def remove_cycle(self):
        slow_p = self.head
        fast_p = self.head
        while fast_p and fast_p.next:            
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p==fast_p:
                slow_p = self.head                
                if slow_p!=fast_p:
                    while slow_p.next!=fast_p.next:
                        slow_p=slow_p.next
                        fast_p=fast_p.next
                    fast_p.next = None
                else:
                    while fast_p.next!=slow_p:
                        fast_p=fast_p.next
                    fast_p.next = None
ll = LinkedList()
ll.insert_at_end(12)
ll.insert_at_end(13)
ll.insert_at_end(14)
ll.print_list()

