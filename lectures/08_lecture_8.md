# Lecture 8 (25.11.2022)
Clone your GitLab repository onto the computer you use before starting these examples.


## Example 1
1. Create a folder as `Lecture8` in `ComputerProgramming2022` and change the working directory into `Lecture8`.
1. Write a shell script (`shell1.sh`) making
  1. a directory so called `shell1` and change directory into it,
  1. 3 directories with the names 1 to 3 in `shell1`,
  1. 11 directories with the names 1 to 11 but filled with zeros such as (0005 and 0010) in each 3 directories,
  1. 101 text files in each 11 directories with the names 1 to 101, but filled with zeros as you do above.
  1. Write the relative path to your working directory (`Lecture8`) in each file as `This is $n$th file in "RELATIVE_PATH"`. Here $n$ is the file number from 1 to 101.
3. Make the shell script executable.

## Example 2
1. Work in `Lecture8` folder and write a shell script (`shell2.sh`) making
  1. a directory so called `shell2` and change directory into it,
  1. 3 directories with the names 1 to 3 in `shell2`,
  1. 11 directories, in each 3 directories, with the names 1 to 21, skipping the even numbers. File names should be constructed by 5 characters filled with zeros,
  1. 20 text files in each 11 directories with the names 20 to 115, skipping 5, but filled with zeros as you do above,
  1. Write the relative path to your working directory (`Lecture8`) in each file as `This is $n$th file in "RELATIVE_PATH"`. Here $n$ is the file number from 20 to 40.
2. Create another directory as `shell3` in `Lecture8` and link all the files in `~/ComputerProgramming2022/Lecture8/shell2/2/19/` to `shell3`.
3. Make the shell script executable.

## Example 3
1. Work in `Lecture8` folder and write a shell script (`shell3.sh`),
  1. removing all the odd number files and folders in `shell1`. In this shell scipt, `if` statement usage is compulsory.
2. Make the shell script executable.

## Example 4
1. Create a folder as `python_scripts` in `Lecture8` and work on it.
1. Write a Python script as follows:
  1. Use `input()` method to read a file name from the commandline.
  1. Create a $3\times1000$ array, multiply each column with the column number and $\pi$ number.
  1. Write it to a text file and a binary file. 
2. Save and exit from the Python script and check the file sizes. 
3. Open a text file as `sizes.txt` and write the file names and sizes manually using Vim.

## Example 5
1. Write a Python script in `python_scripts` folder as follows:
  1. Use argument parser package 
    1. to read an input file name from the commandline,
    1. to read an output file name from the commandline,
    1. to read two folder names from the commandline.
  1. Make two directories as `odd` and `even`.
  1. Read the binary file you write in `Example 4` as input file you read in `1.1.1`.
  1. Remove the lines with the odd line numbers and write output (with only the even lines) into the folder `even` as a binary file.
  1. Remove the lines with the even line numbers and write output (with only the odd lines) into the folder `odd` as a binary file. 
2. Make the Python file executable.

## Example 6
1. Write a Python script in `python_scripts` folder as follows:
  1. Use argument parser package 
    1. to read a name from the commandline.
  1. Create 4 different lists as `names`, `ages`, `heights`, and `weights` each includes 5 persons' information.
  1. Convert these lists into arrays and merge into $4\times5$ array.
  1. Use this array and print information for the person of the name given in the commandline by the argument parser.
2. Write the code, save and exit, make executable and run.
3. Write the output into a file `info.txt` in the commandline.


