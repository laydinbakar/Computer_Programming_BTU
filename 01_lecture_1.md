# THIS PAGE HAS NOT BEEN COMPLETED YET


# Lecture 1 (07.10.2022)
### Basic Terminal Commands on Ubuntu
Open a Terminal Window by
* pressing `Windows Key` and typing `Terminal`,
* pressing `ctrl+alt+t`,
* or clicking the Terminal Icon on the left dock.
### 1. `pwd`
`pwd` stands for `Print Work Directory` in Linux. 
Terminal opens at the `home` directory by default in Ubuntu.
If you type `pwd` and press `Enter` you will see your `home` directory.

![pwd](./figures/01.01.pwd.png)

in my case.

### 2. `ls`
We can list the files and folders in a directory using this command.

![pwd](./figures/01.02.ls.png)

Shows the files and folders located in your `/home/la` directory.
You should see the same folders in your `home` directory
if you followed [this repository](https://github.com/laydinbakar/Computer_Programming_BTU/blob/main/00_ubuntu_installation.md) to install Ubuntu on your computer or if you use one of our lab computers.

`ls` also has some options with it. One of them is `ls -l` which prints the details of the files such as the size of a file in KB and the date that the file has been created.
![pwd](./figures/01.03.ls-l.png)

The other is `ls -la` and used for printing also the hidden files starting with `.` in your working directory.
![pwd](./figures/01.04.ls-la.png)

### 3. `cd`
`cd` stands for `Change Directory` in Linux.
We can go to a directory using the `cd` command as shown below.
![pwd](./figures/01.05.cd.png)

This usage of `cd` lets we go to a directory relatively your working directory.
It can also be used as absolute path.
![pwd](./figures/01.06.cd2.png)

We can use `cd` alone in commandline to go to `home` directory.
![pwd](./figures/01.07.cd3.png)

`..` "two dots without space" is used to go an upper directory. Here we are in `/home/la`. Typing `..` we can go to `/home` directory.
![pwd](./figures/01.08.cd4.png)

`~` which is tilde is equal to `/home/la` in Linux Terminal. 
![pwd](./figures/01.09.cd5.png)

### 4. `mkdir`
`mkdir` is the acronym of `Make Directory`.
We can make directories using this command.
![pwd](./figures/01.10.mkdir.png)

If we use space between two word when we make directories using `mkdir` it makes two different folders.
![pwd](./figures/01.11.mkdir2.png)

So, if we want to make a directory so called "Lecture Notes" we should type
![pwd](./figures/01.13.mkdir4.png)

but this way is usually not preferred by Linux users. Instead we use `Lecture_Notes` or `LectureNotes`. For the differences you can read [here](https://wiki.c2.com/?UnderscoreVersusCapitalAndLowerCaseVariableNaming).
![pwd](./figures/01.13.mkdir4.png)

If we need to make multiple directories in such as `LectureNotes/Lecture1` we can use
However, if any of the non-existing directories included in our command, we get an error.
To get rid of this error we should use `-p` option as follows.
![pwd](./figures/01.12.mkdir3.png)

This will both make the `LectureNotes` directory and `Lecture1` in it.

### 5. `touch`
This is a command creating files in Linux.
```
touch LectureNotes/Lecture1/file.txt
touch LectureNotes/Lecture2/Slides/README.md
mkdir LectureNotes/Lecture1/Python
touch LectureNotes/Lecture1/Python/solve.py
```

### 6. `rm`
`rm` removes files and folders in Linux.
```
ls LectureNotes/Lecture1
file.txt
rm LectureNotes/Lecture1/file.txt
```
removes the `file.txt`. However, we get an error when we try to remove a folder by `rm`
```
rm LectureNotes/Lecture1/Python
rm: cannot remove 'LectureNotes/Lecture2/Slides': Is a directory
```
To remove a directory we need to use `-r` option in this command.
```
rm -r LectureNotes/Lecture1/Python
ls LectureNotes/Lecture1
<empty>
```
`-r` option is usually used with `-f` so as not to get error for nonexisting files and arguments.
```
rm -r LectureNotes/Lecture1
rm: cannot remove 'LectureNotes/Lecture1': No such file or directory
rm -rf LectureNotes
```

### 7. `cp`
`cp` is acronym of `Copy` in Linux Terminal. A `-r` option is used with `cp` for similar reasons.
```
cp -r LectureNotes LectureNotesBck
cp LectureNotes/Lecture2/Slides/README.md .
```



### 5. `ln`
`ln` stands for `Link`. We can use this to link a file or folder to somewhere else.
```

