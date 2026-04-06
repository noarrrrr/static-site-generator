from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "Paragraph"
    HEADING = "Heading"
    CODE = "Code"
    QUOTE = "Quote"
    UNORDERED_LIST = "Unordered List"
    ORDERED_LIST = "Ordered List"

def markdown_to_blocks(text):
    splitty = text.split("\n\n")
    result = []
    for i in splitty:
        if i != "" and i != "\n":
            stripped = i.strip()
            result.append(stripped)
    return result

def block_to_block_type(block):
    if block.startswith("#"):
        return BlockType.HEADING
    if block.startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        return BlockType.QUOTE
    if block.startswith("- "):
        return BlockType.UNORDERED_LIST
    if block.startswith("1."):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def extract_title(md):
    blocks = markdown_to_blocks(md)
    for block in blocks:
        if block_to_block_type(block) == BlockType.HEADING:
            header_count = 0
            for char in block:
                if char == "#":
                    header_count += 1
                else:
                    break
            if header_count == 1:
                return block.split("#", 1)[1].strip()
    raise Exception("No Title Found")