from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from tools import *

def main():
    text_node = TextNode('This is a text node', 'link', 'https://www.boot.dev')
    #print(text_node)

    html_node = HTMLNode('p', 'This is a paragraph', [], {"href":"https://www.boot.dev", "target":"_blank"})
    #print(html_node)
    #print(html_node.props_to_html())
    
    leaf_node = LeafNode('a', 'This is an Anchor', {"href":"https:www.google.com", "target":"_blank"})
    
    #print(leaf_node.to_html())
    
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

    #print(node.to_html())

    print(text_node.text_node_to_html_node().to_html()) 
main()
