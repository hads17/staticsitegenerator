import unittest

from textnode import TextNode
from constants import *
from tools import *

class testTools(unittest.TestCase):
    def test_invalid_markup(self):
        nodelist = [] 
        nodelist.append(TextNode('This has *invalid Markdown', TextType.TEXT))
        with self.assertRaises(ValueError, msg="Invalid Markdown Syntax"):
            split_nodes_delimiter(nodelist, '*', TextType.ITALIC)

    def test_Extract_Images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected_value = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extract_markdown_images(text), expected_value)

    def test_Extract_Links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected_value = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extract_markdown_links(text), expected_value)

    def test_split_nodes_image(self):
        textnodearray = [TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT)]
        expected_value = [TextNode("This is text with a ", TextType.TEXT), TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"), TextNode(" and ", TextType.TEXT), TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(split_nodes_image(textnodearray), expected_value)

    def test_split_nodes_image_multiple(self):
        textnodearray = [TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT), TextNode("This is another test ![additional test](https://testurl.com)", TextType.TEXT), TextNode("This is just a string", TextType.TEXT)]
        expected_value = [TextNode("This is text with a ", TextType.TEXT), TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"), TextNode(" and ", TextType.TEXT), TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"), TextNode("This is another test ", TextType.TEXT), TextNode("additional test", TextType.IMAGE, "https://testurl.com"), TextNode("This is just a string", TextType.TEXT)]
        self.assertEqual(split_nodes_image(textnodearray), expected_value)

    def test_split_nodes_link(self):
        textnodearray = [TextNode("This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT)]
        expected_value = [TextNode("This is text with a ", TextType.TEXT), TextNode("rick roll", TextType.URL, "https://i.imgur.com/aKaOqIh.gif"), TextNode(" and ", TextType.TEXT), TextNode("obi wan", TextType.URL, "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(split_nodes_link(textnodearray), expected_value)

    def test_split_nodes_link_multiple(self):
        textnodearray = [TextNode("This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT), TextNode("This is another test [additional test](https://testurl.com)", TextType.TEXT), TextNode("This is just a string", TextType.TEXT)]
        expected_value = [TextNode("This is text with a ", TextType.TEXT), TextNode("rick roll", TextType.URL, "https://i.imgur.com/aKaOqIh.gif"), TextNode(" and ", TextType.TEXT), TextNode("obi wan", TextType.URL, "https://i.imgur.com/fJRm4Vk.jpeg"), TextNode("This is another test ", TextType.TEXT), TextNode("additional test", TextType.URL, "https://testurl.com"), TextNode("This is just a string", TextType.TEXT)]
        self.assertEqual(split_nodes_link(textnodearray), expected_value)

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected_value = [TextNode("This is ", TextType.TEXT), TextNode("text", TextType.BOLD), TextNode(" with an ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" word and a ", TextType.TEXT),TextNode("code block", TextType.CODE),TextNode(" and an ", TextType.TEXT),TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),TextNode(" and a ", TextType.TEXT),TextNode("link", TextType.URL, "https://boot.dev")]   
        self.assertEqual(text_to_textnodes(text), expected_value)

    def test_markdown_to_blocks(self):
        array = markdown_to_blocks("# This is a heading\n\n\n           This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item")
        expected_value = ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", "* This is the first list item in a list block\n* This is a list item\n* This is another list item"]
        self.assertEqual(array, expected_value)
    
    def test_block_to_block_type(self):
        text1 = "1 this is a sample heading"
        text2 = "12 this is a sample of a paragraph"
        text3 = "```this is a sample of code```"
        text4 = ">this is a sample quote"
        text5 = "* this is a sample unordered list\n* I am super unordered\n* more unordered list!"
        text6 = "1. this is a sample ordered list\n2. I am ordered\n3. Order up!"
        text7 = "1. this is a sample of a bad ordered list\n3. This should be a paragraph type now\n2. uh oh!"

        self.assertEqual(block_to_block_type(text1), BlockType.HEADING)
        self.assertEqual(block_to_block_type(text2), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(text3), BlockType.CODE)
        self.assertEqual(block_to_block_type(text4), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(text5), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type(text6), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type(text7), BlockType.PARAGRAPH)

    if __name__  == "__main__":
        unittest.main()


