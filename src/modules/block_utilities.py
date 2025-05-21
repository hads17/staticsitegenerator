from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'


def markdown_to_blocks(markdown):
    split_strings = markdown.split("\n\n")
    result = []
    for string in split_strings:
        if string:
            result.append(string.strip("\n "))
    return result

def block_to_block_type(block):
    if block.startswith(('1 ','2 ','3 ','4 ','5 ','6 ')):
        return BlockType.HEADING
    elif block.startswith('```') and block.endswith('```'):
        return BlockType.CODE
    elif block.startswith('>'):
        return BlockType.QUOTE
    elif block.startswith('- '):
        lines = block.split("\n")
        if len(lines) > 1:
            for i in range(0, len(lines)):
                if not lines[i].startswith('- '):
                    return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    elif block.startswith('1. '):
        lines = block.split("\n")
        if len(lines) > 1:
            for i in range(0, len(lines)):
                if not lines[i].startswith(f'{i + 1}. '):
                    return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH