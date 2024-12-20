#Contains misc functions to ultilize in this project
import re

from textnode import TextNode
from constants import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
        else:
            temp_array = []
            temp_array = node.text.split(delimiter)
            if (len(temp_array) % 2 == 0):
                raise ValueError("Invalid Markdown Syntax")
            for i in range(len(temp_array)):
                if (i % 2 != 0):
                    result.append(TextNode(temp_array[i], text_type))
                elif (temp_array[i] != ''):
                    result.append(TextNode(temp_array[i], TextType.TEXT))
    return result

def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        extracted_images = extract_markdown_images(node.text)
        temp_array = []
        if extracted_images == []:
            result.append(node)
        else:
            for i in range(0,len(extracted_images)):
                sections = node.text.split(f'![{extracted_images[i][0]}]({extracted_images[i][1]})',1)
                temp_array.extend(sections)
                temp_array.append(TextNode(extracted_images[i][0], TextType.IMAGE, extracted_images[i][1]))
                print(temp_array)



def split_nodes_link(old_nodes):
    pass

def extract_markdown_images(text):
    result = []
    result = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return result

def extract_markdown_links(text):
    result = []
    result = re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)", text)
    return result