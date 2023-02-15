# 1. Writing Python modules and scripts the right way

Welcome to the first session of Coding Club!

In this session, we will be looking at how to clean up your Python code into
scripts and modules. This will make your work easy to use and distribute, both
for yourself and others!

[The slides are available here.](https://jacanchaplais.github.io/python-modules-and-scripts)

Fire up a GitHub Codespace from this repository to test out the examples in
realtime. You can hit the + sign in the top right hand corner of GitHub, and
select "New Codespace", then search for this repository, under
`jacanchaplais/python-modules-and-scripts`. This will give you a virtual
machine in the cloud which you can use to follow along with. Code examples are
stored under `src/`.

## Bonus exercises

Starting from the `src/6_installable/wavey/` directory:

1. Add a new wave function to `__init__.py` (_eg._ `tan_wave()`)
    - Be sure to document the function
2. Edit `generate()` function in `__main__.py` options:
    1. Add an option to select which wave form to use (if you did ex 1)
        - Hint: the relevant section of [`click`'s docs](https://click.palletsprojects.com/en/8.1.x/options/#choice-options)
    2. Edit `--noise` option so that it takes a numerical value, to allow the
       scale of the noise to be set in the CLI
    3. Add an option to select the interval of angles data is created for
3. Add option to `plot()` function to change the line style of the figure
