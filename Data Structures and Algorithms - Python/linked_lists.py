'''
Intro to linked lists:
- Linked lists do not have indexes (0, 1, 2, ..., n)
- The list is in a contiguous place in memory (all items are next to each other)
- Nodes are made up of both values and pointers (they are essentially like nested dictionaries)
'''

# normal list structure
my_normal_list = [11, 3, 23, 7, 4]


# LL structure
head = {
    'value': 11,
    'next': {
        'value': 3,
        'next': {
            'value': 23,
            'next': {
                'value': 7,
                'next': {
                    'value': 4,
                    'next': None # tail node
                }
            }
        }
    }
}

print(head['next']['next']['value'])

# this class creates nodes, so that whenever any of the 4 methods in LinkedList needs to create a node, it will call Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# not efficient to write 4 methods as below
class LinkedList:
    def __init__(self, value): # the constructor: creates new node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self): # prints all items in the list
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value): #creates new node and adds to the end
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self): # removed tail value from list and returns it, two edge cases: (1) no items in LL, and (2) only 1 item in LL
        if self.length == 0: # handling edge case: LL = length 0
            return None 
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tailnext = None 
        self.length -= 1
        if self.length == 0: # after we have decremented the list from 1 to 0
            self.head = None
            self.tail = None
        return temp.value

    def prepend(self, value): # creates new node and adds to the beginning
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self): # pop first item of LL
        if self.length == 0:
            return None
        temp = self.head 
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.value 

    def get(self, index): # returns specific value in a LL according to index
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index): # "_" is used when the iterable is not included in the body of the loop (as opposed to "i")
            temp = temp.next
        return temp.value
    #def insert(self, index, value): #creates new node and inserts at index of choice


my_linked_list = LinkedList(2)

my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.prepend(1)

my_linked_list.print_list()

index = 2
print(f'element in LL at index {index} = {my_linked_list.get(index)}')

# the below will only work with a LL
print('head = ', my_linked_list.head.value)
print('tail = ', my_linked_list.tail.value)



