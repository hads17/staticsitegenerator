from modules.textnode import *
from modules.htmlnode import *
from modules.utilities import *

def main(): 
    text = 'This is **text** with an _italic word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
    print(text_to_textnodes(text))




main()
