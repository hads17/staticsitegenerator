from leafnode import LeafNode
from constants import *

class TextNode():
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, compare):
        if self.text == compare.text and self.text_type == compare.text_type and self.url == compare.url:
            return True
        return False

    def __repr__(self):
        return f'TextNode("{self.text}", {self.text_type}, "{self.url}")'

    def text_node_to_html_node(self):
        if self.text_type == TextType.TEXT:
            return LeafNode(None, self.text)
        if self.text_type == TextType.BOLD:
            return LeafNode("b", self.text)
        if self.text_type == TextType.ITALIC:
            return LeafNode("i", self.text)
        if self.text_type == TextType.CODE:
            return LeafNode("code", self.text)
        if self.text_type == TextType.URL:
            return LeafNode("a", self.text, {"href":f"{self.url}"})
        if self.text_type == TextType.IMAGE:
            return LeafNode("img", '', {"src":f"{self.url}","alt":f"{self.text}"})
        else:
            raise ValueError("Invalid Text_Type Used")
