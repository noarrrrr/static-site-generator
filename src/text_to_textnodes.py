from textnode import TextNode, TextType
from split_delimiter import split_nodes_delimiter
from markdown_images_and_links import split_nodes_image, split_nodes_link
delimiter_list = [
    ("**", TextType.BOLD),
    ("_", TextType.ITALIC),
    ("`", TextType.CODE)
]


def text_to_textnode(text):
    if text == "":
        return None
    result = [TextNode(text, TextType.TEXT)]
    for i in delimiter_list:
        result = split_nodes_delimiter(result, i[0], i[1])
    result = split_nodes_image(result)
    result = split_nodes_link(result)
    return result
