"""
Sorting Algorithms:
    
    Classic:
        1. Selection Sort
        2. Insertion Sort
        3. Bubble Sort
        
    Advanced:
        4. Merge Sort
        5. Quick Sort
        6. Heap Sort
        
    Others:
        7. Counting Sort
        8. Radix Sort
        9. Bucket Sort
        10. Shell Sort
        
Searching Algorithms:
    
    Classic:
        1. Linear Search
        2. Binary Search
"""


# Testing Function to test if a array is sorted.
def isSorted(array):
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            return False
    return True


# 1. Selection Sort
def selectionSort(array):
    """A classic sorting algorithm:
        1.Find the smallest item in the list, and swap it into index 0
        2.Find the smallest item in the remainder of the list (starting at idx 1), and swap to index 1
        3.Find the smallest item in the remainder of the list (starting at idx 2), and swap to index 2
        4.Continue until we've swapped into the second last index.
        --------------------------------------------------------------
        Time Complexity =  O(n^2) Always
        Space Complexity = O(1) 
        Stability: unstable
    """
    for i in range(len(array)):
        smallest_idx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[smallest_idx]:
                smallest_idx = j
        # swap
        array[i], array[smallest_idx] = array[smallest_idx], array[i]

    return array


# Testing selection sort
array = [2, 4, 2, 5, 6, 1, -2, 3, 14]
print('Classic Algorithms:')
print(f'My array is {array}')
print(f'1. After Selection sort, my array is {selectionSort(array)}')
print(f'Array {"is" if isSorted(selectionSort(array)) else "is not"} sorted.')
print('-' * 70)


# 2. Insertion Sort
def insertionSort(array):
    """ A classic sorting algorithm:
    The insertion-sort algorithm sorts a list of values by repeatedly inserting a new element into a sorted sublist until the whole list is sorted. 
    --------------------------------------------------------------
    Time Complexity =  O(n^2) Worst, O(n) Best || BEST when the array is nearly sorted, WORST when the array is completely reversed.
    Space Complexity = O(1)
    Stability: stable
    """
    for i in range(1, len(array)):
        cur_ele = array[i]
        k = i - 1
        while k >= 0 and array[k] > cur_ele:
            array[k + 1] = array[k]
            k -= 1

        array[k + 1] = cur_ele
    return array


# Testing insertion sort
array = [2, 4, 2, 5, 6, 1, -2, 3, 14]
print(f'My array is {array}')
print(f'2. After insertion sort, my array is {insertionSort(array)}')
print(f'Array {"is" if isSorted(insertionSort(array)) else "is not"} sorted.')
print('-' * 70)


# 3. Bubble Sort
def bubbleSort(array):
    """ A classic sorting algorithm:
        1. Make a 'pass' through the list:
            a. Compare the first element to the second element, and swap them if the first if bigger than the second
            b. Compare the second to the third element, and swap them if the second is bigger than the third
            c. Continue this until the second last element is compared to the last (and swapped if the second last is bigger than the last).
        2. Now go back and make another pass through the list, but stopping the comparisons one element earlier than the previous pass.
        3. Repeat step 2 until n-1 passes have been made through the list, where n is the size of the list. 
    --------------------------------------------------------------
    Time Complexity =  O(n^2) Always
    Space Complexity = O(1)
    Stability: stable
    """
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


# Testing bubble sort
array = [2, 4, 2, 5, 6, 1, -2, 3, 14]
print(f'My array is {array}')
print(f'3. After bubble sort, my array is {bubbleSort(array)}')
print(f'Array {"is" if isSorted(bubbleSort(array)) else "is not"} sorted.')
print('-' * 70)


