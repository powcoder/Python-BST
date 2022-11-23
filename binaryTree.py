https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
from binaryNode import *
from contiguous import *

class BinaryTree:
    
    def __init__(self):
        """
        BinaryTree(): creates and empty Binary Tree
        __init__: Void -> BinaryTree
        """
        self._root = None
    
    def is_empty(self):
        """
        self.is_empty(): returns True if self is empty, otherwise False
        is_empty: BinaryTree -> Bool
        """
        return self._root == None
    
    def root(self):
        """
        self.root(): returns the ID of the root node of self
        root: BinaryTree -> NodeID
        Requires: self is non-empty
        """
        return self._root
    
    def value(self, ID):
        """
        self.value(ID): returns the value store in ID
        value: BinaryTree NodeID -> Any
        Requires: ID represents a node that exists in self
        """
        return ID.get_value()
    
    def parent(self, ID):
        """
        self.parent(ID): returns the ID of the parent node of ID
        parent: BinaryTree NodeID -> (anyof NodeID False)
        Requires: ID represents a node that exists in self
        """
        if ID.get_parent() == None:
            return False
        return ID.get_parent()
    
    def left_child(self, ID):
        """
        self.left_child(ID): returns the ID of the left child of ID
        left_child: BinaryTree NodeID -> (anyof NodeID False)
        Requires: ID represents a node that exists in self
        """
        if ID.get_left() == None:
            return False
        return ID.get_left()
    
    def right_child(self, ID):
        """
        self.right_child(ID): returns the ID of the right child of ID
        right_child: BinaryTree NodeID -> (anyof NodeID False)
        Requires: ID represents a node that exists in self
        """
        if ID.get_right() == None:
            return False
        return ID.get_right()         
    
    def set_value(self, ID, Value):
        """
        self.set_value(ID, value): sets the Value to be stored at ID
        set_value: BinaryTree NodeID Any -> None
        Requires: ID represents a node that exists in self
        Effects: the value stored at ID is modified
        """
        return ID.set_value(Value)
    
    def add_leaf(self, Value, ParentID = None, Side = ""):
        """
        self.add_leaf(ParentID, Side, Value): creates a new tree node storing
            Value as the Side child of ParentID. If ParentNode is None, Value
            is stored as the root node with no children.
            Returns the NodeID of the newly created tree node.
        add_leaf: BinaryTree NodeID String Any -> NodeID
        Requires:
         - ParentID is either a valid ID in self or is None
         - If ParentID is None, Side is ""
         - If ParentID is not None, Side is "Left" or "Right"
        """
        if ParentID == None:
            self._root = BinaryNode(Value)
            return self._root
        newLeaf = BinaryNode(Value, ParentID)
        if Side == "Left":
            ParentID.set_left(newLeaf)
        else:
            ParentID.set_right(newLeaf)
        return newLeaf
    
