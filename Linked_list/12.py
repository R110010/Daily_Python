# merge two sorted linked list.
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self,data):
        new_Node =Node(data)
        if not self.head:
            self.head = new_Node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_Node
    def print_list(self):
        current = self.head
        while current:
            print(current.data , end="-->")
            current = current.next
        print("None")
        
     
def merge_lists(list1,list2):
    dummy = Node(0)
    current = dummy
    head1 = list1.head
    head2 = list2.head
    while head1 and head2:
        if head1.data < head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next
    if head1:
        current.next = head1
    else:
        current.next = head2
    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list
list1 = LinkedList()
list1.insert_at_end(1)
list1.insert_at_end(3)
list1.insert_at_end(3)
list1.insert_at_end(5)

list2 = LinkedList()
list2.insert_at_end(2)
list2.insert_at_end(4)
list2.insert_at_end(6)

merged = merge_lists(list1, list2)
merged.print_list()