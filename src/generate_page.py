from markdown_blocks import markdown_to_html_node
from markdown_blocks import extract_title
import os
def generate_page(from_path, template_path, dest_path):
  print(f"Generating page from {from_path} to {dest_path} using {template_path}")
  file = open(from_path,"r")
  content_from_path = file.read()
  html_node = markdown_to_html_node(content_from_path)
  html_content = html_node.to_html()
  #print(html_content)
  template_file = open(template_path,"r")
  content_template = template_file.read()
  title = extract_title(content_from_path)
  #print(title)
  page_content = content_template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
  os.makedirs(os.path.dirname(dest_path), exist_ok=True)
  dest_file =  open(dest_path, "w")
  dest_file.write(page_content)