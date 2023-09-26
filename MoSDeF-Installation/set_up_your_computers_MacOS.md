# Conda install instructions for MacOS or Linux

Below are set of instructions to help you effectively participate 
in this camp: Provided is an introduction to computation and simulations.

- [How to open your terminal](#how-to-open-your-terminal)
- [Set up Anaconda Environments](#set-up-anaconda-environments)
- [Download this repository](#download-this-repository)
- [Access an jupyter notebook](#access-jupyter-notebook)


## How to open your terminal

#### MacOS- open terminal
You can open the terminal application on MacOS by either:
1. Use Spotlight search: press “Command + Space” and search for “terminal”
2. Open Launchpad and look for the “Terminal” app

#### Linux- open terminal
1. `Ctrl + Alt + T`

## Set up Anaconda Environments

Anaconda is a free, open-source distribution of the Python and R programming language for scientific computing, that aims to simplify package management and deployment. In this workshop, we will use Anaconda to manage our Python environment. Below are short instructions to set up the Anaconda software for (Mac)[#macos] or (Linux)[#linux].

#### MacOS  
1. Download miniconda from:   
    https://docs.conda.io/en/latest/miniconda.html   
    (Select the correct installer for macos **Python 3.10, 64-bit pkg**)
2. Install miniconda from the downloaded file  
3. Restart terminal. You should see `(base) YOURUSERNAME $` at your input line. If the `(base)` is not there, additional detals can be found [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html)


#### Linux 
1. Download miniconda from:   
    https://docs.conda.io/en/latest/miniconda.html   
    (Select the correct installer for linux **Python 3.10, 64-bit pkg**)
2. Install miniconda from the downloaded file  
3. Restart terminal. You should see `(base) YOURUSERNAME $` at your input line. If the `(base)` is not there, additional detals can be found [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html)

## Download this repository

This repository contains software and files neccessary for activities in this class, so we ask you to download this repository and put it in a location convienient for later reference. We recommend you put it in your home directory using the commands below:  
```bash
$ git clone https://github.com/mosdef-hub/CECAM-MoSDeF-Workshop.git
$ cd CECAM-MoSDeF-Workshop
$ conda env create -f environment.yml
```


## Access Jupyter Notebook
```bash
$ conda activate cecam_mosdef
$ jupyter notebook
```

The jupyter notebook will be open as one tab in your default browser  
If this doesn't occur automatically, look a the output from your jupyter notebook command. You should see a web link that looks something like `http://localhost:8888/?token=fd014533bc5780c313dfd1803838a89c6a90cdcd75d0cb2b` Copy that link by highlighting it and using command-c. Then, paste the link into the web browser of your choice.

Click on folders to navigate through them, or on files to open them. Text files will open with a built in text editor. Jupyter notebook files have the extension `.ipynb`. These are the files where you execute python code, and where we'll run our assignments from.



