from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from tools import *
from constants import *

def main():
    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    text_to_textnodes(text)

main()
