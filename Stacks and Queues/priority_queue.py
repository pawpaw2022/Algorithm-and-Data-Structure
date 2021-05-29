"""
Priority queue is a special type of queue in which each element is associated with a priority

For example: the element with the HIGHEST value is considered as the highest priority.

Difference:
            Normal Queue: First in First out
            Priority Queue: the values are removed and inserted on the basis of priority
            
"""

# To implement Priority Queue with highest priority, it is the same with Max Heap

class priority_queue:
    def __init__(self):
        self.array = []

    def heapify(self, heap_size, i):
        largest = i
        left = 2*i + 1
        right = 2*i + 2
        
        if left < heap_size and self.array[left] > self.array[largest]: # swap left to parent
            largest = left
        
        if right < heap_size and self.array[right] > self.array[largest]: # swap right to parent
            largest = right
        
        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.heapify(heap_size, largest)

    def enqueue(self, num):
        # check if array is empty
        if len(self.array) == 0:
            self.array.append(num)
        
        else:
            self.array.append(num)
            for i in reversed(range(len(self.array)//2 + 1)):
                self.heapify(len(self.array), i)


    def dequeue(self, num):
        # check if num is in array
        if num not in self.array:
            return
        else:
            num_idx = self.array.index(num)
            
            self.array[num_idx], self.array[-1] = self.array[-1], self.array[num_idx] # switch the target num to the last one
            self.array.pop() # remove the last one
            
            for i in reversed(range(len(self.array)//2 + 1)):
                self.heapify(len(self.array), i)
            

if __name__ == "__main__":
    """ Array: [2,4,2,5,6,1,-2,3,14]

        Heap:  
               14
            /      \
           12       2
         /    \   /  \
        5      6  1   -2
       / \    /
      3   4  2
      
    """
    pri_q = priority_queue()
    pri_q.enqueue(2)
    pri_q.enqueue(4)
    pri_q.enqueue(2)
    pri_q.enqueue(5)
    pri_q.enqueue(6)
    pri_q.enqueue(1)
    pri_q.enqueue(-2)
    pri_q.enqueue(3)
    pri_q.enqueue(14)   
    pri_q.enqueue(12)
    print(pri_q.array)
    pri_q.dequeue(12)
    print(pri_q.array)