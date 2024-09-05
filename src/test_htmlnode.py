import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_tag_none(self):
        htmlnode = HTMLNode()
        self.assertIsNone(htmlnode.tag)

    def test_value_none(self):
        htmlnode = HTMLNode()
        self.assertIsNone(htmlnode.value)

    def test_children_none(self):
        htmlnode = HTMLNode()
        self.assertIsNone(htmlnode.children)

    def test_props_none(self):
        htmlnode = HTMLNode()
        self.assertIsNone(htmlnode.props)

    def test_error_raise(self):
        htmlnode = HTMLNode()
        with self.assertRaises(NotImplementedError):
            htmlnode.to_html()

    def test_props_to_html(self):
        htmlnode = HTMLNode("a", "anchor", [], {"href":"https://www.boot.dev", "target":"_blank"})
        self.assertEqual(htmlnode.props_to_html(), ' href="https://www.boot.dev" target="_blank"')


    if __name__ == "__main__":
        unittest.main()
