from modules.htmlnode import *
from modules.textnode import *

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode('b', text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode('i', text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode('code', text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode('a', text_node.text, None, {'href':text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode('img', '', None, {"src":text_node.url, "alt":text_node.text})
    else:
        raise ValueError("Invalid Text Type")
    
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        split_node_text = []
        if node.text_type == TextType.TEXT:
            result.append(node)
        if text_type == TextType.BOLD:
            split_node_text = node.text.split(delimiter)
            if len(split_node_text) < 3 and len(split_node_text) % 2 == 0:
                raise ValueError("No Matching closing delimiter found")
            