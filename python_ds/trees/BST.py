from Node import Node

class BST:
    def __init__(self):
        self.root = None
    
    def print_in_order(self):
        self.__print_in_order(self.root)
    
    def __print_in_order(self, node):
        if node == None:
            return
        
        print(self.__print_in_order(node.left))
        print(node)
        print(self.__print_in_order(node.right))
    
    def insert(self):
        pass
    
    def free_tree(self):
        pass
    
    def size_of(self):
        pass
    
    def contents_of(self):
        """
        Returns an array containing the elements of that BST in sorted order
        """
        pass
    
    def second_min_in(self):
        """
        Returns the second-smallest element of the given BST, or None 
        if the tree doesn’thave at least two elements
        """
        pass
        
