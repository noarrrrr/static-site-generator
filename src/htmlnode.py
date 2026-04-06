from markdown_blocks import BlockType, markdown_to_blocks , block_to_block_type
from textnode import TextType, TextNode
from text_to_textnodes import text_to_textnode

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children 
        self.props = props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        if not self.props:
            return ""
        result = []
        for i in self.props:
            result.append(f'{i}="{self.props[i]}"')
        return " ".join(result)
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    def __eq__(self, other):
        one = self.tag == other.tag
        two = self.value == other.value
        three = self.children == other.children 
        four = self.props == other.props
        return one and two and three and four
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None and self.tag != "img":
            raise ValueError
        if not self.tag:
            return self.value
        if not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        if self.tag == "img":
            return f"<img {self.props_to_html()}/>"
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("missing tag")
        if not self.children:
            raise ValueError("missing children")
        result_list = []
        for i in self.children:
            result_list.append(i.to_html())
        if self.props:
            return f"<{self.tag} {self.props_to_html()}>{"".join(result_list)}</{self.tag}>"
        return f"<{self.tag}>{"".join(result_list)}</{self.tag}>"
    
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
    

def list_parser(list, type):
    children = []
    splitty = list.split("\n")
    for i in splitty:
        if type == BlockType.ORDERED_LIST:
            i = i.split(". ", 1)[1]
        elif type == BlockType.UNORDERED_LIST:
            i = i[2:]
        textnodes = text_to_textnode(i)
        htmlnodes = []
        for x in textnodes:
            htmlnodes.append(textnode_to_htmlnode(x))
        children.append(ParentNode("li", htmlnodes))
    return children

def markdown_to_html_node(text):
    blocks = markdown_to_blocks(text)
    finished_blocks = []
    for block in blocks:
        type = block_to_block_type(block)
        if type == BlockType.HEADING:
            header_count = 0
            for char in block:
                if char == "#":
                    header_count += 1
                else:
                    break
            children = text_to_textnode(block[header_count+1:])
            for i in range(0, len(children)):
                children[i] = textnode_to_htmlnode(children[i])
        elif type == BlockType.UNORDERED_LIST or type == BlockType.ORDERED_LIST:
            children = list_parser(block, type)
        elif type == BlockType.QUOTE:
            split_block = block.split("\n")
            fixed = []
            for i in split_block:
                fixed.append(i.lstrip(">").strip())
            block = "\n".join(fixed)
            children = text_to_textnode(block)
            for i in range(0, len(children)):
                children[i] = textnode_to_htmlnode(children[i])
        elif type == BlockType.PARAGRAPH:
            children = text_to_textnode(block.replace("\n", " "))
            for i in range(0, len(children)):
                children[i] = textnode_to_htmlnode(children[i])
        else:
            children = [textnode_to_htmlnode(TextNode(block[4:-3], TextType.TEXT))]
        
        if type == BlockType.PARAGRAPH:
            finished_blocks.append(ParentNode("p", children))
        elif type == BlockType.HEADING:
            finished_blocks.append(ParentNode(f"h{header_count}", children))
        elif type == BlockType.CODE:
            finished_blocks.append(ParentNode("pre", [ParentNode("code", children)]))
        elif type == BlockType.QUOTE:
            finished_blocks.append(ParentNode("blockquote", children))
        elif type == BlockType.UNORDERED_LIST:
            finished_blocks.append(ParentNode("ul", children))
        elif type == BlockType.ORDERED_LIST:
            finished_blocks.append(ParentNode("ol", children))
    return ParentNode("div", finished_blocks)
        