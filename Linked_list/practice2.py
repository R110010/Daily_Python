# finding the middle element of a linked list.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_end(self,data) ->None:
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def print_list(self) ->None:
        current= self.head
        while current:
            print(current.data, end="-->")
            current= current.next
        print("None")
    def middle_element(self):
        slow_p = self.head
        fast_p = self.head
        while fast_p != None and fast_p.next != None:
            slow_p= slow_p.next
            fast_p= fast_p.next.next
        return slow_p.data
    def detect_cycle(self):
        slow_p = self.head
        fast_p = self.head
        while fast_p!=None and fast_p.next!=None:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p==fast_p:
                print("Cycle dectected in linked list")
                return True
        return False

ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_end(40)
#ll.insert_at_end(50)
ll.print_list()
middle = ll.middle_element()
print("middle element is ",middle)
