import unittest

from modules.htmlnode import *


class TestHtmlNode(unittest.TestCase):
    def test_eq_1(self):
        node = HtmlNode("a", "This is a link to google", None, {'href':'https://www.google.com', 'target':'_blank'})
        node2 = HtmlNode("a", "This is a link to google", None, {'href':'https://www.google.com', 'target':'_blank'})
        self.assertEqual(node, node2)

    def test_not_eq_1(self):
        node = HtmlNode("a", "This is a link to yahoo", None, {'href':'https://www.yahoo.com', 'target':'_blank'})
        node2 = HtmlNode("a", "This is a link to google", None, {'href':'https://www.google.com', 'target':'_blank'})
        self.assertNotEqual(node, node2)
    
    def test_not_eq_2(self):
        node = HtmlNode("a", "This is a link to yahoo", None)
        node2 = HtmlNode("a", "This is a link to google", None)
        self.assertNotEqual(node, node2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None).to_html()

    def test_leaf_with_children(self):
        with self.assertRaises(ValueError):
            LeafNode("p", "Test Value", [LeafNode("p","Test Value 2")]).to_html()

    def test_leaf_no_tag(self):
        node = LeafNode(None, "This is a value")
        self.assertEqual(node.to_html(), "This is a value")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_parentnode_with_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_parentnode_with_no_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()


if __name__ == "__main__":
    unittest.main()