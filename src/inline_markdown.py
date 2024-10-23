from textnode import *
import re
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
def extract_markdown_images(text):
 if text is None:
  return []
 markdown_images = []
 matches_name = re.findall(r'\!\[.*?\]', text)
 matches_link = re.findall(r'\(.*?\)', text)
 if len(matches_name) != len(matches_link):
  raise ValueError("Not every name have a link")
 for i in range(len(matches_name)):
  markdown_images.append((matches_name[i][2:-1] , matches_link[i][1:-1]))
 return markdown_images
def extract_markdown_links(text):
 # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
 if text is None:
  return []
 markdown_links = []
 matches_name = re.findall(r'\[.*?\]', text)
 matches_link = re.findall(r'\(.*?\)', text)
 if len(matches_name) != len(matches_link):
  raise ValueError("Not every name have a url")
 for i in range(len(matches_name)):
  markdown_links.append((matches_name[i][1:-1] , matches_link[i][1:-1]))
 return markdown_links


