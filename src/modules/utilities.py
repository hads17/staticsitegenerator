from modules.htmlnode import *
from modules.textnode import *
import re

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
        if node.text_type != TextType.TEXT:
            result.append(node)
        else:
            split_node_text = node.text.split(delimiter)
            if len(split_node_text) < 3 and len(split_node_text) % 2 == 0:
                raise ValueError("No Matching closing delimiter found")
            for i in range(0,len(split_node_text)):
                if not split_node_text[i]:
                    pass
                elif i % 2 == 0:
                    result.append(TextNode(split_node_text[i], TextType.TEXT))  
                else:
                    result.append(TextNode(split_node_text[i], text_type))
    return result

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!\!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        node_text = node.text 
        images = extract_markdown_images(node_text)
        if node.text_type != TextType.TEXT:
            result.append(node)
        elif not images:
            result.append(node)
        else:             
            remaining_text = node_text
            for image in images:
                image_split = []
                image_alt = image[0]
                image_url = image[1]
                image_split = remaining_text.split(f'![{image_alt}]({image_url})', 1)
                remaining_text = image_split[1]
                if not image_split[0]:
                    pass
                else:
                    result.append(TextNode(image_split[0], TextType.TEXT))
                result.append(TextNode(image_alt, TextType.IMAGE, image_url))
            if remaining_text.strip():
                result.append(TextNode(remaining_text, TextType.TEXT))
    print(result)
    return result

def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        node_text = node.text 
        images = extract_markdown_links(node_text)
        if node.text_type != TextType.TEXT:
            result.append(node)
        elif not images:
            result.append(node)
        else:             
            remaining_text = node_text
            for image in images:
                image_split = []
                image_alt = image[0]
                image_url = image[1]
                image_split = remaining_text.split(f'![{image_alt}]({image_url})', 1)
                remaining_text = image_split[1]
                if not image_split[0]:
                    pass
                else:
                    result.append(TextNode(image_split[0], TextType.TEXT))
                result.append(TextNode(image_alt, TextType.IMAGE, image_url))
            if remaining_text.strip():
                result.append(TextNode(remaining_text, TextType.TEXT))
    print(result)
    return result
