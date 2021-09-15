# Pathlib - Python 3.4+

The pathlib module provides a way to interact with the file system in a much more convenient way than dealing with `os.path` or the `glob` module.  
The pathlib module makes everything simpler.

More information about the pathlib module:
 - https://docs.python.org/3/library/pathlib.html
 - https://realpython.com/python-pathlib/
 - https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python

List directory tree structure in Python?
We usually prefer to just use GNU tree, but we don't always have tree on every system, and sometimes Python 3 is available.

`tree`'s output looks like this:

```bash
$ tree
.
├── package
│   ├── __init__.py
│   ├── __main__.py
│   ├── subpackage
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   └── module.py
│   └── subpackage2
│       ├── __init__.py
│       ├── __main__.py
│       └── module2.py
└── package2
    └── __init__.py

4 directories, 9 files

```

Tree in Python
To begin with, let's use an example that:
 - uses the Python 3 Path object
 - uses the yield and yield from expressions (that create a generator function)

```python
 
from pathlib import Path

# prefix components:
space =  '    '
branch = '│   '
# pointers:
tee =    '├── '
last =   '└── '


def tree(dir_path: Path, prefix: str=''):
    """A recursive generator, given a directory Path object
    will yield a visual tree structure line by line
    with each line prefixed by the same characters
    """
    contents = list(dir_path.iterdir())
    # contents each get pointers that are ├── with a final └── :
    pointers = [tee] * (len(contents) - 1) + [last]
    for pointer, path in zip(pointers, contents):
        yield prefix + pointer + path.name
        if path.is_dir(): # extend the prefix and recurse:
            extension = branch if pointer == tee else space
            # i.e. space because last, └── , above so no more |
            yield from tree(path, prefix=prefix+extension)

 ```
