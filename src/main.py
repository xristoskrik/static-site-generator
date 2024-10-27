from textnode import TextNode,TextType
from htmlnode import *
from inline_markdown import *
from markdown_blocks import markdown_to_blocks,block_to_block_type


def main():
  text = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
  #print(text)
  markdown_blocks = markdown_to_blocks(text)
  for item in markdown_blocks:
    print(block_to_block_type(item))
    #print(item)

 

main()

