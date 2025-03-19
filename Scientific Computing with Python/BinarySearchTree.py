#learn-tree-traversal-by-building-a-binary-search-tree
#https://github.com/freeCodeCamp/freeCodeCamp/tree/main/curriculum/challenges/english/07-scientific-computing-with-python/learn-tree-traversal-by-building-a-binary-search-tree
#In this project, you are going to create a Binary Search Tree (BST). 
#A BST is a data structure in which each node has at most two children, with the left child containing values less than the parent node and the right child containing values greater than the parent node, allowing for efficient searching and sorting operations

class TreeNode:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)

class BinarySearchTree:

    def __init__(self):
        #The root attribute represents the root node of the binary search tree. 
        #Since this is the constructor when a new BinarySearchTree object is created, it starts with an empty tree, so the root attribute is set to None
        self.root = None

    #Next, you need to define a mechanism to insert nodes in the tree. For that, you need to define an _insert method, which is a helper function and would be used by the actual insert method later on.
    #This method is recursive, meaning it calls itself to traverse the tree until the appropriate location for the new node is found.

    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)
        
    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)
    
    def search(self, key):
        return self._search(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key) 
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left   
            
            node.key = self._min_value(node.right)
            node.right = self._delete(node.right, node.key)   
        
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _min_value(self, node):
        while node.left is not None:
            node = node.left
        return node.key

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

bst = BinarySearchTree()
nodes = [50, 30, 20, 40, 70, 60, 80]

for node in nodes:
    bst.insert(node)

print('Search for 80:', bst.search(80))

print("Inorder traversal:", bst.inorder_traversal())

bst.delete(40)

print("Search for 40:", bst.search(40))

print("Inorder traversal after deleting 40:", bst.inorder_traversal())