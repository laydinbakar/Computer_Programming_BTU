## Lecture 1 07.10.2022
### Basic Terminal Commands on Ubuntu
Open a Terminal Window by
* pressing `Windows Key` and typing `Terminal`,
* pressing `ctrl+alt+t`,
* or clicking the Terminal Icon on the left dock.
### 1. `pwd`
`pwd` stands for `Pring Work Directory` in Linux. 
Terminal opens at the `home` directory by default in Ubuntu.
If you type `pwd` and press `Enter` you will see your `home` directory.
```
pwd
/home/la
```
in my case.

### 2. `ls`
We can list the files and folders in a directory using this command.
```
cd
pwd
/home/la
ls
```
Shows the files and folders located in your `/home/la` directory. 
You will see
```
Desktop/ install2.sh Pictures/ Templates/ Documents/ install.sh Public/ terminal_setting_link1/ Downloads/ Music/ snap/ Videos/
```
if you followed [this repository](https://github.com/laydinbakar/Computer_Programming_BTU/blob/main/00_ubuntu_installation.md) to install Ubuntu on your computer or if you use one of our lab computers.

`ls` also has some options with it. One of them is `ls -l` which prints the details of the files such as the size of a file in KB and the date that the file has been created.
```
ls -l
```
The other is `ls -la` and used for printing also the hidden files starting with `.` in your working directory.
```
ls -la
```

### 3. `cd`
`cd` stands for `Change Directory` in Linux.
We can go to a directory using the `cd` command as shown below.
```
cd Desktop
```
and check where we are working now by
```
pwd
```
shows that
```
/home/la/Desktop
```
This usage of `cd` lets we go to a directory relatively your working directory.
It can also be used as absolute path.
```
cd /home/la/Documents
pwd
/home/la/Documents
```

We can use `cd` alone in commandline to go to `home` directory.
```
cd
pwd
/home/la
```

`..` "two dots without space" is used to go an upper directory. Here we are in `/home/la`. Typing `..` we can go to `/home` directory.
```
cd ..
pwd
/home
```

`~` which is tilde is equal to `/home/la` in Linux Terminal. Insead of using 
```
cd /home/la/Desktop
```
we can use
```
cd ~/Desktop
```
to go to the `Desktop` directory from anywhere we are in.

* Examples with `cd`
Use the commands below and see what happens.
```
cd ~/..
pwd
cd la
ls
pwd
cd ../la/Desktop
pwd
cd ~/Documents
pwd
cd ~
pwd
ls
cd ../../home/~
pwd
```

