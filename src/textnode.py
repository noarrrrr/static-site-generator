from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "Bold Text"
    ITALIC = "Italic Text"
    CODE = "Code text"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, TextType, url=None):
        self.text = text
        self.text_type = TextType
        self.url = url
    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    def assertEqual(self, other):
        return self.__eq__(self, other)
    def assertNotEqual(self, other):
        return not self.__eq__(self, other)

    
def main():
    dummynode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(dummynode)