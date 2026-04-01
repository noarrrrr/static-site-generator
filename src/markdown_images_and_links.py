import re
from textnode import TextNode, TextType

def extract_markdown_images(text):
    result = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return result

def extract_markdown_links(text):
    result = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return result


def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
        else:
            text = node.text
            images = extract_markdown_images(node.text)
            strings = True
            for i in images:
                strings = text.split(f"![{i[0]}]({i[1]})", 1)
                if strings[0] != "":
                    result.append(TextNode(strings[0], TextType.TEXT))
                result.append(TextNode(i[0], TextType.IMAGE, i[1]))
                if strings[1] != "":
                    text = strings[1]
                else:
                    strings = None
            if strings:
                result.append(TextNode(text, TextType.TEXT))
    return result

def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
        else:
            text = node.text
            links = extract_markdown_links(node.text)
            strings = True
            for i in links:
                strings = text.split(f"[{i[0]}]({i[1]})", 1)
                if strings[0] != "":
                    result.append(TextNode(strings[0], TextType.TEXT))
                result.append(TextNode(i[0], TextType.LINK, i[1]))
                if strings[1] != "":
                    text = strings[1]
                else:
                    strings = None
            if strings:
                result.append(TextNode(text, TextType.TEXT))
    return result
