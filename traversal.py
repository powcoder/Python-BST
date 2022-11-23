https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
from contiguous import *

def traverse_helper(tree, curr, stored, num):
    if tree.left_child(curr):
        num = traverse_helper(tree, tree.left_child(curr), stored, num)
    stored.store(num, tree.value(curr))
    num += 1
    if tree.right_child(curr):
        num = traverse_helper(tree, tree.right_child(curr), stored, num)
    return num

def traverse(tree):
    """
    tree.traverse(): Returns a new Contiguous containing the NodeIDs of the
        all nodes in tree in the order in-order traversal
    traverse: BinaryTree -> (Contiguous of NodeID)
    """
    nodes = Contiguous(128)
    if tree.is_empty():
        return nodes
    traverse_helper(tree, tree.root(), nodes, 0)
    return nodes    