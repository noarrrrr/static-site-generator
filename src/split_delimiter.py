from textnode import TextNode, TextType, textnode_to_htmlnode
from htmlnode import HTMLNode, ParentNode, LeafNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    split_point = 0
    index = 0
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
        else:
            while True == True:
                if node.text[index] == delimiter:
                    if index != 0:
                        result.append(TextNode(node.text[split_point:index], TextType.TEXT))
                    split_point = index
                    index += 1
                    while True == True:
                        if node.text[index] == delimiter:
                            result.append(TextNode(node.text[split_point + 1:index], text_type))
                            index += 1
                            split_point = index
                            break
                        elif index == len(node.text) - 1:
                            raise Exception("delimiter never closed")
                        else:
                            index += 1
                else:
                    if index == len(node.text) - 1:
                        if index == split_point:
                            break
                        else:
                            result.append(TextNode(node.text[split_point:index + 1], TextType.TEXT))
                            break
                    else:
                        index += 1
    return node.split(delimiter)