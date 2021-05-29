class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        
    def addChild(self, name):
        self.children.append(name)

    def addChildren(self, children):
        self.children.extend(children)


def depth_first_search_recursively(root, result): # DFS (Recursively)
    result.append(root.value)
    dfs_helper(root, result)
   
def dfs_helper(node, result):
    for child in node.children:
        result.append(child.value)
        dfs_helper(child, result)
        
        

from Stacks import Stack2
def depth_first_search_iteratively(root, result):# DFS (Iteratively)
    stack = Stack2()
    stack.push(root)
    
    while len(stack)>0:
        node = stack.pop()
        result.append(node.value)
        
        for idx in reversed(range(len(node.children))):
            stack.push(node.children[idx])
            
            
from Queues import Queue # We need to use queue to make it BFS 
def breadth_first_search(root, result): # BFS 
    queue = Queue()
    queue.enqueue(root)
    
    while len(queue) > 0:
        node = queue.dequeue()
        result.append(node.value)
        
        for child in node.children:
            queue.enqueue(child)
        


if __name__ == '__main__':
    root = Node(5)
    root.addChildren([Node(1), Node(3), Node(6)])
    root.children[0].addChildren([Node(5), Node(7)])
    root.children[2].addChildren([Node(7), Node(8), Node(9)])
    
    dfs_array = []
    depth_first_search_recursively(root, dfs_array)
    print(f'DFS recursively: {dfs_array}')
    
    dfs_array_2 = []
    depth_first_search_iteratively(root, dfs_array_2)
    print(f'DFS iteratively: {dfs_array_2}')
    
    bfs_array = []
    breadth_first_search(root, bfs_array)
    print(f'BFS: {bfs_array}')
    
    """Tree:
                5   
            /   |    \
           1    3     6
          / \       / | \
         5   7     7  8  9
    """