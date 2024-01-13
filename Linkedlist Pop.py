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
    def append_list(self, value):
        New_node =  Node(value)
        if  self.length == 0:
            self.head = New_node
            self.tail = New_node
        else:
            self.tail.next = New_node
            self.tail = New_node
        self.length +=1
        return  True
    def pop(self):
        if self.length == 0:
            return  None
        temp= self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -=1
        if self.length == 0:
            self.head = None
            self.tail = None
        return  temp
    
 
my_linked_list = LinkedList(1)
my_linked_list.append_list(2)

# (2) Items - Returns 2 Node
print(my_linked_list.pop().value)
# (1) Item -  Returns 1 Node
print(my_linked_list.pop().value)
# (0) Items - Returns None
print(my_linked_list.pop())

