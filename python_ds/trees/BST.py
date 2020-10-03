from Node import Node

class BST:
    def __init__(self):
        self.root = None
    
    def print_in_order(self):
        def __print_in_order(node):
            if node == None:
                return
            
            __print_in_order(node.left)
            print(node)
            __print_in_order(node.right)

        __print_in_order(self.root)
    
    
    def insert(self, value):
        def __insert(value, node):
            if node.value >= value:
                # Go Left
                if node.left == None:
                    node.left = Node(value)
                else:
                    __insert(value, node.left)
            else:
                # Go Right
                if node.right == None:
                    node.right = Node(value)
                else:
                    __insert(value, node.right)

        if self.root == None:
            self.root = Node(value)
        else:
            __insert(value, self.root)
    

    def size_of(self):
        def __size_of(root):
            if root == None:
                return 0
            return 1 + __size_of(root.left) + __size_of(root.right)
        
        return __size_of(self.root)
    
    def contents_of(self):
        """
        Returns an array containing the elements of that BST in sorted order
        """
        def fill_list(contents_list, node):
            if node == None:
                return
            
            fill_list(contents_list, node.left)
            contents_list.append(node.value)
            fill_list(contents_list, node.right)
        
        contents_list = []
        fill_list(contents_list, self.root)
        return contents_list


    def second_min_in(self):
        """
        Returns the second-smallest element of the given BST, or None 
        if the tree doesn’t have at least two elements
        """
        stack = []
        root = self.root
        k = 2

        if root == None or root.left == root.right == None:
            return None
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root
            root = root.right
