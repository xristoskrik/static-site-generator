from recursive_copy import recursive_copy
from generate_page import generate_page
def main():
  source_dir = 'static'
  destination_dir = 'public'
  recursive_copy(source_dir, destination_dir)
  generate_page("content/index.md","template.html","public/index.html")
 

main()

