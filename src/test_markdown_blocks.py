import unittest
from markdown_blocks import *
class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )
    def test_block_to_block_types(self):
     text = "# heading"
     self.assertEqual(block_to_block_type(text), BlockType.HEADING)
     text = "```\ncode\n```"
     self.assertEqual(block_to_block_type(text), BlockType.CODE)
     text = "> quote\n> more quote"
     self.assertEqual(block_to_block_type(text), BlockType.QUOTE)
     text = "* list\n* items"
     self.assertEqual(block_to_block_type(text), BlockType.UNORDERED_LIST)
     text = "1. list\n2. items"
     self.assertEqual(block_to_block_type(text), BlockType.ORDERED_LIST)
     text = "paragraph"
     self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)



if __name__ == "__main__":
    unittest.main()
