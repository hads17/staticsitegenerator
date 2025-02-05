from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from tools import *
from constants import *

def main():
    text = "# This is a heading\n\n\n           This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
    markdown_to_blocks(text)

main()
 