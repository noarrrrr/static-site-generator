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
        if not self.value and self.tag != "img":
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
    