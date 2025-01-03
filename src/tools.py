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
        nodetext = node.text
        extracted_images = extract_markdown_images(nodetext)
        if extracted_images == []:
            result.append(node)
        else:
            for image in extracted_images:
                temp_array = []
                section = nodetext.split(f'![{image[0]}]({image[1]})',1)
                if section[0] != '':
                    temp_array.append(TextNode(section[0], TextType.TEXT))
                temp_array.append(TextNode(image[0], TextType.IMAGE, image[1]))
                nodetext = nodetext.replace(section[0],'')
                nodetext = nodetext.replace(f'![{image[0]}]({image[1]})','')
                result.extend(temp_array)
            if nodetext != '':
                result.append(TextNode(nodetext, TextType.TEXT))
    return result

def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        nodetext = node.text
        extracted_links = extract_markdown_links(nodetext)
        if extracted_links == []:
            result.append(node)
        else:
            for link in extracted_links:
                temp_array = []
                section = nodetext.split(f'[{link[0]}]({link[1]})',1)
                if section[0] != '':
                    temp_array.append(TextNode(section[0], TextType.TEXT))
                temp_array.append(TextNode(link[0], TextType.URL, link[1]))
                nodetext = nodetext.replace(section[0],'')
                nodetext = nodetext.replace(f'[{link[0]}]({link[1]})','')
                result.extend(temp_array)   
            if nodetext != '':
                result.append(TextNode(nodetext, TextType.TEXT))
    return result

def extract_markdown_images(text):
    result = []
    result = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return result

def extract_markdown_links(text):
    result = []
    result = re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)", text)
    return result