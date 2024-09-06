from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(self)
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if tag is None:
            raise ValueError('Tag is a required parameter')
        if children is None:
            raise ValueError('Children is a required parameter')
        
        
