# Max Heap Construction

def heapify(array, heap_size, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    
    if left < heap_size and array[left] > array[largest]: # swap left to parent
        largest = left
    
    if right < heap_size and array[right] > array[largest]: # swap right to parent
        largest = right
    
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, heap_size, largest)

def insert(array, num):
    # check if array is empty
    if len(array) == 0:
        array.append(num)
    
    else:
        array.append(num)
        for i in reversed(range(len(array)//2 + 1)):
            heapify(array, len(array), i)


def delete(array, num):
    # check if num is in array
    if num not in array:
        return
    else:
        num_idx = array.index(num)
        
        array[num_idx], array[-1] = array[-1], array[num_idx] # switch the target num to the last one
        array.pop() # remove the last one
        
        for i in reversed(range(len(array)//2 + 1)):
            heapify(array, len(array), i)
            

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
    array = []
    insert(array, 2)
    insert(array, 4)
    insert(array, 2)
    insert(array, 5)
    insert(array, 6)
    insert(array, 1)
    insert(array, -2)
    insert(array, 3)
    insert(array, 14)   
    insert(array, 12)
    print(array)
    delete(array, 12)
    print(array)


