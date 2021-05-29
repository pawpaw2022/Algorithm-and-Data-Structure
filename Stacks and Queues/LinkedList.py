# Singly Linked List

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class linked_list:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        if self.head == None:
            new_node = Node(data, self.head)
            self.head = new_node
        
        else:
            new_node = Node(data)
            cur = self.head  # start traversing
            while cur.next:  # meaning cur.next != None 
                cur = cur.next
            cur.next = new_node
            
    def insert(self, index, data):
        if index < 0:
            print( "index is out of range")
        elif index == 0:
            new_node = Node(data)
            temp = self.head
            self.head = new_node
            new_node.next = temp
        elif index >= self.__len__():
            self.append(data)
            
        else:
            new_node = Node(data)
            cur = self.head
            i = 0 
            while i < index - 1:
                i += 1
                cur = cur.next
            temp = cur.next
            cur.next = new_node
            cur.next.next = temp
            
    def remove(self, index):
        if index < 0 or index > self.__len__():
            print( "index is out of range")
        elif index == 0:
            self.head = self.head.next
        elif index == self.__len__():
            cur = self.head
            while cur.next.next:
                cur = cur.next
            cur.next = None
        else:
            cur = self.head
            i = 0
            while i < index - 1:
                cur = cur.next
            cur.next = cur.next.next
    
    def pop(self):
        if self.head == None:
            return None
        
        elif len(self) == 1:
            element = self.head.data
            self.head = None
            return element
        else:
            cur = self.head
            while cur.next.next:
                cur = cur.next
            element = cur.next.data
            cur.next = None
            return element
        
                
        
            
    def __len__(self):
        if self.head == None:
            return 0
        
        else:    
            count = 1
            cur = self.head
            while cur.next:
                cur = cur.next
                count += 1
            return count
    
    def __repr__(self):
        if self.head == None:
            return "Linked List is empty"
        else:
            items = []
            cur = self.head
            items.append(cur.data)
            while cur.next :
                cur = cur.next
                items.append(cur.data)
            return str(items)