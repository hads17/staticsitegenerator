from modules.textnode import *
from modules.htmlnode import *
from modules.utilities import *

def main(): 
    textnode = TextNode('this is a test TextNode', TextType.IMAGE, 'www.google.com')
    print(textnode)
    print(text_node_to_html_node(textnode).to_html())

    #htmlnode = HtmlNode("a", "This is a link to google", None, {'href':'https://www.google.com', 'target':'_blank'})
    #print(htmlnode.props_to_html())
    #print(htmlnode)

    #leafnode = LeafNode("a", "This is a link to google", None, {'href':'https://www.google.com', 'target':'_blank'})
    #print(leafnode.to_html())

    #parentnode = ParentNode(
    #"p",
    #[
    #    LeafNode("b", "Bold text"),
    #    LeafNode(None, "Normal text"),
    #    LeafNode("i", "italic text"),
    #    LeafNode(None, "Normal text"),
    #],
    #)

    #print(parentnode.to_html())




main()
