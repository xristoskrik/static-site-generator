

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