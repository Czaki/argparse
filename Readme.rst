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
It could be path to file with data to proceed, error reporting level, save location, used metrics and other. 

Lets take such simple program which copy first ``count_lines`` from one file to second.

.. code-block:: python

   def copy_lines(input_file, result_file, count_lines):
      with open(input_file, 'r') as r_f, open(result_file, 'w') as w_f:
         for _ in range(count_lines):
               w_f.write(r_f.readline())

   copy_lines("data/input.txt", "result/result.txt", 10)

From shell it could be called this way:

.. code-block:: bash 

   $ python copy_script.py

If such parameters are hardcoded in code of program, then may be hard to use it on another machine, 
or share code with other people. 

Even simplify update it by put all control variables in one place does not solve this problem. 
When synchronize code between machines user need to remember to update variables to local values. 
Especially this may introduce redundant work when using automated systems like ``git`` or even *Dropbox*

Current computers allow execute more than one process at the same time. 
Often case is to run same analysis against different files or parameters. 
In some programing language like C, C++ or Java each update of code require recompilation of code to 
make changes available in executable. This process may take long time. 


Because of above mentioned limitations there is need to easy provide program parameters outside the code. 
Here there are described two options to solve this: *configuration file* and *command line arguments*. 

configuration file
~~~~~~~~~~~~~~~~~~

*configuration file* is structured file which contains mapping from name to value. 
One of basic format is ``.ini``. Example of simple ``.ini`` file bellow:

.. code-block:: ini

   [default]
   input_file="data/input.txt"
   count_lines=10
   result_file="result/result.txt"

   [windows]
   input_file="data\input.txt"
   result_file="result\result.txt"

This is simple, limited but human readable format. Its contains at least one 
section which header is marked by square braces (``[]``), in example there are two sections. 
Content of section is mapping *name* to *value*, where name need to be unique per each section. 
Python library which allow to parse and create this file format is ``configparser``.

Same program as above with ``configparse``

.. code-block:: python

   import configparser
   import os

   dir_name = os.path.dirname(__file__)

   config = configparser.ConfigParser()
   config.read(os.path.join(dir_name, "sample_config.ini"))

   def copy_lines(input_file, result_file, count_lines):
      with open(input_file, 'r') as r_f, open(result_file, 'w') as w_f:
         for _ in range(count_lines):
               w_f.write(r_f.readline())

   copy_lines(
      config["default"]["input_file"],
      config["default"]["result_file"],
      config["default"]["count_lines"]
   )


it is possible to make some parameter optional in file using ``get`` function. 
Below parameter ``count_lines`` is optional with default variable ``10``:

.. code-block:: python

   import configparser
   import os

   dir_name = os.path.dirname(__file__)

   config = configparser.ConfigParser()
   config.read(os.path.join(dir_name, "sample_config.ini"))

   def copy_lines(input_file, result_file, count_lines):
      with open(input_file, 'r') as r_f, open(result_file, 'w') as w_f:
         for _ in range(count_lines):
               w_f.write(r_f.readline())

   copy_lines(
      config["default"]["input_file"],
      config["default"]["result_file"],
      config["default"].get("count_lines", 10)
   )


When more complex structures need to be handled there are more robust format like ``json`` or ``xml``.

command line arguments
~~~~~~~~~~~~~~~~~~~~~~
Second option are *command line arguments* which where already mentioned on **Shell** classes.
This method provide user friendly interface if user need only few parameters. 
But it is not an optimal solution if user need to provide dozen or more parameters. 
They allow simple and fast change value for few parameters but 
provide dozen of parameters need long and harder to read line in shell. 

In Python they are accessible by ``argv`` from ``sys`` library.
This code show show same example program but with parameters read from argv:

.. code-block:: python
    
   import sys

   def copy_lines(input_file, result_file, count_lines):
      with open(input_file, 'r') as r_f, open(result_file, 'w') as w_f:
         for _ in range(count_lines):
               w_f.write(r_f.readline())

   copy_lines(sys.argv[1], sys.argv[2], sys.argv[3])

To make ``count_lines`` optional there is need to check length of list ``sys.argv``. 

.. code-block:: python
   
   import sys

   def copy_lines(input_file, result_file, count_lines):
      with open(input_file, 'r') as r_f, open(result_file, 'w') as w_f:
         for _ in range(count_lines):
               w_f.write(r_f.readline())

   copy_lines(
      sys.argv[1],
      sys.argv[2],
      sys.argv[3] if len(sys.argv) == 4 else 10
   )

In contradiction to earlier examples its calls from shell will look like:

.. code-block:: bash 

   $ python copy_script.py "data/input.txt" "result/result.txt" 10

The common case of program is to have only few mandatory parameters but many optionals. 
For example this program could be extended with options to copy last lines, every second lines etc. 
It could be control in approach shown during **Shell** class using flag like ``--tail`` or ``--every-second``.

Base library for parse ``argv`` variable content is ``argparse``. Using this library out program will look:

.. code-block:: python

   import argparse

   parser = argparse.ArgumentParser()
   parser.add_argument("input_file")
   parser.add_argument("result_file")
   parser.add_argument("count_lines")

   args = parser.parse_args()

   def copy_lines(input_file, result_file, count_lines):
      with open(input_file, 'r') as r_f, open(result_file, 'w') as w_f:
         for _ in range(count_lines):
               w_f.write(r_f.readline())

   copy_lines(args.input_file, args.result_file, args.count_lines)

As could be seen from comparing above example, if program has only positional parameters 
the code which use ``argv`` variable is shorter. But usage of ``argparse`` has multiple benefits:

* type checking - ``add_argument`` has optional argument ``type`` which takes function to convert provided string to chosen type
* help text - argparse automatically generate help string which could be used to remind parameter

.. code-block:: python

   import argparse

   parser = argparse.ArgumentParser()
   parser.add_argument("input_file", help="file to be read")
   parser.add_argument("result_file", help="file to save result")
   parser.add_argument(
      "count_lines", type=int, default=10, nargs="?", help="Number of lines to be copied, default 10"
   )
   parser.add_argument(
      "--append", action="store_const", const="a", default="w", help="append result to `result_file`", dest="append"
   )

   args = parser.parse_args()

   def copy_lines(input_file, result_file, count_lines, write_mode):
      with open(input_file, 'r') as r_f, open(result_file, write_mode) as w_f:
         for _ in range(count_lines):
               w_f.write(r_f.readline())

   copy_lines(args.input_file, args.result_file, args.count_lines, args.append)

``argparse``

If program have multiple parameters, especially optionals then
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
Write own ``type`` checking function which will check if file ``input`` exists and if not then raise proper exception
See: https://docs.python.org/3/library/argparse.html#type

Exercise 3
~~~~~~~~~~
Modify code from exercise 1 to read default values from config file ``sample_code/sample_config.ini``


Exercise 4
~~~~~~~~~~
Modify code from exercise 2 to have optional argument with path to config file and read default values from this config file.