from pathlib import Path
import os
import subprocess
import shutil

from bs4 import BeautifulSoup

SCRIPT_DIR = Path(__file__).resolve()
POSTS_DIR = SCRIPT_DIR.parent.parent / "posts"
MD_DIR = POSTS_DIR / "raw md"
INDEX_FILE = SCRIPT_DIR.parent.parent / "posts.html"

def convert_and_link():

    # Get a list of all markdown files
    md_files = [f for f in os.listdir(POSTS_DIR) if f.endswith('.md')]
    
    links = []

    for md_file in md_files:
        name_root = os.path.splitext(md_file)[0]
        html_filename = f"{name_root}.html"
        pandoc_input = os.path.join(POSTS_DIR, md_file)
        pandoc_output = os.path.join(POSTS_DIR, html_filename)
        md_destination = os.path.join(MD_DIR, md_file)
        html_loc = "/posts/" + html_filename

        #TODO: Remove the comments on the lines below before final push

        #1. Run Pandoc to convert the markdown to html
        subprocess.run(['pandoc', pandoc_input, '-o', pandoc_output])

        #2. Move the markdown file
        shutil.move(pandoc_input, md_destination)

        #3. Add new html file to link index
        # links.append(f'<li><a href="{html_loc}">{name_root.replace("-", " ").title()}</a></li>')
        # print(links)
        # print('\n')

    #4. Update the posts html page
    # update_posts(links)

def update_posts(new_links):
    
    # Read in the html file
    with open(INDEX_FILE, 'r') as f:
        index = BeautifulSoup(f, 'html.parser')

    # TODO: Write code to look for the link list and append the new links
    for l in new_links:
        newadd = BeautifulSoup(l, 'html.parser')
        index.ul.append(newadd)

    print(index.prettify())

    with open(INDEX_FILE, 'w') as f:
        f.write(index.prettify())

if __name__ == "__main__":
    convert_and_link()