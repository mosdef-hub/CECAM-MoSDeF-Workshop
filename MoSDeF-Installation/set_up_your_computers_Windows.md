# Conda install instructions for Windows

Below are set of instructions to help you effectively participate 
in this workshop. 

- [Set up Windows Subsystems for Linux](#set-up-windows-subsystems-for-linux)
- [How to open your terminal](#how-to-open-your-terminal)
- [Download this repository](#download-this-repository)
- [Set up Anaconda environments](#set-up-anaconda-environments)
- [Access an assignment or class in Jupyter](#access-an-assignment-or-class-in-jupyter)


## Set up Windows Subsystems for Linux 

For Windows machine, we recommend students to use the Windows Subsystems for Linux (WSL). If you are a Linux user, you can skip this section. The following link may provide additional information if the steps below give you trouble   https://docs.microsoft.com/en-us/windows/wsl/install-win10. 
**Note** Optionally, if you have Windows 11, you may have a linux command line already installed. Try running `wsl --install` and complete [these instructions](https://itsubuntu.com/run-linux-on-windows-11/). You can try to use that for the remaining setup, but be aware that you may run into unforseen issues if you choose not to use Ubuntu. Then continue to the next section.
1. Go to the cortana search bar in the bottom left of your screen and look for "Windows Powershell"
2. Open the powershell by right clicking the icon and selecting "Run as administrator"
3. Copy and paste this single line of code into the terminal that opens up. You may have to right click to paste text into your terminal. Control-V may work as well.  
      `dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart`
4. Restart your computer by selecting restart from the power options in the lower left menu of your windows bar.
5. Copy and paste this web address into the search bar of any web browser.  
    https://www.microsoft.com/en-us/p/ubuntu-2004-lts/9n6svws3rx71?rtc=1&activetab=pivot:overviewtab
6. Select the large blue "Get" button to open this app entitled Ubuntu in a Microsoft Store window. Select Get again in the windows store and then Install will appear. Hit the install button. Ubuntu will be the equivalent linux terminal you will use moving forwards.
7. In the same blue box, hit the Launch button that has now appeared. This will open Ubuntu for the first time on your device. It will open a black terminal window and will say “Installing, this may take a few minutes...” 
8. Enter a UNIX username once prompted. I would recommend using ""firstnamelastname"". No capitals or other symbols are allowed.
9. Enter a password for this username. I recommend using your computer’s login password.
10. Retype the password when prompted.
11. To open a new terminal in the future, just type Ubuntu into the cortana search bar and run as administrator. This will be the terminal you use to navigate directories and files in future steps.
12. In order to get into your C drive from this linux subsystem home directory, input `cd \mnt/c/Users`. Use `ls` to see which files and folders are available to you in your current directory.
13. You may need some practice to feel more comfortable working with the terminal. 
        We recommend you to work throught this [tutorial](https://swcarpentry.github.io/shell-novice/)
        to learn more about basic unix terminal commands. 


## How to open your terminal

#### Windows
0. For Windows users, make sure you have set up the Windows Subsystem for Linux (WSL) for your machine. If not, you can follow the instruction [here](#set-up-windows-subsystems-for-linux).
1. You can also open up a terminal window by searching for and opening the app Ubuntu.


## Set up Anaconda environments

Anaconda is a free, open-source distribution of the Python and R programming language for scientific computing, that aims to simplify package management and deployment. In this class, we will use Anaconda to manage our Python environment. 


#### Windows (Windows Subsystem for Linux)
0. For Windows users, make sure you have set up the Windows Subsystem for Linux (WSL) for your machine. If not, you can follow the instruction [here](#set-up windows-subsystems-for-linux).  
1. Go to this link https://docs.conda.io/en/latest/miniconda.html and select the **Linux** installer for Python 3.10 with 32-bit or 64-bit depends on your computer (use this link if you are unsure https://itsfoss.com/32-bit-64-bit-ubuntu/). 
   <\t> **Note**  Even if you are using Windows download for ***Linux***
2. Right click on the correct version and select “Copy link address”
3. Open your terminal and download the file with the copied link  
    `$ cd $HOME`  
    `$ curl -O <The link you just copied>`  
4. Once the downloads finish, type `$ ls` and make sure you can identify the downloaded file (should look something like “Miniconda3-***-Linux-x86_**.sh”) , then   
    `$ bash <The file you just download>`
5. Restart your terminal session and type `conda --version` to make sure the installation finishes. 

## Download this repository

This repository contains software and files neccessary for activities in this class, so we ask you to download this repository and put it in a location convienient for later reference. We recommend you put it in your home directory using the commands below:  
```bash
$ git clone https://github.com/mosdef-hub/CECAM-MoSDeF-Workshop.git
$ cd CECAM-MoSDeF-Workshop
$ conda env create -f environment.yml
$ conda activate mosdef_cecam
```

## Access an assignment or class in Jupyter

1. Type `jupyter notebook` into your terminal
2. The jupyter notebook will be open as a tab in your default browser  
If this doesn't occur automatically, look a the output from your jupyter notebook command. You should see a web link that looks something like `http://localhost:8888/?token=fd014533bc5780c313dfd1803838a89c6a90cdcd75d0cb2b` Copy that link by highlighting it and using control-c. Then, paste the link into the web browser of your choice. We recommend Google Chrome.
3. Click on folders to navigate through them, or on files to open them. Text files will open with a built in text editor. Jupyter notebook files have the extension `.ipynb`. These are the files where you execute python code, and where we'll run our tutorials from.

