#!/usr/bin/env python3

# Iterate through all directories in src/, in each subdirectory, find the only file that does not start with number, use it as the file to insert TOC into
# for all other files that start with number, use their file name as the link text, and insert them into the TOC file, in the order of their file name
# the first underscore in the file name is replaced with ". ", and the rest of the underscores are replaced with spaces

import json
import sys
import os
import re

# hash table for words that should not be capitalized
# for example, "of" should not be capitalized
# this is used to make sure the first letter of each word is capitalized
# but not the first letter of the whole file name
# for example, "01. of the world" should be "01. Of the World"
# instead of "01. Of The World"
htable = {
    "of": 1,
    "the": 1,
    "a": 1,
    "an": 1,
    "and": 1,
    "or": 1,
    "nor": 1,
    "but": 1,
    "is": 1,
    "at": 1,
    "from": 1,
    "by": 1,
    "on": 1,
    "off": 1,
    "for": 1,
    "in": 1,
    "out": 1,
    "over": 1,
    "to": 1,
    "into": 1,
    "with": 1,
}

htable_upper = {
    "i": 1,
    "ii": 1,
    "iii": 1,
    "iv": 1,
    "v": 1,
    "vi": 1,
    "vii": 1,
    "viii": 1,
    "ix": 1,
    "x": 1,
}

htable_strict = {
    "mirna": "miRNA",
    "mirnas": "miRNAs",
    "rna": "RNA",
    "rnas": "RNAs",
}

def titlize(word, fname):
    if htable_strict.get(word.lower()):
        return htable_strict.get(word.lower())
    elif htable_upper.get(word.lower()):
        return word.upper()
    elif htable.get(word.lower()) and fname.index(word) != 0:
        return word.lower()
    else:
        return word.capitalize()

def generate_toc(dir, sub_dir):
    toc = ""
    for file in os.listdir(os.path.join("src", dir, sub_dir)):
        if file[0].isdigit():
            fname = [x for x in file[2:].replace('.md', '').split('_') if x]
            # remove empty strings in fname
            # make sure the first letter of each word is capitalized
            fname = ' '.join([titlize(word, fname) for word in fname])
            toc += f"* [{file[:2]}. {fname}]({file})\n"
        # else if the file is a file
        elif os.path.isfile(os.path.join("src", dir, sub_dir, file)):
            main_file = file
        else:
            continue
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
