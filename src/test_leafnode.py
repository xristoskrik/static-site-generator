import unittest
from htmlnode import *
class TextHtmlNode(unittest.TestCase):
  def test_props_to_html(self):
    node = LeafNode("p", "This is a paragraph of text.")
    node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    node3 = LeafNode("a", "Click me!")
    node4 = LeafNode("a", "t", {"href": "https://www.google.com"})
    print(node.to_html())
    print(node2.to_html())
    print(node3.to_html())
    print(node4.to_html())
   