# 4. Merge Sort
def mergeSort(array):
    """Recursive Algorithm:
        1. if the list has one element, then return (it's sorted).
        2. Split up the list into 2 equal sections.
        3. Recursively call merge_sort function on the left half & the right half.
        4. Merge the 2 halves by calling the merge function.
    --------------------------------------------------------------
    Time Complexity =  O(nlogn) Always
    Space Complexity =  O(n) || It requires more space to store the splitted elements.
    Stability: stable
    """
    if len(array) <= 1:  # Base case
        return array

    mid = len(array) // 2  # Set the mid point
    left = array[:mid]
    right = array[mid:]

    left = mergeSort(left)
    right = mergeSort(right)  # Using recursion cutting the array into half until we get every single element.

    return merge_two_arrays(left, right, array)


def merge_two_arrays(left, right,
                     array):  # using this function to keep merging sub-arrays till it becomes to a entire array

    i = j = k = 0  # i -> idx of left array | j -> idx of right array | k -> idx of original array.

    while i < len(left) and j < len(
            right):  # each time we compare each ele in both L & R. Place the smaller one into orignial array.
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
            k += 1
        else:
            array[k] = right[j]
            j += 1
            k += 1

    while i < len(left):  # if one of the sub-arrays runs out, keep adding the rest elements. 
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

    return array


# Testing merge sort
print('Advanced Algorithms: ')
array = [2, 4, 2, 5, 6, 1, -2, 3, 14]
print(f'My array is {array}')
print(f'4. After merge sort, my array is {mergeSort(array)}')
print(f'Array {"is" if isSorted(mergeSort(array)) else "is not"} sorted.')
print('-' * 70)


# 5. Quick Sort
def quickSort(array):
    """Recursive Algorithm:
        1. Pivot Selection: the algorithem selects an element, called 'Pivot' (In this case, we select the last element)
        2. Partitioning Step: put the pivot element into our final sorted array, with all other smaller elements to the left, and larger elements to the right.
        3. Recursion Step: recursively call step 1 & 2, until we get all elements sorted in the final array.
    -----------------------------------------------------------------------------------------
    Time Complexity =  O(nlogn) best, O(n^2) worst. || NOTE: BEST when each time the pivot is placed right in the middle, WORST when each time the pivot is placed in the leftmost or rightmost.
    Space Complexity = O(logn)
    Stability: unstable
    """
    if len(array) <= 1:
        return array  # base case
    else:
        pivot = array.pop()  # get the last element as the pivot.

    # partition step
    lower_ele = []
    higher_ele = []

    for ele in array:
        if ele <= pivot:
            lower_ele.append(ele)
        else:
            higher_ele.append(ele)

    return quickSort(lower_ele) + [pivot] + quickSort(higher_ele)


# Testing Quick sort
array = [2, 4, 2, 5, 6, 1, -2, 3, 14]
print(f'My array is {array}')
print(f'5. After quick sort, my array is {quickSort(array)}')
print(f'Array {"is" if isSorted(quickSort(array)) else "is not"} sorted.')
print('-' * 70)


