import unittest

from textnode import TextNode, TextType
from htmlnode import LeafNode, textnode_to_htmlnode
from text_to_textnodes import text_to_textnode
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_non_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text chode", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "sdkjcnsvl")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_text_to_html(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = textnode_to_htmlnode(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_modified_text_to_html(self):
        node = TextNode("This text bold as hell", TextType.BOLD)
        self.assertEqual(textnode_to_htmlnode(node), LeafNode("b", "This text bold as hell"))
        node2 = TextNode("This text slanted and shi", TextType.ITALIC)
        self.assertEqual(textnode_to_htmlnode(node2), LeafNode("i", "This text slanted and shi"))
    def test_link_and_img_to_html(self):
        node = TextNode("you dont have to be lonley", TextType.LINK, "farmersonly.com")
        self.assertEqual(textnode_to_htmlnode(node), LeafNode("a", "you dont have to be lonley", {"href": "farmersonly.com"}))
        node2 = TextNode("noods", TextType.IMAGE, 
                         "https://www.modernfarmhouseeats.com/wp-content/uploads/2021/03/chili-lime-shrimp-ramen-2-scaled.jpg")
        self.assertEqual(textnode_to_htmlnode(node2), LeafNode("img", None, {
            "src": "https://www.modernfarmhouseeats.com/wp-content/uploads/2021/03/chili-lime-shrimp-ramen-2-scaled.jpg", 'alt': 'noods'}))
    def test_text_to_textnodes(self):
        node = text_to_textnode(
            "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        self.assertEqual(node, [
    TextNode("This is ", TextType.TEXT),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" and an ", TextType.TEXT),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.TEXT),
    TextNode("link", TextType.LINK, "https://boot.dev")])
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    def test_block_to_block_type(self):
        result = block_to_block_type("### heading")
        self.assertEqual(result, BlockType.HEADING)
        result = block_to_block_type("""```code
block```""")
        self.assertEqual(result, BlockType.CODE)
        result = block_to_block_type("> quote")
        self.assertEqual(result, BlockType.QUOTE)
        result = block_to_block_type("- list\n- items")
        self.assertEqual(result, BlockType.UNORDERED_LIST)
        result = block_to_block_type("1. list\n2. items")
        self.assertEqual(result, BlockType.ORDERED_LIST)
        result = block_to_block_type("normal text")
        self.assertEqual(result, BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()

