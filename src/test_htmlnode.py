import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class testHTMLNode(unittest.TestCase):
    def test_createnode(self):
        node = HTMLNode("h1", "testing123", None, {
    "href": "https://www.google.com",
    "target": "_blank"})
    
    def test_props_to_html(self):
        node = HTMLNode("h1", "testing123", None, {
    "href": "https://www.google.com",
    "target": "_blank"})
        node.props_to_html()
    def test_equal(self):
        node1 = HTMLNode("h1", "testing123", None, {
    "href": "https://www.google.com",
    "target": "_blank"})
        node2 = HTMLNode("h1", "testing123", None, {
    "href": "https://www.google.com",
    "target": "_blank"})
        self.assertEqual(node1, node2)
    def test_nonequal(self):
        node1 = HTMLNode("h1", "testing123", None, {
    "href": "https://www.google.com",
    "target": "_blank"})
        node2 = HTMLNode("a", "testing1234", None, {
    "href": "https://www.google.com",
    "target": "_blank"})
        self.assertNotEqual(node1, node2)

class testLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    def test_leaf_to_html_img(self):
        node = LeafNode("img", None, {"src": "url/of/image.jpg", "alt": "Description of image"})
        self.assertEqual(node.to_html(), '<img src="url/of/image.jpg" alt="Description of image"/>')

class testParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>")
    
    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("h1", [child_node], {
    "href": "https://www.google.com",
    "target": "_blank"})
        self.assertEqual(parent_node.to_html(), 
                         '<h1 href="https://www.google.com" target="_blank"><span>child</span></h1>')
    

if __name__ == "__main__":
    unittest.main()