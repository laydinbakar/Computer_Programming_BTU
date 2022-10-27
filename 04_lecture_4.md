# Lecture 4 (28.10.2022)
You can watch the video lectures for
* [Python]().

## Introduction to Python Programming Language
### Basic arithmatic operations
|Sign |Name |Ex |Results |
|------|------|------|------|
|`+`| Addition| 7+3 |10|
|`-`| Substraction| 7-3|4|
|`\*`| Multiplication|7\*3|21|
|`/`| Division|7/3|2.3333|
|`%`| Modulo|7%3|1|
|`**`|Exponentiation|7\*\*3|343|

### Python in the commandline
Python can be used in the commandline by typing `python` (or `python3` for 3rd version of Python).

You can try the arithmetic operations above in the commandline Python and press `ctrl+d` or type `exit()` to exit.

![](./figures/04.01.commandline.png)

To write the output of the commandline Python into a file use `python3 > file` command.

![](./figures/04.02.commandline_tee.png)

Or you can both see the results in commandline Python and write into a file by `python3 | tee file`. Try it.

### Python in Vim
To see clearer you can start using Screen here `screen -S lecture4`.

Open a file with `.py` extension `vi firstPythonCode.py`. 

### `print` in Python
Use `print("")` command to print out.

![](./figures/04.03.print.png)
 
### `input` in Python
You can ask user to type something when it runs the code.

![](./figures/04.04.input.png)

### Basic data types
Integer, floating-point numbers, strings and boolean are the four data types in python.

See for integers and floats for example:

![](./figures/04.05.data_types1.png)

and for strings and booleans:

![](./figures/04.06.data_types2.png)

### Variables

We can define variables as follows:

![](./figures/04.07.variables1.png)

We can also ask variables to the user with `input()`. But the input is in string type as default. If we use it as integer, float or boolean we should express it.

![](./figures/04.08.variables2.png)

## Lists in Python Programming Languange
### Makiing lists
You can make lists in Python as follows:

![](./figures/04.09.lists.png)

### Use the lists
Read an item in a list and make operations.

![](./figures/04.10.lists_items.png)

Read multiple vaules from lists.

![](./figures/04.11.lists_items2.png)

You can manipulate items of lists.

![](./figures/04.12.lists_manipulate.png)

Find some useful list methods below.

![](./figures/04.13.lists_methods.png)

### String methods

Similar methods are also available for strings.

![](./figures/04.14.strings_methods.png)

# Upload your codes on GitLab
You signed up GitLab last week. Open that repository on your web browser and copy its link.

![](./figures/04.15.git_clone.png)

Open the terminal and use `git clone` command to download the repository onto your computer.

![](./figures/04.16.git_clone2.png)

`cd` to `ComputerProgramming2022` folder and make some changes as follows.
* Make `Lecture4` and `MidtermExam` folders. Be careful about the names and capitalization. Do exactly the same as `Lecture4` and `MidtermExam`.
* Move all the scripts you write from `../` to `Lecture4`.
* Empty folders cannot be uploaded onto GitLab repositories. Use touch to add `README.md` files in each folders.
* Check if you do all correctly by `ls *`.

![](./figures/04.17.git_files.png)

Then, add all the Python scripts you have written today onto your GitLab repository. Use 
* `git add .`, 
* `git commit -m "Add files"` and 
* `git push origin main` commands, respectively.

![](./figures/04.18.git_push.png)

At the end, you can check your GitLab repository from your browser.

![](./figures/04.19.git_browser.png)


