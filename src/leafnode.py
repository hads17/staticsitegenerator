from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None):
        self.tag = tag
        self.value = value
        self.props = props

        super().__init__(self)

    def to_html(self):
        if self.value is None:
            raise ValueError("Value is required")
        if self.tag is None:
            return self.value
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
