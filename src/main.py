from modules.textnode import *
from modules.htmlnode import *
from modules.utilities import *

def main(): 
    node = TextNode(
        "![google](https://google.com) This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)       trailing text",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])




main()
