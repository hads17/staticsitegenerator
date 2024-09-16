import unittest
from leafnode import LeafNode

class test_LeafNode(unittest.TestCase):
    def test_ValueRequired(self):
        leaf_node = LeafNode('p')
        with self.assertRaises(ValueError):
            leaf_node.to_html()

    def test_DefaultNone(self):
        leaf_node = LeafNode('p')
        self.assertIsNone(leaf_node.props)

    def test_to_html(self):
        leaf_node = LeafNode('a', 'this is an anchor', {'href':'https://www.bootdev.com','target':'_blank'})
        test_string = '<a href="https://www.bootdev.com" target="_blank">this is an anchor</a>'
        self.assertEqual(leaf_node.to_html(), test_string)

    if __name__ == "__main__":
        unittest.main()

