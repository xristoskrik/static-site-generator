from markdown_blocks import markdown_to_html_node
from markdown_blocks import extract_title
import os
def generate_page(from_path, template_path, dest_path):
  print(f"Generating page from {from_path} to {dest_path} using {template_path}")
  file = open(from_path,"r")
  content_from_path = file.read()
  html_node = markdown_to_html_node(content_from_path)
  html_content = html_node.to_html()
  template_file = open(template_path,"r")
  content_template = template_file.read()
  title = extract_title(content_from_path)
  page_content = content_template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
  os.makedirs(os.path.dirname(dest_path), exist_ok=True)
  dest_file =  open(dest_path, "w")
  dest_file.write(page_content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
  for root, _, files in os.walk(dir_path_content):
   for file in files:
     if file.endswith(".md"):
        from_path = os.path.join(root, file)
        relative_path = os.path.relpath(from_path, dir_path_content)
        dest_path = os.path.join(dest_dir_path, os.path.splitext(relative_path)[0] + ".html")
        generate_page(from_path, template_path, dest_path)