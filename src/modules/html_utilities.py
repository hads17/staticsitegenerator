from modules.text_utilities import *
from modules.block_utilities import *
from modules.htmlnode import *
from modules.textnode import *

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        #Determine Block Type
        block_type = block_to_block_type(block)
        #Split the block into html nodes
        html_nodes.append(block_to_html_node(block_type,block))
    return ParentNode('div', html_nodes)

        
    
#return children

def text_to_children(text):
    result = []
    text_nodes = text_to_textnodes(text)
    for node in text_nodes:
        result.append(text_node_to_html_node(node))
    return result

def block_to_html_node(type, block):
    children = []
    if type != BlockType.CODE:
            block = block.replace("\n", " ")
    if type == BlockType.PARAGRAPH:
        return ParentNode('p', text_to_children(block))
    elif type == BlockType.CODE:
        block = block.strip("```").lstrip("\n")
        text_node = TextNode(block, TextType.TEXT)
        return ParentNode('pre', [ParentNode('code', [text_node_to_html_node(text_node)])])
    elif type == BlockType.HEADING:
        headernumber = f'h{children[0][0]}'
        return ParentNode(headernumber, text_to_children(block))
    elif type == BlockType.QUOTE:
        return ParentNode('blockquote', text_to_children(block))
    elif type == BlockType.ORDERED_LIST or type == BlockType.ORDERED_LIST:
        split_block = block.split('\n')
        list_nodes = []
        for b in split_block:
            list_nodes.append(ParentNode('li', text_to_children(b)))
        if type == BlockType.ORDERED_LIST:
            return ParentNode('ol', list_nodes)
        if type == BlockType.UNORDERED_LIST:
            return ParentNode('ul', list_nodes)
    else:
        raise ValueError("Invalid block type provided")