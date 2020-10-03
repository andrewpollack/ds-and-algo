from BST import BST

test_BST = BST()

print(test_BST.size_of())

# test_BST.insert(3)
# test_BST.insert(2)
test_BST.insert(1)
test_BST.insert(4)
test_BST.insert(6)


test_BST.print_in_order()
print(test_BST.size_of())

print(test_BST.contents_of())

# print(test_BST.second_min_in())