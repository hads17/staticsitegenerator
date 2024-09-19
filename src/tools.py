#Contains misc functions to ultilize in this project
from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for node in old_nodes:
        temp_list = []
        temp_list = node.text.split(f"{delimiter}")
        for n in range(0, len(temp_list)):
            #print(temp_list[n])
            split_node = None
            if (n % 2 != 0):
                split_node = TextNode(temp_list[n], text_type)
                new_list.append(split_node)
            elif temp_list[n] != "":
                split_node = TextNode(temp_list[n], 'text')
                new_list.append(split_node)
    print(new_list)
    return new_list
