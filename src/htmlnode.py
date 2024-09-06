class HTMLNode():
    def __init__(self, tag = None, value = None, children =None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Not yet implemented")

    def props_to_html(self):
        if self.props is None:
            return 'this is a test'
        attribute_string = ''
        for p in self.props:
            attribute_string += f' {p}="{self.props[p]}"'
        return attribute_string
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'