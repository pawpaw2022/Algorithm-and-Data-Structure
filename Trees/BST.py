class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

def insert(root, node):
    if root is None: # check if the root exists.
        root = node
    else:
        if root.value > node.value: # smaller to left, larger to right.
            if root.left is None: # check if the current node reachs the end
                root.left = node  
            else:
                insert(root.left, node) 
        else:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
                

def contains(root, value):
    """ return true if the tree contains the node value, else False
    """
    if root is None:
        return False 
    
    if value == root.value:
        return True
    
    elif value > root.value:
        return contains(root.right, value)
    else:
        return contains(root.left, value)


def remove(root, value):
    """remove the first instance node from the tree given the value.
    1. if the node has 2 children, replace the node value with the right closest node, and remove that node.
    2. if the node has 1 child, connect the child with the node's parent.
    3. if the node has 0 child, simply delete that node.
    4. if the tree is a single tree, removing value is the top, we replace the root with root.child.
    """
    return removeHelper(root, value, parent = None)

def removeHelper(node, value, parent):
    if node.left is None and node.right is None and parent is None: # tree only contains a root
        return
    
    if node.value < value: # start traverse till we find target node
        return removeHelper(node.right, value, node)
    elif node.value > value:
        return removeHelper(node.left, value, node)
    
    else: # now we reach the target node
        if node.left and node.right:
            closest_value = find_closest_value(node.right)
            node.value = closest_value
            removeHelper(node.right, closest_value, node)
        
        elif parent is None:
            if node.left:
                node.value = node.left.value
                node.left = node.left.left
                node.right = node.left.right
            else:
                node.value = node.right.value
                node.left = node.right.left
                node.right = node.right.right
        
        else:
            if parent.left == node:
                parent.left = node.left if node.left else node.right
                
            elif parent.right == node:
                parent.right = node.left if node.left else node.right
                
            
            
def find_closest_value(node):
    if node.left is None:
        return node.value
    else:
        return find_closest_value(node.left)
                

"""
With inorder traversal,
the left subtree of the current node is visited first,
then the current node,
and finally the right subtree of the current node.

The inorder traversal displays all the nodes in a BST in increasing order. 
"""
def in_order_print(root, result):
    if root is None:
        return
    in_order_print(root.left, result)
    result.append(root.value)
    in_order_print(root.right, result)
    
    
    

"""
With preorder traversal,
the current node is visited first,
then the left subtree of the current node,
and finally the right subtree of the current node.

Depth-first traversal is the same as preorder traversal.
"""
def pre_order_print(root, result):
    if root is None:
        return
    
    result.append(root.value)
    
    pre_order_print(root.left,result)
    pre_order_print(root.right,result)



"""
With postorder traversal,
the left subtree of the current node is visited first,
then the right subtree of the current node,
and finally the current node itself. 
"""
def post_order_print(root, result):
    if root is None:
        return
    
    post_order_print(root.left,result)
    post_order_print(root.right,result)
        
    result.append(root.value)
    
    
"""
Depth-first traversal is to visit the root, then recursively visit its left subtree and right subtree in an arbitrary order.
The preorder traversal can be viewed as a special case of depth-first traversal,
which recursively visit its left subtree and then its right tree.

"""
def depth_first_search_recursively(root, result): # DFS (Recursively)
    if root is None:
        return
    
    result.append(root.value)
    
    depth_first_search_recursively(root.left, result)
    depth_first_search_recursively(root.right, result)
    
    
from Stacks import Stack2
def depth_first_search_iteratively(root, result):# DFS (Iteratively)
    stack = Stack2()
    stack.push(root)
    
    while len(stack)>0:
        node = stack.pop()
        result.append(node.value)
        
        if node.right:
            stack.push(node.right)
        if node.left:
            stack.push(node.left)


"""
With breath_first traversal, the nodes are visited level by level.
First the root is visited,
then all the children of the root from left to right,
then the grandchildren of the root from left to right, and so on.
"""
from Queues import Queue # We need to use queue to make it BFS 
def breadth_first_search(root, result): # BFS 
    queue = Queue()
    queue.enqueue(root)
    
    while len(queue) > 0:
        node = queue.dequeue()
        result.append(node.value)
        
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)
    
    
    
if __name__ == '__main__':
    root = Node(10)
    insert(root, Node(6))
    insert(root, Node(3))
    insert(root, Node(8))
    insert(root, Node(1))
    insert(root, Node(4))
    insert(root, Node(9))
    insert(root, Node(13))
    insert(root, Node(11))
    insert(root, Node(14))
    
    
    print(f'13 existing in the tree is {contains(root, 13)} ')
    print(f'31 existing in the tree is {contains(root, 31)} ')

    in_order_array = []
    in_order_print(root, in_order_array)
    print(f'in order: {in_order_array}')
    
    pre_order_array = []
    pre_order_print(root, pre_order_array)
    print(f'pre order: {pre_order_array}')
    
    post_order_array = []
    post_order_print(root, post_order_array)
    print(f'post order: {post_order_array}')
    
    
    
    dfs_array = []
    depth_first_search_recursively(root, dfs_array)
    print(f'depth first search recursively: {dfs_array}')


    dfs_array_2 = []
    depth_first_search_iteratively(root, dfs_array_2)
    print(f'depth first search iteratively: {dfs_array_2}')
    
    
    bfs_array = []
    breadth_first_search(root, bfs_array)
    print(f'breadth first search: {bfs_array}')
    
    remove(root, 8)
    array = []
    breadth_first_search(root, array)
    print(f'bfs after removing 8: {array}')

    remove(root, 10)
    array2 = []
    breadth_first_search(root, array2)
    print(f'bfs after removing 10: {array2}')
    
    
    """ Tree:
              10
           /     \
          6      13
         / \    /  \
        3   8  11  14
       / \   \
      1  4    9
    """
    print('-'*60)
    
    single_root = Node(1)
    insert(single_root, Node(2))
    insert(single_root, Node(3))
    insert(single_root, Node(4))
    insert(single_root, Node(5))
    
    
    array = []
    depth_first_search_recursively(single_root, array)
    print(f'single tree dfs: {array}')
    
    remove(single_root, 1)
    array2 = []
    depth_first_search_recursively(single_root, array2)
    print(f'single tree dfs after removing 1: {array2}')
    
    
    """Single Tree:
        1
         \
          2
           \
            3
             \
              4
               \
                5
    """
    
    
