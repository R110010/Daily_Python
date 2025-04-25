# Find the length of a linked list (iteratively and recursively).

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
    def len_list_iter(self):
        count = 0
        temp = self.head
        while temp:
            temp = temp.next 
            count+=1
        print(" length of list by iteration is :", count)
    def len_list_recr(self,node,count=0):
        if node is None:
            print(" length of list by recursion is ",count)
            return
        return self.len_list_recr(node.next,count+1)
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
ll.insert_at_last(45)
#ll.insert_at_last(93)
#ll.insert_at_last(187)
ll.print_list()
ll.len_list_iter()
ll.len_list_recr(ll.head)