# 6. Heap Sort
def heapSort(array):
    """Advanced Sorting Algorithm using HEAP data structure:
        1. Build a Max Heap. i.e. All nodes in the tree follow the property that they are greater than their children
        2. Work on Heap Sort:
            a. Since the tree satisfies Max-Heap property, then the largest item is stored at the root node.
            b. Swap: Remove the root element and put at the end of the array (nth position) Put the last item of the tree (heap) at the vacant place.
            c. Remove: Reduce the size of the heap by 1.
            d. Heapify: Heapify the root element again so that we have the highest element at root.
            e. The process is repeated until all the items of the list are sorted.
     -----------------------------------------------------------------------------------------
        Time Complexity =  O(nlogn) Always
        Space Complexity = O(1)
        Stability: unstable
    """
    length = len(array)
    # Build up a max heap
    for i in reversed(
            range(length // 2 + 1)):  # start from the mid, traverse backwards 1 at a time till the 1st element.
        heapify(array, length, i)

    # Heap sort
    for j in reversed(range(length)):  # start from the end, traverse backwards 1 at a time till the 2nd element.

        # Swap the root (largest) of the heap to the tail 
        array[j], array[0] = array[0], array[j]

        # Remove the tail & Heapify the root
        heapify(array, j, 0)

    return array


def heapify(array, heap_size, parentIdx):
    """
    Takes in parentIdx and find out if the parent node is the largest among its children. If not, swap the largest to the parent. 
    """

    largest = parentIdx  # assume the parent is the largest.

    left = 2 * parentIdx + 1  # left child = 2*i+1
    right = 2 * parentIdx + 2  # right child = 2*i+2

    # check if children are larger than the parent.
    if left < heap_size and array[largest] < array[left]:
        largest = left

    if right < heap_size and array[largest] < array[right]:
        largest = right

    # if the largest one has been replaced: 1. swap parent and child. 2. recursivly call heapify till the child's children are heapified.
    if largest != parentIdx:
        array[parentIdx], array[largest] = array[largest], array[parentIdx]
        heapify(array, heap_size, largest)


# Testing Heap sort
array = [2, 4, 2, 5, 6, 1, -2, 3, 14]
print(f'My array is {array}')
print(f'6. After heap sort, my array is {heapSort(array)}')
print(f'Array {"is" if isSorted(heapSort(array)) else "is not"} sorted.')
print('-' * 70)


# 7. Counting Sort
def countingSort(array):
    """Easy soring algorithm:
            A sorting algorithm that sorts the elements of an array by counting the number of occurrences of each unique element in the array.
            The count is stored in an auxiliary array and the sorting is done by mapping the count as an index of the auxiliary array.
        
        1. Build a Counting array to store the occurrences:
            a. Find out the maximum element from the given array.
            b. Initialize an array of length(max+1) with all 0, which will be used for storing the counts.
            c. Store the count of each element at their respective index in the count array (step b)
        2. Accumulate the sum of the elements of the count array. It helps in placing the elements into the correct index of the sorted array.
        3. Map the index of each element of the original array in count array, and position the element in sorted array at index(count[element]-1)
        4. After placing each element at its correct position, decrease its count by one.
        
        NOTE: Counting Sort CAN'T deal with negative number. But preforms well when there are smaller integers with multiple counts.
    -----------------------------------------------------------------------------------------
    Time Complexity =  O(n+k) where n = len(array) and k = max(array)
    Space Complexity = O(k)  k = max(array), the larger the max of the array, the more space it takes.
    Stability: stable
    """
    size = len(array)

    output = [0] * size  # initialize the output array (length = original array) filled with 0
    count = [0] * (max(
        array) + 1)  # initialize the counting array (length = the max element of the array + 1) filled with 0

    for i in range(len(array)):  # count the occurrences of the array.
        count[array[i]] += 1

    for i in range(1, len(count)):  # accumulate the sum of the occurences
        count[i] += count[i - 1]

    for num in array:
        pos = count[num] - 1  # map the element from original array to count array
        count[num] = pos  # update the count array
        output[pos] = num  # place the element in sorted array.

    return output


# Testing counting sort
print('Other Algorithms:')
array = [2, 4, 2, 4, 10, 1, 3, 6]
print(f'My array is {array}')
print(f'7. After counting sort, my array is {countingSort(array)}')
print(f'Array {"is" if isSorted(countingSort(array)) else "is not"} sorted.')
print('-' * 70)


# 8. Radix Sort
def radixSort(array):
    """Improved sorting algorithm based on counting sort:
            it sorts the elements by first grouping the individual digits of the same place value.
            Then, sort the elements according to their increasing/decreasing order.
            
        1. Find the max number in array, which represents all the significant places of all elements we have to go through.
        2. Using counting sort(or any other stable sorting algorithm) to sort each significant place one by one.
        3. Continue sorting at ten place, hundreds place ...
        
        NOTE: Radix sort handles well with large number(unlike Counting sort), but CAN'T handle negative numbers.
    -----------------------------------------------------------------------------------------
    Time Complexity =  O(n+k) where n = len(array) and k = max(array)
    Space Complexity = O(k)  k = max(array), the larger the max of the array, the more space it takes.
    Stability: stable
    """
    # Get the maximum element
    max_element = max(array)

    # Apply counting sort to help sort elements based on place value
    place = 1
    while max_element // place > 0:
        countingSortHelper(array, place)
        place *= 10

    return array


def countingSortHelper(array, place):
    size = len(array)

    output = [0] * size
    count = [0] * 10  # obviously the value range of each place is from 0 to 9, so we initialize 10 empty space.

    for i in range(size):  # count occurrences
        index = array[i] // place
        count[index % 10] += 1  # locating the number of that particular place.

    for i in range(1, 10):  # accumulate
        count[i] += count[i - 1]

    for i in reversed(range(len(
            array))):  # Note: this step requires reversed traversal, because the larger number needs to be placed behind.
        index = array[i] // place
        pos = count[index % 10] - 1
        count[index % 10] = pos
        output[pos] = array[i]

    for i in range(size):
        array[i] = output[i]


# Testing Radix sort
array = [121, 432, 564, 23, 1, 45, 788]
print(f'My array is {array}')
print(f'8. After Radix sort, my array is {radixSort(array)}')
print(f'Array {"is" if isSorted(radixSort(array)) else "is not"} sorted.')
print('-' * 70)


# 9. Bucket Sort
def bucketSort(array):
    """A sorting algorithm:
            it sorts the elements by first dividing the elements into several groups called buckets.
            The elements inside each bucket are sorted using any of the suitable sorting algorithms or recursively calling the same algorithm.
        
        1. Create an array-length empty array as buckets for storing elements
        2. Insert elements into the buckets from the array according to the range. i.e. 0.23 & 0.28 will be store in the same No.2 bucket.
        3. Using other sorting algorithm(i.e. insertion sort) to sort the elements in each bucket
        4. The elements from each bucket are gathered.
        
        NOTE: bucketSort handles well when there are floating point values & input is uniformly distributed over a range.
    -----------------------------------------------------------------------------------------
    Time Complexity =  O(n+k) Best, O(n^2) Worst, O(n) Average. || BEST when the elements are uniformly distributed, Worst when all elements are stored in a single bucket.
    Space Complexity = O(n+k)  
    Stability: stable

    """
    buckets = []
    output = []

    # Create empty buckets
    for _ in range(len(array)):
        buckets.append([])

    # Insert elements into their respective buckets
    for element in array:
        index = int(10 * element)
        buckets[index].append(element)

    # Sort the elements of each bucket
    for i in range(len(array)):
        buckets[i] = sorted(buckets[i])  # feel free to use any other sorting algorithm i.e. insertion sort

    # append the sorted element into output array
    for bucket in buckets:
        for ele in bucket:
            output.append(ele)

    return output


# Testing Bucket sort
array = [.42, .32, .33, .52, .37, .47, .51]
print(f'My array is {array}')
print(f'9. After Bucket sort, my array is {bucketSort(array)}')
print(f'Array {"is" if isSorted(bucketSort(array)) else "is not"} sorted.')
print('-' * 70)


# 10. Shell Sort
def shellSort(array):
    """Advanced sorting algorithm based on Insertion Sort:
            it first sorts the elements far apart from each other and successively reduces the interval between the elements to be sorted.
        1. Make an interval (gap), n//2, n//4, n//8 ....
        2. Compare element with its previous gap index of element
        3. Continue step 2 till the current gap of elements are sorted
        4. Narrow the gap and continue step 2&3 till all elements are sorted.
    -----------------------------------------------------------------------------------------
    Time Complexity =  O(nlogn) best, average, O(n^2) worst
    Space Complexity = O(1)  
    Stability: unstable
    """
    gap = len(array) // 2
    while gap > 0:
        for i in range(gap, len(array)):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap //= 2
    return array


# Testing Shell sort
array = [2, 4, 2, 5, 6, 1, -2, 3, 14]
print(f'My array is {array}')
print(f'10. After Shell sort, my array is {shellSort(array)}')
print(f'Array {"is" if isSorted(shellSort(array)) else "is not"} sorted.')
print('-' * 70)
