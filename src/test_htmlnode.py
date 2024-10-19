import unittest
from htmlnode import *
class TextHtmlNode(unittest.TestCase):
  def test_props_to_html(self):
    node =  HTMLNode("a", "node1", None,{"href": "https://www.google.com"})
    node2 = HTMLNode("h1", "node1", None,{"color": "red","font-size": "35px"})
    node3 = HTMLNode("p", "node1", None,None)
    node4 = HTMLNode("p", "node1", None,"haha not good")
    print(node.props_to_html())
    print(node2.props_to_html())
    print(node3.props_to_html())
    print(node4.props_to_html())
   