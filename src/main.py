from textnode import TextNode,TextType
from htmlnode import *


def main():
 #node = TextNode("This is a text node", NodeType.BOLD, "https://www.boot.dev")
 #print(repr(node)) 
 #node1 = LeafNode("p", "This is a paragraph of text.")
 #node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
# print(node1.to_html())
# print(node2.to_html())
 # node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
  node = TextNode("This is a text node", TextType.TEXT)
  node = TextNode("This is a bold text", TextType.BOLD)
  node = TextNode("This is an italic text", TextType.ITALIC)
  node = TextNode("var x = 42", TextType.CODE)
  node = TextNode("this is a link", TextType.LINK,{"href": "https://www.google.com"})
  node = TextNode("",TextType.IMAGE,{"src": "image.png","alt": "its an image"})
  node2 = HTMLNode.text_node_to_html_node(HTMLNode,node)
  print(node2.tag,node2.value,node2.children,node2.props,type(node2)) 
  print(node2.to_html())
 

main()