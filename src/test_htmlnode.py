import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, markdown_to_html_node

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
        
class testTranslationLayer(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_headings(self):
        md = """## h2

### h3

# h1"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>h2</h2><h3>h3</h3><h1>h1</h1></div>")
    

if __name__ == "__main__":
    unittest.main()