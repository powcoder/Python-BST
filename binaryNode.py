https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder

"""
A NodeID is defined to be any of:
 - None
 - A BinaryNode
"""

class BinaryNode:
     
     def __init__(self, Value, Parent = None, Left = None, Right = None):
          """
          BinaryNode(Value, Parent, Left, Right): creates a new BinaryNode
          __init__: Any NodeID NodeID NodeID -> BinaryNode
          """
          self._value = Value
          self._parent = Parent
          self._left = Left
          self._right = Right
     
     def get_parent(self):
          """
          self.get_parent(): returns the parent of self
          get_parent: BinaryNode -> NodeID
          """          
          return self._parent
     
     def get_left(self):
          """
          self.get_left(): returns the left child of self
          get_left: BinaryNode -> NodeID
          """          
          return self._left
     
     def get_right(self):
          """
          self.get_right(): returns the right child of self
          get_right: BinaryNode -> NodeID
          """          
          return self._right
     
     def get_value(self):
          """
          self.get_value(): returns the value of self
          get_value: BinaryNode -> NodeID
          """          
          return self._value
     
     def set_parent(self, Parent):
          """
          self.set_parent(Parent): sets the parent of self to be Parent
          set_parent: BinaryNode NodeID -> None
          Effects:
           - the parent of self is modified
          """          
          self._parent = Parent
     
     def set_left(self, Left):
          """
          self.set_left(Left): sets the left child of self to be Left
          set_left: BinaryNode NodeID -> None
          Effects:
           - the left of self is modified
          """          
          self._left = Left
          
     def set_right(self, Right):
          """
          self.set_right(Right): sets the right child of self to be Right
          set_right: BinaryNode NodeID -> None
          Effects:
           - the right of self is modified
          """          
          self._right = Right
          
     def set_value(self, Value):
          """
          self.set_value(Value): sets the value of self to be Value
          set_Value: BinaryNode Any -> None
          Effects:
           - the value of self is modified
          """          
          self._value = Value
          
          