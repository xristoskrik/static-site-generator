import unittest
from inline_markdown import *
class TestTextHtmlNode(unittest.TestCase):
  def test_inline_markdown(self):
    print("start inline markdown test")
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    print(new_nodes)
    node = TextNode("This is text with a **bold text** word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    print(new_nodes)
    node = TextNode("This is text with a *italic text* word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
    print(new_nodes)
    node = TextNode(None, TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
    print(new_nodes)
    node = TextNode("text", None)
    new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
    print(new_nodes)
 