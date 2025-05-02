class HtmlNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, htmlnode):
        if (
            self.tag == htmlnode.tag and 
            self.value == htmlnode.value and 
            self.children == htmlnode.children and
            self.props == htmlnode.props
            ):
            return True
        else:
            return False

    def __repr__(self):
        result = f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})"
        return result
    
    def to_html(self):
        raise NotImplementedError("This function is not yet implemented.")
    
    def props_to_html(self):
        result = ''
        if self.props != None:
            for prop in self.props:
                result += f' {prop}="{self.props[prop]}"'
        return result

class LeafNode(HtmlNode):
    def __init__(self, tag, value, children=None, props=None):
        super().__init__(tag, value, children, props)
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        result = f"LeafNode({self.tag}, {self.value}, {self.children}, {self.props})"
        return result
    
    def to_html(self):
        if self.value == None:
            raise ValueError("Value is a Required Parameter")
        if self.children:
            raise ValueError("Leaf Nodes Cannot have Children")
        
        result = ''
        if not self.tag:
            result += self.value
        else:
            result += f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        return result
    
class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag is a Required Parameter")
        if not self.children:
            raise ValueError("Children is a Required Parameter")
        
        result = ''
        result += f'<{self.tag}>'
        for child in self.children:
            result += child.to_html()
        result += f'</{self.tag}>'
        
        return result
