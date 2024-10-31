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

    if __name__  == "__main__":
        unittest.main()
