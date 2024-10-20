import unittest
from htmlnode import HTMLNode,LeafNode
from textnode import TextNode,TextType
class TestTextHtmlNode(unittest.TestCase):
  def test_props_to_html(self):
    print("start convertion test")
    nodes = [TextNode("This is a text node", TextType.TEXT),
               TextNode("This is a bold text", TextType.BOLD),
              TextNode("This is an italic text", TextType.ITALIC),
                TextNode("var x = 42", TextType.CODE),
               TextNode("this is a link", TextType.LINK,{"href": "https://www.google.com"}),
              TextNode("",TextType.IMAGE,{"src": "image.png","alt": "its an image"})
                
               ]
    for item in nodes:
     htmlnodeTest = HTMLNode.text_node_to_html_node(HTMLNode,item)
     print(htmlnodeTest.tag,htmlnodeTest.value,htmlnodeTest.children,htmlnodeTest.props,type(htmlnodeTest)) 
     print(htmlnodeTest.to_html())