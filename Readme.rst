********
Argparse
********

.. sectnum::
   :depth: 2

.. contents:: Table of Contents
   :depth: 2


Command line interface
======================

Write code which has hardcoded all parameters in code may make hard to use it on another machine, 
or share code top be used by other people. 

First way to do this is to extract values to global level variables, which provide one place to edit 
all values, but also it may create problem with synchronistation between machines.  

If program have binary form (Python code could be converted to binary executable for example with ``Pyinstaller``).
then each update force to rebuild whole project. 

Because of mentioned limitations there is need to easy provide program parameters outside the code. 
There are two options: *configuration file* and *command line arguments*. 

For *configuration file* most popular format for basic one is ``.ini`` format. 
Python library to work with such file is ``configparser``. 
There are more formats, which may handle more complex formats, like ``json``. 

Other option are *command line* arguments which where mentioned on **Shell** classes.
In python they are accessible by ``argv`` from ``sys`` library. 

.. code-block:: python
    
    import sys

    print(sys.argv)

But instead of manual parsing, especially in case of multiple optional parameters, 
it is nicer to use library which hide all this logic for Python such library is ``argparse``.

Both approach could be used mixed.


Documentation https://docs.python.org/3/library/argparse.html and https://docs.python.org/3/library/configparser.html


Exercises
=========

Exercise 1
~~~~~~~~~~
Create program which take as argument one existing file, one integer number and one result file as in below help. 
(All with default parameters)

 .. code-block::

   Usage: exercise_1.py [-h] [-i,--input INPUT] [-n,--num NUM] [-o,--output OUTPUT]

   optional arguments:
   -h, --help          show this help message and exit
   -i,--input INPUT
   -n,--num NUM
   -o,--output OUTPUT

program should print values of ``input``, ``num`` and ``output`` on standard output


Exercise 2
~~~~~~~~~~
Modify code from exercise 1 to read default values from config file ``sample_code/sample_config.ini``


Exercise 3
~~~~~~~~~~
Modify code from exercise 2 to have optional argument with path to config file and read default values from this config file.