from textnode import *
def split_nodes_delimiter(old_nodes, delimiter, text_type):
  nodes = []
  for item in old_nodes:
   if text_type is None:
    return nodes
   if item.text is not None:
    words = item.text.split(delimiter)
    for i in range(len(words)):
      if i%2 ==0:
       nodes.append(TextNode(words[i],TextType.TEXT))
      else:
       nodes.append(TextNode(words[i],text_type))
    
  return nodes