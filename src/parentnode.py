from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(self)
        self.tag = tag
        self.children = children
        self.props = props

    def __repr__(self):
        return f'ParentNode({self.tag}, {self.children}, {self.props})'

    def to_html(self):
        if self.tag is None:
            raise ValueError('Tag is a required parameter')
        if self.children is None:
            raise ValueError('Children is a required parameter')
        html_string = ''
        if self.props is not None:
            html_string += f'<{self.tag}{self.props_to_html()}>'
        else:
            html_string += f'<{self.tag}>'
        for child in self.children:
            if child.children is not None:
                html_string += child.to_html()
                print(f'parentnode found: {child}')
            else:
                print(f'leafnode found: {child}')
                html_string += child.to_html()
        return html_string + f'</{self.tag}>'
