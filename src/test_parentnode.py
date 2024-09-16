import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class test_ParentNode(unittest.TestCase):
    def test_nested_parent(self):
        node = ParentNode(
            "div",
            [
                LeafNode("b", "Bold text"),
                ParentNode("div", [LeafNode("b", "Test Parent Node")]),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text")
            ]
            )

        test_result = node.to_html()
        self.assertEqual(test_result, '<div><b>Bold text</b><div><b>Test Parent Node</b></div>Normal text<i>italic text</i>Normal text</div>')

    def test_multi_parent(self):
        node = ParentNode(
            "div",
            [
                LeafNode("b", "Bold text"),
                ParentNode("div", [
                    LeafNode("b", "Test Parent Node"),
                    ParentNode("div",[
                        LeafNode("a", "Test URL", {"href":"https://boot.dev"}),
                        LeafNode(None, "Normal text")
                        ], 
                        {"target":"_blank"}),
                    LeafNode("i", "italic text")]),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text")
            ]
            )
        test_result = node.to_html()
        self.assertEqual(test_result, '<div><b>Bold text</b><div><b>Test Parent Node</b><div target="_blank"><a href="https://boot.dev">Test URL</a>Normal text</div><i>italic text</i></div>Normal text<i>italic text</i>Normal text</div>')
 
    if __name__ == "__main__":
        unittest.main()

