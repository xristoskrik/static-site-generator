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
        raise ValueError("Not every image alt text has a URL")

    for i in range(len(matches_name)):
        alt_text = matches_name[i][2:-1] 
        image_url = matches_link[i][1:-1] 
        markdown_images.append((alt_text, image_url))

    return markdown_images
def extract_markdown_links(text):

    if text is None:
        return []

    markdown_links = []
    matches_name = re.findall(r'\[.*?\]', text)
    matches_link = re.findall(r'\(.*?\)', text)

    if len(matches_name) != len(matches_link):
        raise ValueError("Not every link has a URL")

    for i in range(len(matches_name)):
        link_text = matches_name[i][1:-1] 
        link_url = matches_link[i][1:-1]  
        markdown_links.append((link_text, link_url))

    return markdown_links

def split_nodes_link(old_nodes):

    original_text = old_nodes[0].text
    markdown_links = extract_markdown_links(original_text)

    nodes = []
    current_pos = 0

   
    for link_text, link_url in markdown_links:
     
        link_pattern = f"[{link_text}]({link_url})"
        link_start = original_text.find(link_pattern, current_pos)
        if link_start > current_pos:
            before_link_text = original_text[current_pos:link_start]
            nodes.append(TextNode(before_link_text, TextType.TEXT))
        nodes.append(TextNode(link_text, TextType.LINK, link_url))
        current_pos = link_start + len(link_pattern)
    if current_pos < len(original_text):
        remaining_text = original_text[current_pos:]
        nodes.append(TextNode(remaining_text, TextType.TEXT))

    return nodes
def split_nodes_image(old_nodes):
    original_text = old_nodes[0].text
    markdown_images = extract_markdown_images(original_text)
    nodes = []
    current_pos = 0 
    for alt_text, image_url in markdown_images:
        image_pattern = f"![{alt_text}]({image_url})"
        image_start = original_text.find(image_pattern, current_pos)
        if image_start > current_pos:
            before_image_text = original_text[current_pos:image_start]
            nodes.append(TextNode(before_image_text, TextType.TEXT))
        nodes.append(TextNode(alt_text, TextType.IMAGE, image_url))
        current_pos = image_start + len(image_pattern)
    if current_pos < len(original_text):
        remaining_text = original_text[current_pos:]
        nodes.append(TextNode(remaining_text, TextType.TEXT))

    return nodes