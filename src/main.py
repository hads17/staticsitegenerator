from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode

def main():
    text_node = TextNode('This is a text node', 'bold', 'https://www.boot.dev')
    print(text_node)

    html_node = HTMLNode('p', 'This is a paragraph', [], {"href":"https://www.boot.dev", "target":"_blank"})
    print(html_node)
    print(html_node.props_to_html())
    
    leaf_node = LeafNode('a', 'This is an anchor', {"href":"https:www.google.com", "target":"_blank"})
    print(leaf_node)

main()
