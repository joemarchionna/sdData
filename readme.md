sdData - Testing Python Package Deployment
============================================
Project Description

Installation
============
<p>This is meant to be used as a library. To install this project manually (if not automatically installed) in another project run the following command:

```
    $ pip install git+ssh://git@github.com/joemarchionna/sdData.git
```

<p>This is not meant to be used as a library. To run, create a virtual environment and then add the dependancies with this command:

```
    $ pip install -r requirements/prod.txt
```

To run this project use the following command:

```
    $ pip install git+ssh://git@github.com/joemarchionna/sdData.git
```

If cloning this project to make updates, create a virtual environment and then add the dependancies with one of the following commands:

```
    $ pip install -r requirements/dev.txt
	$ pip install -r requirements/devlocal.txt
```

Dependancies
============
This project uses the following projects:

* none

Tests
=====
To run all tests in the project:

```
    $ source env/Scripts/activate
    $ python -m unittest discover -s sdData/tests/
```

To run a specific test in the project:

```
    $ source env/Scripts/activate
	$ python -m unittest sdData/tests/<module>.py
```

Code Formatting
===============
<p>Code formatting is done using BLACK. BLACK allows almost no customization to how code is formatted with the exception of line length, which has been set to 144 characters. VS Code supports BLACK using the shift-alt-f shortcut and the line length can be set in preferences, search for 'python formatting black'
<p>To bulk format files, the following command will work:

```
    $ black . -l 144
```
