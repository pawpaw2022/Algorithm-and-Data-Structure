# An array-like data structure whose elements follow the FIFO rule:
# #  First In, First Out.

# Queue implemented with a singly linked list.
# Note that we don't typically implement Queue with a list because dequeue requires too much time complexity. 

from LinkedList import linked_list, Node
class Queue:
    def __init__(self):
        self.queue = linked_list()
        
    # O(1)
    def enqueue(self, item): # add a item at the end
        self.queue.append(item)
    
    # O(1)
    def dequeue(self): # remove first item from the queue
        if self.queue.head == None:
            return
        else:
            return self.queue.pop()      
    
    # O(1)
    def peek(self):
        if self.queue.head == None:
            return None
        
        cur = self.queue.head
        while cur.next:
            cur = cur.next
        return cur.data
    
    # O(n)
    def search(self, element):
        if self.queue.head == None:
            return None
        elif self.queue.head.data == element:
            return 0  # it means the target element is the first element 
        else:
            cur = self.queue.head
            count = 0
            while cur.next:
                if cur.data == element:
                    return count
                cur = cur.next
                count +=1
    
    def __len__(self):
        return len(self.queue)
    
    def __repr__(self):
        return str(self.queue)


if __name__ == "__main__":
    my_queue = Queue()
    for i in range(10):
        my_queue.enqueue(i)
#     print(my_queue)
#     print(len(my_queue))
#     my_queue.dequeue()
#     print(my_queue)
#     print(my_queue.peek())
#     print(my_queue.search(3))
    print(f'pop: {my_queue.dequeue()}')
    print(f'{my_queue} after poping')
    my_queue.enqueue(666)
    print(f'{my_queue} after pushing')
    
