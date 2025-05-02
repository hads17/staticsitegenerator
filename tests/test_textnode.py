import unittest

from modules.textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_1(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_2(self):
        node = TextNode("This is a text node", TextType.BOLD, 'www.google.com')
        node2 = TextNode("This is a text node", TextType.BOLD, 'www.google.com')
        self.assertEqual(node, node2)

    def test_not_eq_1(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_2(self):
        node = TextNode("This is a text node", TextType.BOLD, 'www.google.com')
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_not_eq_3(self):
        node = TextNode("This is a BAD node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a BAD node", TextType.BOLD)
        self.assertEqual(node.url, None)

if __name__ == "__main__":
    unittest.main()