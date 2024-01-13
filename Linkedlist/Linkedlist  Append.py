class Node:
    def __init__(self, value):
        self.value= value
        self.next = None
class LinkedList:
    def __init__(self,value):
        New_Node = Node(value)
        self.head = New_Node
        self.tail = New_Node
        self.length = 1
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def make_empty(self):
        self.head =None
        self.tail =None
        self.length =0


    def append(self, value):
        New_node =  Node(value)
        if  self.length == 0:
            self.head = New_node
            self.tail = New_node
        else:
            self.tail.next = New_node
            self.tail = New_node
        self.length +=1
        return  True
my_linked_list = LinkedList(1)
my_linked_list.make_empty()

my_linked_list.append(1)
my_linked_list.append(2)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')

print('Linked List:')
my_linked_list.print_list()