from textnode import TextNode,TextType

class HTMLNode():
  def __init__(self,tag = None,value = None,children = None ,props = None):
   self.tag = tag
   self.value = value
   self.children = children
   self.props = props
  def to_html(self):
   raise Exception(NotImplementedError)
  def __repr__(self):
   return f"HTLMNode({self.tag},{self.value!r}, {self.children!r}, {self.props!r})"
  def text_node_to_html_node(self,text_node):
   match(text_node.text_type):
    case TextType.TEXT:
     return LeafNode(None,text_node.text)
    case TextType.BOLD:
     return LeafNode('b',text_node.text)
    case TextType.ITALIC:
      return LeafNode('i',text_node.text)
    case TextType.CODE:
     return LeafNode('code',text_node.text)
    case TextType.LINK:
     return LeafNode('a',text_node.text,text_node.url)
    case TextType.IMAGE:
     return LeafNode('img',text_node.text,text_node.url)
    case default:
     raise Exception(ValueError)
  def props_to_html(self):
   if type(self.props)!=dict:
    return ""
   final_text = ""
   for k,v in self.props.items():
    final_text+=f'{k}="{v}" '
   return final_text


class LeafNode(HTMLNode):
   def __init__(self,tag = None,value = None,props = None):
    super().__init__(tag,value,None,props)
   def to_html(self):
    if self.value is None:
     raise Exception(ValueError)
    if self.tag is None:
     return self.value
    props = self.props_to_html()
    if props != "":
     return f"<{self.tag} {props[:len(props)-1]}>{self.value}</{self.tag}>"
    return f"<{self.tag}>{self.value}</{self.tag}>"
   
class ParentNode(HTMLNode):
  def __init__(self,tag = None,children = None,props = None):
   super().__init__(tag,None,children,props)
  def to_html(self):
   if self.tag is None:
    raise Exception(ValueError)
   if self.tag is None:
    raise ValueError("no children")
   final_str=f"<{self.tag}>"
   for item in self.children:
    final_str+=item.to_html()
   return  f"{final_str}</{self.tag}>"