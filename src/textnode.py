from leafnode import LeafNode

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
        return f'TextNode({self.text}, {self.text_type}, {self.url})'

    def text_node_to_html_node(self):
        if self.text_type == "text":
            return LeafNode(None, self.text)
        if self.text_type == "bold":
            return LeafNode("b", self.text)
        if self.text_type == "italic":
            return LeafNode("i", self.text)
        if self.text_type == "code":
            return LeafNode("code", self.text)
        if self.text_type == "link":
            return LeafNode("a", self.text, {"href":f"{self.url}"})
        if self.text_type == "image":
            return LeafNode("img", '', {"src":f"{self.url}","alt":f"{self.text}"})
        else:
            raise ValueError("Invalid Text_Type Used")
