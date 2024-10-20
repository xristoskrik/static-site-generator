import unittest
from htmlnode import ParentNode,LeafNode
class TestParentNode(unittest.TestCase):
  def test_props_to_html(self):
    print("start test parent ")
    node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode("a", "Click me!", {"href": "https://www.google.com"}),
        LeafNode(None, "test"),
    ],)
  
    print(node.to_html())

   

