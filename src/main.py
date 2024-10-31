from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from tools import *
from constants import *

def main():
    text_node = TextNode('This *has valid markup*', TextType.TEXT)
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

    #print(text_node.text_node_to_html_node().to_html()) 
    node_list = []
    text_node2 = TextNode('`This` is text with a `code block` woot', 'text')
    node_list.append(text_node2)
    node_list.append(text_node)
    new_node_list = split_nodes_delimiter(node_list, '*', TextType.ITALIC)
    print(new_node_list)
    for n in new_node_list:
        print(n.text_node_to_html_node().to_html())
    text = text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"

    test_extract_images = extract_markdown_images(text)
    test_extract_links = extract_markdown_links(text)

    print(test_extract_images)
    print(test_extract_links)
main()
