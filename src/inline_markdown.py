from textnode import *
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []
    for item in old_nodes:
        if item.text is not None:
            parts = item.text.split(delimiter)
            for i, part in enumerate(parts):
                if i % 2 == 0:
                    nodes.append(TextNode(part, TextType.TEXT))
                else:
                    nodes.append(TextNode(part, text_type))
    return nodes

def extract_markdown_images(text):
    if text is None:
        return []
    markdown_images = []
    pattern = r'!\[([^\]]+)\]\((http[s]?://[^\)]+)\)'
    matches = re.findall(pattern, text)
    for alt_text, image_url in matches:
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
    nodes = []
    for item in old_nodes:
        if item.text:
            markdown_links = extract_markdown_links(item.text)
            current_pos = 0
            for link_text, link_url in markdown_links:
                link_pattern = f"[{link_text}]({link_url})"
                link_start = item.text.find(link_pattern, current_pos)
                if link_start > current_pos:
                    nodes.append(TextNode(item.text[current_pos:link_start], TextType.TEXT))
                nodes.append(TextNode(link_text, TextType.LINK, link_url))
                current_pos = link_start + len(link_pattern)
            if current_pos < len(item.text):
                nodes.append(TextNode(item.text[current_pos:], TextType.TEXT))
        else:
            nodes.append(item)
    return nodes

def split_nodes_image(old_nodes):
    nodes = []
    for item in old_nodes:
        if item.text:
            markdown_images = extract_markdown_images(item.text)
            current_pos = 0
            for alt_text, image_url in markdown_images:
                image_pattern = f"![{alt_text}]({image_url})"
                image_start = item.text.find(image_pattern, current_pos)
                if image_start > current_pos:
                    nodes.append(TextNode(item.text[current_pos:image_start], TextType.TEXT))
                nodes.append(TextNode(alt_text, TextType.IMAGE, image_url))
                current_pos = image_start + len(image_pattern)
            if current_pos < len(item.text):
                nodes.append(TextNode(item.text[current_pos:], TextType.TEXT))
        else:
            nodes.append(item)
    return nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes