from enum import Enum
from htmlnode import HTMLNode, ParentNode, LeafNode

class TextType(Enum):
    TEXT = "Text"
    BOLD = "Bold"
    ITALIC = "Italic"
    CODE = "Code"
    LINK = "Link"
    IMAGE = "Image"

class TextNode:
    def __init__(self, text, TextType, url=None):
        self.text = text
        self.text_type = TextType
        self.url = url
    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    
def textnode_to_htmlnode(textnode):
    if textnode.text_type == TextType.TEXT:
        return LeafNode(None, textnode.text)
    elif textnode.text_type == TextType.BOLD:
        return LeafNode('b', textnode.text)
    elif textnode.text_type == TextType.ITALIC:
        return LeafNode('i', textnode.text)
    elif textnode.text_type == TextType.CODE:
        return LeafNode('code', textnode.text)
    elif textnode.text_type == TextType.LINK:
        return LeafNode('a', textnode.text, {"href": textnode.url})
    elif textnode.text_type == TextType.IMAGE:
        return LeafNode('img', None, {"src": textnode.url, "alt": textnode.text})
    else:
        raise Exception("invalid text type")
    

