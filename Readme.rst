********************
Parametrize programs
********************

.. sectnum::
   :depth: 2

.. contents:: Table of Contents
   :depth: 2


Parametrize program
===================

Almost all complex program has some control parameters. 
It could be path to file to data to proceed, error reporting level, save location, used metrics and many other. 

If such parameters are hardcoded in code of program, then may be hard to use it on another machine, 
or share code top be used by other people. 

Using global level variables, which provide one place to edit which simplify this  
but still not solve problem with synchronistation between machines, 
especially when using ``git`` or other automated solution.

Current computers allow execute more than one process at the same time. 
Often case is to run same analysis against different files or parameters. 
In some programing language like C, C++ or Java each update of code require recompilation of code to 
make changes available in executable. This process may tke long time. 


Because of above mentioned limitations there is need to easy provide program parameters outside the code. 
Here there are described two options to solve this: *configuration file* and *command line arguments*. 

*configuration file* is structured file which contains mapping from name to value. 
One of basic format is ``.ini``

.. code-block:: ini

   [default]
   input="data/input"
   num=10
   result="result/result.txt"

This is simple, limited but human readable format. Its contains section marked by square braces (``[]``). 
And mapping *name* to *value*, where name need to be unique per each section. 
Python library to parse and create this file format is ``configparser``.

When more complex structures need to be handled there are more robust format like ``json`` or ``xml``.


Second option are *command line arguments* which where already mentioned on **Shell** classes.
They allow simple and fast change value for few parameters but 
provide dozen of parameters need long and hard to read line in shell. 

In python they are accessible by ``argv`` from ``sys`` library. 

.. code-block:: python
    
    import sys

    print(sys.argv)

Writing manual parser for program with multiple optional parameters is time consuming and it is easy to make a mistake. 
(see ``sample_code/simple_cli.py`` vs ``sample_code/argparse_reference.py``).
Default Python library to do this is ``argparse``

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