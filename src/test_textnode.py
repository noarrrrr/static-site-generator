import unittest

from textnode import TextNode, TextType, textnode_to_htmlnode
from htmlnode import HTMLNode, ParentNode, LeafNode


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


if __name__ == "__main__":
    unittest.main()

