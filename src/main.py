from modules.textnode import *
from modules.htmlnode import *
from modules.text_utilities import *
from modules.block_utilities import *

def main(): 
    md="1. This is an unordered List\n2. More unorder\n4. wrong order"
    print(block_to_block_type(md))




main()
