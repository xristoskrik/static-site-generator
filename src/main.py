from recursive_copy import recursive_copy
from generate_page import generate_pages_recursive
def main():
  source_dir = 'static'
  destination_dir = 'public'
  recursive_copy(source_dir, destination_dir)
  generate_pages_recursive("content","template.html","public/")
 

main()

