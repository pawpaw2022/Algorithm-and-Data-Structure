"""
    AVL tree is a self-balancing Binary Search Tree (BST)
    where the difference between heights of left and right subtrees cannot be more than one for all nodes. 
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVL_tree:
    # insert a value in AVLtree and return the root
    def insert(self, root, value):
        # Step 1 - Perform normal BST insertion
        if root is None:
            return Node(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        # Step 2 - Update the height of the root
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Step 3 - Get the balance factor
        balance = self.getBalanceFactor(root)

        # Step 4 - Fix the balance including 4 possible cases

        # Case 1 - Left Left 
        if balance > 1 and value < root.left.value:
            return self.rightRotate(root)

        # Case 2 - Right Right
        if balance < -1 and value > root.right.value:
            return self.leftRotate(root)

        # Case 3 - Left Right
        if balance > 1 and value > root.left.value:
            root.left = self.leftRotate(root.left)  # make it straight first
            return self.rightRotate(root)

            # Case 4 - Right Left
        if balance < -1 and value < root.right.value:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root  # already balanced

    # delete a value in AVLtree and return the root
    def delete(self, root, value):
        # Step 1 - Perform a normal BST deletion
        if root is None:
            return root  # value not found

        elif value > root.value:
            root.right = self.delete(root.right, value)

        elif value < root.value:
            root.left = self.delete(root.left, value)

        else:  # value found!
            if root.left is None:  # only have right child
                temp = root.right
                root = None
                return temp

            elif root.right is None:  # only have left child
                temp = root.left
                root = None
                return temp

            else:  # have 2 children, successor needed!
                temp = self.findClosestValue(root.right)
                root.value = temp
                root.right = self.delete(root.right, temp)

        # Step 2 - Update the height of the root
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Step 3 - Get the balance factor
        balance = self.getBalanceFactor(root)

        # Step 4 - Fix the balance including 4 possible cases

        # Case 1 - Left Left 
        if balance > 1 and self.getBalanceFactor(root.left) >= 0:
            return self.rightRotate(root)

        # Case 2 - Right Right
        if balance < -1 and self.getBalanceFactor(root.right) <= 0:
            return self.leftRotate(root)

        # Case 3 - Left Right
        if balance > 1 and self.getBalanceFactor(root.left) < 0:
            root.left = self.leftRotate(root.left)  # make it straight first
            return self.rightRotate(root)

            # Case 4 - Right Left
        if balance < -1 and self.getBalanceFactor(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root  # already balanced

    def leftRotate(self, a):
        """Before:        After:
                A              B
                 \           /   \
                  B   -->   A     C
                 / \         \
                S   C         S
        """
        b = a.right
        s = b.left

        # Rotate
        a.right = s
        b.left = a

        # Update heights
        a.height = 1 + max(self.getHeight(a.left),
                           self.getHeight(a.right))
        b.height = 1 + max(self.getHeight(b.left),
                           self.getHeight(b.right))

        # Return new root
        return b

    def rightRotate(self, a):
        """Before:        After:
                A            B
               /           /   \
              B     -->   C     A
             / \               /
            C   S             S
        """
        b = a.left
        s = b.right

        # Rotate
        b.right = a
        a.left = s

        # Update heights
        a.height = 1 + max(self.getHeight(a.left),
                           self.getHeight(a.right))
        b.height = 1 + max(self.getHeight(b.left),
                           self.getHeight(b.right))

        # Return new root
        return b

    def getHeight(self, root):
        return 0 if not root else root.height

    def getBalanceFactor(self, root):
        return 0 if not root else self.getHeight(root.left) - self.getHeight(root.right)

    def findClosestValue(self, node):
        if node.left is None:
            return node.value

        return self.findClosestValue(node.left)

    def pre_order_print(self, root, result):
        if root is None:
            return
        result.append(root.value)
        self.pre_order_print(root.left, result)
        self.pre_order_print(root.right, result)
        return result


tree = AVL_tree()
root = None
root = tree.insert(root, 10)
root = tree.insert(root, 20)
root = tree.insert(root, 30)
root = tree.insert(root, 40)
root = tree.insert(root, 50)
root = tree.insert(root, 60)
root = tree.insert(root, 70)
root = tree.insert(root, 25)

print(tree.pre_order_print(root, result=[]))

root = tree.delete(root, 25)
root = tree.delete(root, 40)

print(tree.pre_order_print(root, result=[]))
