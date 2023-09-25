# Instructions to set run MoSDeF Workshops and Tutorials Locally
Click the following links to take you to installation instructions equivalent to your personal familiarity/expertise with setting up python environments

1. I have conda and python set up, and know how to use conda to install into a local environment -- [expert](#expert-level)
2. I need to check if I have conda installed -- [double check conda](#check-for-conda)
3. I need to install conda and have a MAC or LINUX OS -- [mac/os beginner](set_up_your_computers_MacOS.md)
4. I need to install conda and have a Windows OS -- [windows beginner](set_up_your_computers_Windows.md)
5. [I'm not certain](#additional-resources) 

## Expert Level
All python packages are available via conda-forge. Feel free to use `conda install mbuild gmso foyer` to install particular packages to your local environment. You can also view other dependencies in the [environment.yml](../environment.yml).

#### With [mamba](https://github.com/mamba-org/mamba) installed (much faster installation)
```bash 
$ git clone https://github.com/mosdef-hub/CECAM-MoSDeF-Workshop.git
$ cd CECAM-MoSDeF-Workshop
$ mamba env create -f environment.yml
$ conda activate mosdef_cecam
```
OR

#### Without mamba installed
```bash 
$ git clone https://github.com/mosdef-hub/CECAM-MoSDeF-Workshop.git
$ cd CECAM-MoSDeF-Workshop
$ conda env create -f environment.yml
$ conda activate mosdef_cecam
```

#### Installing simulation packages
Since MoSDeF enables writing simulation inputs to variety of simulation engines, it is necessary to know where to look to install these. The installation depends on the architecture of the device for best performance.
- [HOOMD-blue](https://hoomd-blue.readthedocs.io/en/latest/installation.html)
- [Cassandra](https://cassandra-mc.readthedocs.io/en/latest/getting_started/install.html)
- [GOMC](https://github.com/GOMC-WSU/GOMC#building-gomc-on-gnulinux-macos-or-cygwin)
- [LAMMPS](https://docs.lammps.org/Install.html)
- [GROMACS](https://manual.gromacs.org/documentation/current/install-guide/index.html)

## Check for conda
In order to test for conda on your current os, run this code:
```bash
$ which conda
$ conda list
$ conda update -n base conda
```

If this all worked okay, procede to [expert](#expert-level).
Else, proceed to steps 3 or 4 in the above heading: [Instuctions](#instructions-to-set-run-mosdef-workshops-and-tutorials-locally)


## Additional Resources  
See these additonal links for more in depth explanations of important topics for beginners:  
- **Knowing your computer OS**: https://mashable.com/article/how-to-find-operating-system
- **Working with your terminal**: https://swcarpentry.github.io/shell-novice/  
- **Introduction to Python**: https://swcarpentry.github.io/python-novice-inflammation/  
- **Introduction to Github**:   http://swcarpentry.github.io/git-novice/
