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
    def prepend(self, values):
        new_node = Node(values)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.length +=1
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length ==  0:
            self.tail = None
        return  temp
    def get(self, index):
        if index <0 or index >= self.length:
            return  None
        temp = self.head
        for _ in range(index):
            temp =  temp.next
        return  temp.value

my_linked_list = LinkedList(2)
my_linked_list.append_list(1)
my_linked_list.append_list(3)

print(my_linked_list.get(0))
