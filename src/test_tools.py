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
    
    if __name__  == "__main__":
        unittest.main()
