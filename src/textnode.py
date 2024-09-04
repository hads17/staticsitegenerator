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
