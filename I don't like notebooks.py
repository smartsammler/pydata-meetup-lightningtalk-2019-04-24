# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.3'
#       jupytext_version: 0.8.5
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.6.8
# ---

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # JupyterCon 2018: [Joel Grus](https://twitter.com/@joelgrus), [I don't like Notebooks](https://docs.google.com/presentation/d/1n2RlMdmv1p25Xy5thJUhkKGvjtV-dkAIsUXP-AL4ffI/edit#slide=id.g362da58057_0_1)

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# Key points of criticism:
#
# * Hidden state
#  * Difficult for beginners
# * Bad habits
#  * No testing, linting, auto-formatting,
#  * Not importable
#  * No clean design
# * No classes, etc.
# * Linked state (in JupyterLab)
# * No reproducibility 
# * Copy paste notebook content
# * Aborts also at expected errors

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# I would add:
# * Git support (JSON: Nah)
# * Extensions in environments like
#
# ![XKCD 1987](https://imgs.xkcd.com/comics/python_environment.png)

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## Hidden state

# + {"slideshow": {"slide_type": "fragment"}}
x = 2

# + {"slideshow": {"slide_type": "fragment"}}
print(x)

# + {"slideshow": {"slide_type": "fragment"}}
x = 3

# + {"slideshow": {"slide_type": "notes"}, "cell_type": "markdown"}
# The execution order is shown in brackets, but need not to be in from top to bottom.

# + {"slideshow": {"slide_type": "subslide"}}
x = 5
print(x)

# + {"slideshow": {"slide_type": "notes"}, "cell_type": "markdown"}
# Even more subtle: edit cells after executing them (here: changed 4 to 5 after execution)

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ### Learned from that talk:

# + {"slideshow": {"slide_type": "fragment"}}
# %history

# + {"slideshow": {"slide_type": "fragment"}, "cell_type": "markdown"}
# But it works only for the first case and is a unhandy solution.
#
# **Do you know of good solutions?**

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## No reproducibility

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# * No versioning without hacks like

# + {"slideshow": {"slide_type": "fragment"}}
import sys
print(f"Python {sys.version_info}")
print(f"Interpreter {sys.executable}")
print("Installed packages: ")
!{sys.executable} -m pip freeze # > requirements.txt
# !{sys.executable} -m pip install -r requirements.txt

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## Classes and many cells

# + {"slideshow": {"slide_type": "slide"}}
import jdc

class TestClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

# + {"slideshow": {"slide_type": "fragment"}}
# %%add_to TestClass
def __call__(self, c):
    print(self.a, self.b, c)

# + {"slideshow": {"slide_type": "fragment"}}
a = TestClass(1, 2)
a(3)
# -

class TestClass(TestClass):
    def __repr__(self):
        return f"a: {self.a}\nb: {self.b}"

a = TestClass(1, 2)
a

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## Things I like Notebooks for

# + {"slideshow": {"slide_type": "fragment"}, "cell_type": "markdown"}
# * Presentations (Nice slides from non-Apple-Academics)
# * Tutorials (especially with Binder)
#  * Easily have the same environment for all, but more powerful than Notepad (no vim-Plugin or PyCharm-config issues)
# * Taking notes and actively "reading" papers (incl. calculations)
# * Share Calculations with colleagues (HTML-export)
# * Showing examples and blogging
# * Interactively designing a plot (JupyterLab) or exploring functions (with widgets)

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## Extensions dealing with those problems
#
# * Git
#  * Jupyterlab-git
#  * nbdime
#  
# Talk at PyConDE 2018: [Prototyping To Tested Code - Christopher Prohm](https://www.youtube.com/watch?v=8fg7AkvG-Oc)

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# * [Jupytext](https://github.com/mwouts/jupytext/blob/master/README.md) saves Notebooks as ipynb and as Python scripts including all cells, excluding cell states.
#
# The article from the author on [medium](https://towardsdatascience.com/introducing-jupytext-9234fdff6c57?gi=6b861bbe5cad)
#
# * Also possible to run in an IDE
# * Also works for JupyerLab

# + {"slideshow": {"slide_type": "fragment"}, "cell_type": "markdown"}
# Edit your `jupyter_notebook_config.py`
# ```
# c.NotebookApp.contents_manager_class = "jupytext.TextFileContentsManager"
# ```

# + {"slideshow": {"slide_type": "fragment"}, "cell_type": "markdown"}
# Edit the Notebook in the Editor and add imadeately before the `kernelspec`
# ```
# "jupytext" : {"formats": "ipynb,py"}
# ```

# + {"slideshow": {"slide_type": "fragment"}}
# %autosave 0

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # Thank you.
#
# *We should not show Joel Grus [Prezi](https://prezi.com/), so he can complain about [Reveal.js](https://revealjs.com) first* :)
