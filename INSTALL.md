#Installation Tutorial

First, if you don't have i already you will need to install a version of Python.

##Python Installation:

###Linux

It is very likely that you already have Python installed out of the box. To check if you have it installed (and which version it is), open a console and type the following command:

command-line
```$ python3 --version
Python 3.5.1```

If you have a different 'micro version' of Python installed, e.g. 3.5.0, then you don't have to upgrade. If you don't have Python installed, or if you want a different version, you can install it as follows:

####Debian or Ubuntu
command-line
```$ sudo apt-get install python3.5```

####Fedora (up to 21)
command-line
```$ sudo yum install python3```

####Fedora (22+)
command-line
```$ sudo dnf install python3```

openSUSE
command-line
```$ sudo zypper install python3```


### macOS ( OS X )
The macOS comes with python 2.7, but it is a good idea to install Python3.

Before you install Python on OS X, you should ensure your Mac settings allow installing packages that aren't from the App Store. Go to System Preferences (it's in the Applications folder), click "Security & Privacy," and then the "General" tab. If your "Allow apps downloaded from:" is set to "Mac App Store," change it to "Mac App Store and identified developers."

You need to go to the website https://www.python.org/downloads/release/python-351/ and download the Python installer:

Download the Mac OS X 64-bit/32-bit installer file,
Double click python-3.5.1-macosx10.6.pkg to run the installer.
Verify the installation was successful by opening the Terminal application and running the python3 command:

command-line
```$ python3 --version
Python 3.5.1```

###Windows

You can download Python for Windows from the website https://www.python.org/downloads/release/python-351/. After downloading the *.msi file, you should run it (double-click on it) and follow the instructions there. It is important to remember the path (the directory) where you installed Python. It will be needed later!

One thing to watch out for: on the second screen of the installation wizard, marked "Customize", make sure you scroll down to the "Add python.exe to the Path" option and select "Will be installed on local hard drive".

Don't forget to add Python to the Path

In upcoming steps, you'll be using the Windows Command Line. For now, if you need to type in some commands, go to Start menu → All Programs → Accessories → Command Prompt. (On newer versions of Windows, you might have to search for "Command Prompt" since it's sometimes hidden.)


##Virtual environment (Optional, but recomended)

Before we install the necessary packages, we will get you to install an extremely useful tool to help keep your coding environment tidy on your computer. It's possible to skip this step, but it's highly recommended. Starting with the best possible setup will save you a lot of trouble in the future!

So, let's create a virtual environment (also called a virtualenv). Virtualenv will isolate your Python setup on a per-project basis. This means that any changes you make to one project won't affect any others you're also developing. This is similar to the Workspaces for Java developers.

All you need to do is find a directory in which you want to create the virtualenv; it is recomended that you create it inside your projects folder as it will be part of your project.

On Unix ( Linux and macOS):
``` mkdir folder_name && cd folder_name
python3 -m venv virtualenv_name(of your choice) ```

On Windows:

``` C:\Users\Name\projects\folder_name> C:\Python35\python -m venv virtualenv_name(of your choice) ```

Starting the Virtualenv:


``` $ source virtualenv_name/bin/activate```

NOTE: sometimes source might not be available. In those cases try doing this instead:

``` $ . virtualenv_name/bin/activate```

This is the recomended place for cloning this repository.
```git clone https://github.com/peixebabel/simple-recognition.git```

## Installing Scikit-learn, the Python Machine learning Framework

This Library requires NumPy and SciPy. To install them, run:

``` pip3 install NumPy SciPy
pip3 install -U scikit-learn ```


NOTE 1: if you only have one version of Python installed, you might not need to add the "3" in the command, thus you can use "pip instal.." instead.

NOTE 2: If you have a new installation of python, you probably already have PIP installed as well (a Python package installer)
But In case PIP ins't already installed, refer to this link to install it : https://pip.pypa.io/en/latest/installing/


##Caffe Framework

As this part is very different for each system, you can follow a step-by-step guide here (macOS check below first): [caffe.berkeleyvision.org/installation](http://caffe.berkeleyvision.org/installation.html#prerequisites)

### macOS

#### Homebrew
For the installation on the macOS, you are going to need the Homebrew Package Manager, and for that you will need the Command line tools. If you already have Xcode installed, you can just run the command ```xcode-select --install```

Or you can download it from [developer.apple](http://developer.apple.com/)


To install the Homebrew itself, run the following command:
``` ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" ```

Now you should be able to follow Caffe's tutorial.
