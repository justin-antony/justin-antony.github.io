import os
import shutil
import subprocess

# Configuration
SOURCE_DIR = 'posts'
OUTPUT_DIR = 'posts'
MD_STORE = 'posts/raw md'
INDEX_FILE = 'posts.html'

def convert_and_link():
    # Ensure output directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Get a list of all markdown files
    md_files = [f for f in os.listdir(SOURCE_DIR) if f.endswith('.md')]
    
    links = []

    for md_file in md_files:
        name_root = os.path.splitext(md_file)[0]
        html_filename = f"{name_root}.html"
        input_path = os.path.join(SOURCE_DIR, md_file)
        output_path = os.path.join(OUTPUT_DIR, html_filename)

        # 1. Run Pandoc
        subprocess.run(['pandoc', input_path, '-o', output_path])

        # 2. Move markdown files to subfolder
        shutil.move(md_file,MD_STORE)
        
        # 2. Store the link for the index
        links.append(f'<li><a href="{output_path}">{name_root.replace("-", " ").title()}</a></li>')

    # 3. Update the Index Page
    update_index(links)

def update_index(new_links):
    # This logic looks for a specific placeholder in your HTML to insert links
    with open(INDEX_FILE, 'r') as f:
        content = f.read()

    # Create the block of links
    links_html = "\n".join(new_links)
    
    # Simple replacement logic: look for tags in your index.html
    start_tag = ""
    end_tag = ""
    
    if start_tag in content and end_tag in content:
        head = content.split(start_tag)[0]
        tail = content.split(end_tag)[1]
        new_content = f"{head}{start_tag}\n<ul>\n{links_html}\n</ul>\n{end_tag}{tail}"
        
        with open(INDEX_FILE, 'w') as f:
            f.write(new_content)

if __name__ == "__main__":
    convert_and_link()