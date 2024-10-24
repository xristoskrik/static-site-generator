from textnode import TextNode,TextType
from htmlnode import *
from inline_markdown import *


def main():
 node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
 )
 result = split_nodes_link([node])
 print(result)
 node = TextNode(
   "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
    TextType.TEXT,
 )
 result = split_nodes_image([node])
 print(result)
 

 

main()

