from modules.textnode import *
from modules.htmlnode import *
from modules.text_utilities import *
from modules.block_utilities import *
from modules.html_utilities import *
from modules.utilities import *
from os import *

def main():
    public_path = os.path.join(os.getcwd(), "public")
    copy_static_files_to_public(public_path)




main()
