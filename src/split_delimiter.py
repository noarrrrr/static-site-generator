from textnode import TextNode, TextType, textnode_to_htmlnode
from htmlnode import HTMLNode, ParentNode, LeafNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
        else:
            strings = node.text.split(delimiter)
            if len(strings) % 2 == 0:
                raise Exception("delimiter not closed")
            if strings[0] != "":
                result.append(TextNode(strings[0], TextType.TEXT))
            if len(strings) > 2:
                fancy = True
                for i in strings[1:]:
                    if fancy == True:
                        result.append(TextNode(i, text_type))
                        fancy = False
                    else:
                        result.append(TextNode(i, TextType.TEXT))
                        fancy = True
    return result