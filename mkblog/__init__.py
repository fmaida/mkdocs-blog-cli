import datetime
import sys
import os
import subprocess


def search_config_file(attempts=7):
    curpath = os.getcwd()
    found = None
    attempt = 1
    while not found and attempt < attempts:
        for root, dirs, files in os.walk(curpath):
            if "mkdocs.yml" in files:
                found = root
                break
        if not found:
            curpath = os.path.dirname(curpath)
            attempt += 1
    return found

def main():
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == "new":
            root = search_config_file()
            if root:
                title = "_".join(sys.argv[2:]).lower()
                if not ".md" in title:
                    title = title + ".md"
                today = datetime.datetime.now().date()
                path = os.path.join(root, "docs")
                if not os.path.isdir(path):
                    os.mkdir(path)
                path = os.path.join(path, "blog")
                if not os.path.isdir(path):
                    os.mkdir(path)
                path = os.path.join(path, str(today.year))
                if not os.path.isdir(path):
                    os.mkdir(path)
                path = os.path.join(path, str(today.month).zfill(2))
                if not os.path.isdir(path):
                    os.mkdir(path)
                path = os.path.join(path, str(today.day).zfill(2))
                if not os.path.isdir(path):
                    os.mkdir(path)
                path = os.path.join(path, title)
                if not os.path.isfile(path):
                    with open(path, "w") as f:
                        f.write("---\n")
                        f.write("title: {}\n".format(" ".join(sys.argv[2:])))
                        f.write("---\n")
                        f.write("\n")
                        f.write("# {}\n".format(" ".join(sys.argv[2:])))
                        f.write("\n")
                        f.write("\n")
                subprocess.call(["nvim", path])

