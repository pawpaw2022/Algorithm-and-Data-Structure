# Doubly Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, value):
        node = Node(value) 
        if self.head is None:
            self.head = node
            self.tail = node
            return
        cur = self.head
        while cur.next:  # traverse to the last node
            cur = cur.next
        cur.next = node   # append the node to the next
        cur.next.prev = cur   # set the prev to the last one
        self.tail = cur.next  # set the tail
         
         
    def setHead (self, node):
        # setting the head of linked list, if node exists, move the node to the front
        if self.head is None:
            self.head = node
            self.tail = node
        self.insertBefore(self.head, node)
        
    
    def setTail (self, node):
        # setting the tail of the linked list, if node exists, move the node to the end 
        if self.head is None:
            self.head = node
            self.tail = node
        self.insertAfter(self.tail, node)
    
    def insertBefore (self, node, nodeToInsert):
        # inserting nodeToInsert before node, if node exists, move the node in front of the node 
        self.remove(nodeToInsert.value)
        nodeToInsert.next = node
        nodeToInsert.prev = node.prev
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert
        
    
    def insertAfter (self, node, nodeToInsert):
        # inserting nodeToInsert after node, if node exists, move the node behind the node  
        self.remove(nodeToInsert.value)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert
        
    
    def insertAtPosition(self, position, nodeToInsert):
        # insert the node at given position
        if position = 1:
            self.setHead(nodeToInsert)
            return
        cur_pos = 1
        cur_node = self.head
        while cur_node:
            if cur_pos == position:
                self.insertBefore(cur_node, nodeToInsert)
                return
            cur_node = cur_node.next
            cur_pos += 1
        if cur_pos == position:
            self.setTail(nodeToInsert)
            return
        
        
    
    def removeNodesWithValue(self, value):
        # remove all nodes with the given value
        cur = self.head
        while cur:
            to_remove = cur
            cur = cur.next
            if to_remove.value == value:
                self.remove(to_remove)

    
    def remove(self, value):
        # remove a single node
        if self.head.value == value:
            self.head = self.head.next
            self.head.prev = None
            
        elif self.tail.value == value:
            self.tail = self.tail.prev
            self.tail.next = None
            
        else:
            self.removeBindings(value)
    
    def removeBindings(self, value):
        cur = self.head
        while cur and cur.value != value:
            cur = cur.next
        
        if cur.prev:
            cur.prev.next = cur.next
        if cur.next:
            cur.next.prev = cur.prev
        cur.prev = None
        cur.next = None 
        
            
    
    def containsNodeWithValue(self,value):
        # True if the value exists, else False
        cur = self.head
        while cur:
            if cur.value == value:
                return True
            cur = cur.next
        return False
            
    def __repr__(self):
        if self.head == None:
            return "Linked List is empty"
        else:
            items = []
            cur = self.head
            items.append(cur.value)
            while cur.next :
                cur = cur.next
                items.append(cur.value)
            return str(items)


if __name__ == '__main__':
    my_list = doubly_linked_list()
    my_list.append(5)
    my_list.append(3)
    my_list.append(7)
    my_list.append(6)
    my_list.append(3)
    my_list.append(1)
    my_list.append(9)
     
    print(f'my doubly linked list is {my_list} \nhead is {my_list.head.value} & tail is {my_list.tail.value}')
    """My doubly linked list:

           Head                                Tail
            |                                   |
            v                                   v
    None <- 5 <-> 3 <-> 7 <-> 6 <-> 3 <-> 1 <-> 9 -> None 

    """
    # Try your linked list operation here:
    my_list.remove(6)
    print(f'my_list after removing 6: {my_list}')
    
    
