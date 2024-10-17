#!/usr/bin/env python3

# Iterate through all directories in src/, in each subdirectory, find the only file that does not start with number, use it as the file to insert TOC into
# for all other files that start with number, use their file name as the link text, and insert them into the TOC file, in the order of their file name
# the first underscore in the file name is replaced with ". ", and the rest of the underscores are replaced with spaces

import sys
import os
import re
import pathlib


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


def generate_toc(dir: pathlib.Path, toc_file: str, chapter_files: list[str]) -> None:
    toc = ""
    for file in chapter_files:
        fname = [x for x in file[2:].replace(".md", "").split("_") if x]
        # remove empty strings in fname
        # make sure the first letter of each word is capitalized
        fname = " ".join([titlize(word, fname) for word in fname])
        toc += f"* [{file[:2]}. {fname}]({file})\n"
    # do nothing if main_file is not found (i.e. no file needs TOC)
    main_file_path = dir / toc_file
    with open(main_file_path, "r") as f:
        content = f.read()
    # get the current TOC
    curr_toc = re.search(r"<!-- toc -->\n(.*)<!-- toc -->", content, flags=re.DOTALL)
    if curr_toc:
        curr_toc = curr_toc.group(1)
    if curr_toc == toc:
        return
    else:
        content = re.sub(
            r"<!-- toc -->.*<!-- toc -->",
            f"<!-- toc -->\n{toc}<!-- toc -->",
            content,
            flags=re.DOTALL,
        )
        with open(main_file_path, "w") as f:
            f.write(content)


IGNORES = [
    "README.md",
    "SUMMARY.md",
]


def is_chapter(file: str) -> bool:
    return file[0].isdigit() and file not in IGNORES and file.endswith(".md")


def is_toc(file: str) -> bool:
    return file not in IGNORES and file.endswith(".md")


def main():
    PROJECT_ROOT = pathlib.Path(__file__).parent.parent
    SRC_DIR = PROJECT_ROOT / "src"

    to_process: list[pathlib.Path] = []
    to_process.append(SRC_DIR)
    while len(to_process) > 0:
        curr = to_process.pop()
        paths = os.listdir(curr)
        dirs = [curr / p for p in paths if (curr / p).is_dir()]
        for d in dirs:
            to_process.append(curr / d)
        files = [p for p in paths if (curr / p).is_file()]
        chapter_files: list[str] = []
        toc_file: str | None = None

        for f in files:
            if is_chapter(f):
                chapter_files.append(f)
            elif is_toc(f):
                toc_file = f
        if len(chapter_files) == 0 or toc_file is None:
            continue
        generate_toc(curr, toc_file, chapter_files)


if __name__ == "__main__":
    if len(sys.argv) > 1:  # we check if we received any argument
        if sys.argv[1] == "supports":
            # then we are good to return an exit status code of 0, since the other argument will just be the renderer's name
            sys.exit(0)
    else:
        main()
        sys.exit(0)
