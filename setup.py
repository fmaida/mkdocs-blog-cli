from distutils.core import setup

# Read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.rst"), encoding='utf-8') as f:
    read_me = f.read()

setup(
    name="mkdocs-blog-cli",
    version="0.1",
    author="Francesco Maida",
    author_email="francesco.maida@gmail.com",
    packages=["mkblog"],
    url='https://github.com/fmaida/mkdocs-blog-cli',
    license="MIT",
    description="Command-line interface for my plugin 'mkdocs-blog-plugin'",
    long_description_content_type="text/x-rst",
    long_description=read_me,
    install_requires=[],

    entry_points={
        "console_scripts": [
            "mkblog = mkblog:main",
        ]
    }
)

