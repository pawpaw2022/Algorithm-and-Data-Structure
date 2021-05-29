# An array-like data structure whose elements follow the LIFO rule:
# #  Last In, First Out.
# A stack is typically implemented with a dynamic array or with a singly linked list.

# Stack implemented with a dynamic array. 
class Stack:
    
    def __init__(self):
        self.stack = []
    
    # O(1)
    def pop(self):
        if len(self.stack) <= 0:
            return None
        
        return self.stack.pop()
   
   # O(1)
    def push(self, item):
        self.stack.append(item)
    
    # O(1)
    def peek(self):
        if len(self.stack) <= 0:
            return None
        
        return self.stack[len(self.stack) - 1]
    
    # O(n)
    def search(self, element):
        for i in range(len(self.stack)):
            if self.stack[i] == element:
                return i
        return None
        
    def size(self):
        return len(self.stack)
    
    def __repr__(self):
        return str(self.stack)
    
# Stack implemented with a singly linked list.
from LinkedList import linked_list, Node
    
class Stack2:
    
    def __init__(self):
        self.stack2 = linked_list()
    
    # O(1)
    def pop(self):
        if self.stack2.head == None:
            return None
        
        return self.stack2.pop()
   
    # O(1)
    def push(self, item):
        self.stack2.append (item)
    
    # O(1)
    def peek(self):
        if self.stack2.head == None:
            return None
        
        cur = self.stack2.head
        while cur.next:
            cur = cur.next
        return cur.data
    
    # O(n)
    def search(self, element):
        if self.stack2.head == None:
            return None
        elif self.stack2.head.data == element:
            return 0  # it means the target element is the first element 
        else:
            cur = self.stack2.head
            count = 0
            while cur.next:
                if cur.data == element:
                    return count
                cur = cur.next
                count +=1
        
    def __len__(self):
        return len(self.stack2)
    
    def __repr__(self):
        return str(self.stack2)

    
if __name__ == "__main__":
    my_stack = Stack2()
    for i in range(10):
        my_stack.push(i)
    print(my_stack)
    print(my_stack.peek())
    print(my_stack.pop())
    print(my_stack)
    print(my_stack.search(7))
