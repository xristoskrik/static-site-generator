import unittest
from inline_markdown import *
class TestExtractMarkdownImages(unittest.TestCase):
  def test_extract_markdown_images(self):
   print("markdown_images")
   try: 
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))
    text = None
    print(extract_markdown_images(text))
    text = "![](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))
    text = "!(https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))
    text = "![obi wan]and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))
   except Exception as e:
    print(e)
 
class TestExtractMarkdownLinks(unittest.TestCase):
  def test_extract_markdown_images(self):
   print("markdown_links")
   text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
   print(extract_markdown_links(text))
   text = None
   print(extract_markdown_links(text))
   text = "This is text with a link ![to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
   print(extract_markdown_links(text))
   try:
    text = "This is text with a link (https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(extract_markdown_links(text))
   except Exception as e:
    print(e)
   try: 
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube]"
    print(extract_markdown_links(text))
   except Exception as e:
    print(e)
class TestSplitNodeImages(unittest.TestCase):
   def test_split_node_images(self):
    print("node images")
    node = TextNode(
    "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
    TextType.TEXT,
    )
    result = split_nodes_image([node])
    print(result)
class TestSplitNodeLinks(unittest.TestCase):
    def test_split_node_links(self):
     print("node links")
     node = TextNode(
      "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
     TextType.TEXT,
     )
     result = split_nodes_link([node])
     print(result)