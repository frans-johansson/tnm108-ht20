# Introduction to Python for Machine Learning
This directory holds a Jupyter Notebook *Introduction.ipynb* which runs through the basics of using the common data science libraries NumPy, Pandas and Matplotlib for the purposes of the course TNM108, Machine Learning for Social Media. This notebook allows the reader to play around with the code themselves and see results more or less immediately!

## Prerequisites
You will need to install the following packages using the `pip install` command

- `notebook`
- `jupyter`

## Starting the notebook
If you're using the code editor *Visual Studio Code*, you should just be able to open the .ipynb file directly and have all the notebook functionalities built in to the code editor (you might have to install some extensions and click your way through a few pop ups, but then you should be ready to go).

However, if you don't want to install a new code editor, you are able to run the notebook in your browser by pulling up a terminal (preferrably in the same directory as the .ipynb file) and run one of the following commands: `jupyter notebook` or `jupyter notebook Introduction.ipynb` (or whatever filename your notebook has). Running the first command will open a browser window where you are able to select or create new notebooks in the directory you ran the command frmo, the second command will simply open the specified notebook immediately.

## Using the noteboook

> Short disclaimer: These instructions and commands work in Visual Studio Code, but might not be the same when running the notebooks through the browser interface.

You can run the currently active cell with `ctrl+enter`. Using `ctrl+shift+enter` will run the cell and highlight the next cell (allowing you to chain together cell executions). Commenting out a line can be done with `ctrl+*`, which annoyingly seems to be a different setting to the normal Visual Studio Code keybinding.

The top bar of the notebook has a few useful buttons for running all cells, running all cells above or below the current cells and restarting the kernel (if something goes south, this button will come to your rescue). You will also find buttons for stopping execution of a cell, e.g. if you accidentally created some sort of infinite loop, without restarting the Python kernel. You can also select which Python environment to use (if you have multiple versions of Python installed for example) or specify a virtual environment to use instead (if you happen to be using something like *Anaconda* or *pipenv*).