---
title: Writing Python modules and scripts (the right way)
author: Jacan Chaplais
date: Wednesday, 15th February 2023
...

- Python is interpreted language
- Can write in lots of ways: interactive, notebook, source files
- Saving Python code in files to re-use best for sharing work
- Two types of Python file: modules and scripts
- Script is an executable file which takes input and produces output
- `cat`, `ls`, ImageMagick's `convert` command are all command line executables
- all compiled though, where does interpreted languages like Python come in?
- can use `python` command before Python filename, behaves just like exe
    - can also add shebang, _eg._ `#!/usr/bin/bash` or `#!/usr/bin/env python3`
    - if `chmod +x my-program` becomes executable `my-program`

# Python's killer feature

- Python's killer feature is that it's very _permissive_
- Lets you do things in many ways, even if not best practice
- Much easier to get things done as a beginner
- Python has lots of conventions which do give more functionality, though!
- 


# ifmain idiom

contents of `who_are_you.py`:

```python3
print(f"__name__: {__name__}")
```

if run from a terminal:

```bash
$ python who_are_you.py
__name__: __main__
```

whereas, if imported during interactive session

```
>>> import who_are_you
__name__: who_are_you

```

This tells Python you are using the file as a module!

Hence, we can define script-only behaviour by using:

```python3
def main():
    print("Hello world")


if __name__ == "__main__":
    main()
```

- the culture motivation:
    - indicates to other programmers that the file is a script, and can run it
    - without this, many programmers will assume it's a module to be imported
    - many editors will highlight the idiom especially
- the practical motivation:
    - without `if` block, importing the code will run it!
    - without `main()` function, variables will be in global scope
        - include examples of this, see mcoding ~ 4 minutes in
        - multiprocessing with unpickle
    - can use it as an entry-point to run the script from another file
