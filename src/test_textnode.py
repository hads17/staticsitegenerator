import unittest

from textnode import TextNode

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

    if __name__ == "__main__":
        unittest.main()
