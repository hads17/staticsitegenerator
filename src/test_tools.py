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

    if __name__  == "__main__":
        unittest.main()


