from textnode import *
from htmlnode import *


def main():
 #node = TextNode("This is a text node", NodeType.BOLD, "https://www.boot.dev")
 #print(repr(node)) 
 node1 = LeafNode("p", "This is a paragraph of text.")
 node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
 print(node1.to_html())
 print(node2.to_html())
 #print(node.props_to_html())
 

main()