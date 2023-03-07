#!/usr/bin/env python3

# Iterate through all directories in src/, in each subdirectory, find the only file that does not start with number, use it as the file to insert TOC into
# for all other files that start with number, use their file name as the link text, and insert them into the TOC file, in the order of their file name
# the first underscore in the file name is replaced with ". ", and the rest of the underscores are replaced with spaces

import json
import sys
import os
import re

def generate_toc(dir, sub_dir):
    toc = ""
    for file in os.listdir(os.path.join("src", dir, sub_dir)):
        if file[0].isdigit():
            fname = [x for x in file[2:].replace('.md', '').split('_') if x]
            # remove empty strings in fname
            # make sure the first letter of each word is capitalized
            fname = ' '.join([word.capitalize() for word in fname])
            toc += f"* [{file[:2]}. {fname}]({file})\n"
        else:
            main_file = file
    main_file_path = os.path.join("src", dir, sub_dir, main_file)
    with open(main_file_path, "r") as f:
        content = f.read()
    # if there is already a TOC, remove it
    content = re.sub(r"<!-- toc -->.*<!-- toc -->",
                     f"<!-- toc -->\n{toc}<!-- toc -->", content, flags=re.DOTALL)
    with open(main_file_path, "w") as f:
        f.write(content)

def main():
    for _, dirs, _ in os.walk("src"):
        for dir in dirs:
            for _, sub_dirs, _ in os.walk(os.path.join("src", dir)):
                for sub_dir in sub_dirs:
                    generate_toc(dir, sub_dir)

if __name__ == '__main__':
    if len(sys.argv) > 1: # we check if we received any argument
        if sys.argv[1] == "supports":
            # then we are good to return an exit status code of 0, since the other argument will just be the renderer's name
            sys.exit(0)

    main()
