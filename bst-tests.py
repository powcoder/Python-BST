https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
from binarySearchTree import *
from traversal import *

def clean_contig(lst):
    array = []
    for index in range(0, lst.size()):
        if lst.access(index) != None:
            array.append(lst.access(index))
        else:
            break
    return array

def empty_test():
    bst = BinarySearchTree()
    expected = True
    result = bst.is_empty()

def insert():
    bst = BinarySearchTree()
    expected = [True, False, 7]
    result = []
    result.append(bst.is_empty())
    node = bst.insert(7)
    result.append(bst.is_empty())
    result.append(bst.value(node))

    
def find():
    bst = BinarySearchTree()
    expected = [7, 4, 12]
    result = []
    bst.insert(7)
    bst.insert(4)
    bst.insert(12)
    node = bst.find(7)
    result.append(bst.value(node))
    node = bst.find(4)
    result.append(bst.value(node))
    node = bst.find(12)
    result.append(bst.value(node))

    
def not_found():
    bst = BinarySearchTree()
    expected = [11]
    result = []
    bst.insert(6)
    bst.insert(11)
    bst.insert(3)
    node = bst.find(7)
    result.append(bst.value(node))

    
def search():
    bst = BinarySearchTree()
    expected = [True, True, True, False, False, False, False]
    result = []
    bst.insert(25)
    bst.insert(3)
    bst.insert(72)
    result.append(bst.search(25))
    result.append(bst.search(3))
    result.append(bst.search(72))
    result.append(bst.search(-3))
    result.append(bst.search(17))
    result.append(bst.search(65))
    result.append(bst.search(101))

def order():
    bst = BinarySearchTree()
    expected = [2, 4, 5, 6, 25, 72]
    result = [] 
    bst.insert(6)
    bst.insert(2)
    bst.insert(4)
    bst.insert(5)
    bst.insert(25)
    bst.insert(72)
    result = clean_contig((traverse(bst.tree())))
