---
title: Python modules and scripts
author: Jacan Chaplais
date: Wednesday, 15th February 2023
...

## Python is a scripting language {
data-background-image="img/bg.jpg"
data-background-opacity=0.3
}

- High level interpreted language (similar to Lua, BASH, _etc._)
- Compiled code provides tools _eg._ `cat`, `ls`, `mv`, _etc._
- Typed into command-line, act as **entry-points** to software
- Scripts are the entry-points to interpreted code

## Rookie workflow {
data-background-image="img/bg.jpg"
data-background-opacity=0.3
}


- Inexperienced folks often write a bunch of scripts, _eg._ `python mycode.py`
- Useful to share code between files for common behaviour => `import mycode`
- If file acts a both script and **module**, can cause **side effects**

## ``if main`` guard {
data-background-image="img/bg.jpg"
data-background-opacity=0.2
}


- Explicitly define scripts by checking how it's called

:::::: {.columns style="display: flex; align-items: center;"}
:::: {.column width="45%"}
```python
def main():
    """Script code here."""

if __name__ == "__main__":
    main()
```
::::
:::: {.column width="52%"}
- Only executes if script
- `main()` prevents globals
- No more side-effects!
::::
::::::

- All Python scripts should use this idiom!
- Can set most text editors load this from a template

## Command-line interfaces {
data-background-image="img/bg.jpg"
data-background-opacity=0.2
}


- Scripts are annoying if need to jump into source
- Add CLI to pass variable params, and get help text
- De-facto library in Python is [`click`](https://click.palletsprojects.com/),
  very powerful!


```python
import click

@click.command()
@click.argument("name", type=click.STRING)
def main(name):
    """Greet NAME via the command line."""
    click.echo(name)

if __name__ == "__main__":
    main()
```

## Directories as packages {
data-background-image="img/bg.jpg"
data-background-opacity=0.3
}


- **Packages** are Python's builtin directory system
- Named folders with a default module and script file
    - module: `pkgname/__init__.py`
    - script: `pkgname/__main__.py`
- `import pkgname` get contents of module
- `python -m pkgname` runs script from terminal

## Install globally {
data-background-image="img/bg.jpg"
data-background-opacity=0.2
}


- Can only use package from parent directory
- Adding `pyproject.toml` enables install with `pip`
- Makes modules and scripts available everywhere!

```toml
[project]
name = "pkgname"
version = "0.0.1"
dependencies = [
    "click",
]
[project.scripts]
shazam = "pkgname.__main__:main"
```

## It's play time {
data-background-image="img/bg.jpg"
data-background-opacity=0.3
}


If you haven't already, fire up your text editors and have a go making some
packages! Flag me down, or ask the people nearby if you are having trouble.
There are some optional exercises for you to try on the GitHub README.

Also anybody who wants to give a talk would be a huge support for Coding Club!
It can be interactive like this, or a much simpler slideshow affair.

Thanks, everyone!
