# Computer Programming
## Installation of Ubuntu
### Download of Ubuntu
To download Ubuntu, type Ubuntu Download into google search button or click [This Link](https://ubuntu.com/download/desktop).
After, you will see the download page. 
At this page, there is a button for download the Ubuntu 22.04.1 LTS. 

However, we will use the Ubuntu 20.04 LTS in our courses. 
In the version we will use, the first two numbers are important. So I mean Ubuntu 20.04. Please note that there are numbers 20 and 04 here. The number after these numbers is not important.
To download Ubuntu 20.04, click on the button that says "see our alternative downloads" as given below.
![Ubuntu_download_for_alternative_version.jpg](./figures/Ubuntu_download_for_alternative_version.jpg)

Download the Ubuntu 20.04 iso file by clicking the button as shown in the figure below. (Download via BitTorrent as the file size is too large.) 
![002_alternative_version_button.jpg](./figures/002_alternative_version_button.jpg)

### Download of Rufus
Rufus is a tool for Windows that lets you create boot devices from external storage units, like USB flash drives and SD cards. Its versatility lets you format a new drive, as well as install Linux, Windows, and even FreeDOS disk images, which, in fact, comes built into the application itself.

We need to write the Ubuntu iso file to a flash drive. So we will create an image file. For this we need to download the Rufus.
Type "Download Rufus" in the google search button or click [This Link](https://rufus.ie/en/) to download Rufus.
After, download Rufus to your computer as shown in the image below.
![003_Rufus_Download.jpg](./figures/003_Rufus_Download.jpg)

Run Rufus and write your Ubuntu 20.04 iso file to your flash memory as in the image below. (Make sure your flash memory is at least 15GB.)
![004_Rufus_iso_image.jpg](./figures/004_Rufus_iso_image.jpg)
![005_Rufus_iso_image.jpg](./figures/005_Rufus_iso_image.jpg)

### Installation
After using Rufus to make an ISO image into a USB drive, you can restart your computer and press your boot key.
In the boot screen of your computer, you will see a similar page as given below.  (If you don't know which key (F12, F11 etc.) is used on your keyboard for "boot manager", search it on google with your computer model.)
![01_select_usb_in_boot_menu.JPG](./figures/01_select_usb_in_boot_menu.JPG)

From the boot menu that appears, select the USB driver where you writed the iso file by the rufus.
After selecting the USB drive, you will see a screen similar to the one below. 
![02_select_install_ubuntu.JPG](./figures/02_select_install_ubuntu.JPG)
Continue here by selecting the English language option and clicking Install Ubuntu button.

Then choose your keyboard layout as in the image below. (Choose English if you have an English keyboard layout.)
![03_choose_your_keyboard_layout.JPG](./figures/03_choose_your_keyboard_layout.JPG)

Then you will see a screen like the below. Continue to the installation by clicking the "Normal installation" and Download updates while installing ubuntu" options as in the image.
![04_click_to_continue.JPG](./figures/04_click_to_continue.JPG)

On the next step, as shown the below, click "Install Ubuntu alongside Windows Boot Manager" as the installation type and continue.
![05_install_ubuntu_alongside_windows.JPG](./figures/05_install_ubuntu_alongside_windows.JPG)

In the next step, you will see a screen like the one below.
![06_allocate_30gb_for_ubuntu.JPG](./figures/06_allocate_30gb_for_ubuntu.JPG)
Allocate at least 30 GB of space which we will need in the lessons for Ubuntu. (You can boost this area further if you prefer.)
To allocate disk space, pull the bidirectional arrow to the right or left.

In the next step, you will see the location selection section as in the image below. Select your location by typing Turkey or Istanbul here.
![07_choose_turkiye.JPG](./figures/07_choose_turkiye.JPG)

In the next step, you will see a screen with information such as username, password and computer name as below.
![08_fill_the_form_weakpassword.JPG](./figures/08_fill_the_form_weakpassword.JPG)
While we are working on Ubuntu, we will have to use passwords many times. Because most of the operations we will do will require a password in the terminal. So set a password that is both strong and fast to type. (Please be careful not to use Turkish characters in all your steps.)

Then wait for some time the installation to complete as in the picture below.
![09_wait_for_some_time.JPG](./figures/09_wait_for_some_time.JPG)

When the installation is complete, you will see a screen like the picture below. Please do not remove the USB drive during this time and click the restart button. 
![10_restart.JPG](./figures/10_restart.JPG)

After restart, you will then see a screen like the image below.
![11_remove_usb_and_enter.JPG](./figures/11_remove_usb_and_enter.JPG)
Remove the USB driver and then press the enter. 
After this step, wait for the computer to start.

When the computer starts, you will see a screen like the image below. 
![12_choose_ubuntu_or_windows.JPG](./figures/12_choose_ubuntu_or_windows.JPG)
Here, select the "Ubuntu" partition to boot your computer with Ubuntu, or the partition starting with "Windows Boot Manager" to boot your computer with Windows. 

### Updating and Installing Required Applications

After you complete the installation cleanly, watch the video below. 

![01_ubuntu_installation-2022-09-28_12.27.29.mp4](./videos/01_ubuntu_installation-2022-09-28_12.27.29.mp4)

This video includes some other system updates and installation of useful applications such as web browser in the first stage.

Then watch the second video below.

![02_terminal_setting-2022-09-28_12.36.40.mp4](./videos/02_terminal_setting-2022-09-28_12.36.40.mp4)

This video contains the programs we will use in the lessons and some terminal settings. The folders and files in the video will be shared with you via the google drive.
