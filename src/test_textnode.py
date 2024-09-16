import unittest

from textnode import TextNode
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_dif(self):
        node = TextNode("This is a text node", "italics", "https://www.testwebsite.xyz")
        node2 = TextNode("This is a text node", "italics")
        self.assertNotEqual(node, node2)

    def test_urlnone(self):
        node = TextNode("This will test URL Null Default", "bold")
        self.assertIsNone(node.url)

    def test_to_html_bad_text_type(self):
        with self.assertRaises(ValueError):
            TextNode("test Text", "badValue").text_node_to_html_node()

    def test_to_html_good_text_type(self):
        node = TextNode("This is a text node", "image", "https://www.boot.dev")

        self.assertEqual(node.text_node_to_html_node().to_html(), LeafNode("img", "", {"src":"https://www.boot.dev", "alt":"This is a text node"}).to_html())

    if __name__ == "__main__":
        unittest.main()
