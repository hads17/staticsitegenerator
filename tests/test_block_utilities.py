import unittest

from modules.block_utilities import *


class TestBlockUtilities(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_blocktypes_paragraph(self):
        md="this is a paragraph\nso much paragraphing happening rn"
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.PARAGRAPH
        )
    
    def test_block_to_blocktypes_unordered_list_1(self):
        md="- This is an unordered List\n-More unorder"
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.PARAGRAPH
        )


    def test_block_to_blocktypes_unordered_list_1(self):
        md="1. This is an unordered List\n2. More unorder"
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.ORDERED_LIST
        )
    
    def test_block_to_blocktypes_unordered_list_2(self):
        md="1. This is an unordered List\n2. More unorder\n4. Wrong Order"
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.PARAGRAPH
        )

    def test_block_to_blocktypes_code_1(self):
        md="```This is a code block```"
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.CODE
        )
    def test_block_to_blocktypes_code_2(self):
        md="```This is a code block`"
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.PARAGRAPH
        )
    
    def test_block_to_blocktypes_code_3(self):
        md="`This is a code block```"
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.PARAGRAPH
        )
    
    def test_block_to_blocktypes_Heading_1(self):
        md="1 This is a heading"
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.HEADING
        )

    def test_block_to_blocktypes_Heading_2(self):
        md="7 This is a heading"
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.PARAGRAPH

    
        )
    
    def test_block_to_blocktypes_Heading_3(self):
        md="1This is a heading"
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.PARAGRAPH
        )

    def test_block_to_blocktypes_Quote_1(self):
        md="> This is a Quote"
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.QUOTE
        )

    def test_block_to_blocktypes_Quote_2(self):
        md="< This is a Quote"
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.PARAGRAPH
        )

    def test_block_to_blocktypes_Quote_3(self):
        md=">This is a Quote"
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.QUOTE
        )
if __name__ == "__main__":
    unittest.main()