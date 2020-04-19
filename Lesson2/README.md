# Hands-on Tutorial

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/biovcnet/pythonBinderContent-L2/master?urlpath=lab)

In this tutorial, the participant will learn how to set and determine the datatype of a variable using python methods,
and apply some of the built-in python string functions to manipulate the way that text is displayed in print statements. 

The participant may refer to the following tables as needed:

**TABLE I**: DataTypes and corresponding python methods


| DataType      |python method        |
| ------------- |:------------------: |
| text          | str                 |
| numeric       | int, float, complex |
| Boolean       | bool                |
| binary        | bytes, memoryview   |
| set           | set                 |
| mapping       | dict                |
| seqence       | list, tuple, range  |

**TABLE II**: Python escape characters

| escape char.  | encoding            |
| ------------- |:------------------: |
| \\'           | single quote        |
| \\\           | backslash           |
| \n            | new line            |
| \r            | carriage return     |
| \t            | tab                 |
| \b            | backspace           |

**TABLE III**: Python string functions

| function      | format                                 |
| ------------- |:-------------------------------------: |
| .upper        | myString.upper()                       |
| .lower        | myString.lower()                       |
| .strip        | myString.strip(string)                 |
| .replace      | myString.replace(original,replacement) |
| .split        | myString.split(string)                 |




## Setting and determining datatypes of variables

The pre-written code contains only two lines

In the first line, a *variable* `y` is set as the integer, 6. Python will automatically classify the variable's datatype based on the user's input if the datatype is not explicitly set. 

The second line uses the python function `print` to show the variable in standard output and the datatype

Run the code to see standard output. For instructions on launching console and running code selections, see [Tutorial 1](https://github.com/biovcnet/python/tree/master/Lesson1)

<img align="left" src="/Lesson2/Images/L2Im1.png" width="900px" style="padding-right: 15px">

Notice that the print statement prints the integer 6, which `y` is now set to, and the datatype- `class int`


In the text editor:

retype the the variable declaration and the print function below to set the variable using each python method in the *python function* column of **Table I**. The print statement remain the same, but must be repeated each time the variable is reset,
because y is no longer the same. You may do this in any order you like as long as the **last time the variable is set as a string**. This is required for the next exercise.

Let's do one together!

Here, under the original code, i have set the variable `y` to be the datatype `float`

Look at the console, and we can see that `y` now prints as 6.0 because it is `class float`

<img align="left" src="/Lesson2/Images/L2Im2.png" width="900px" style="padding-right: 15px">


## string manipulation

Python strings can be manipulated by several built-in functions. The most common are `strip`,`lower`,`upper`,`replace`, and `split`

These built in functions are used in the format `theString.function()`. Specifics are in **Table III**

Technical note on `strip`: it only strips the string of the *leading* and *trailing* characters specified.

Before we continue, double check that **y is set as str** in your console by running the command `print(y(type))`

We are first going to *concatenate* y with another string- combine into into one string. Strings can be concatenated using a `+`

In your notebook, set a variable `newString` as `'y is '+y`

Let's now let's set newString to an altered version of itself using the built in functions.

In the text editor, do the following in this order:

+ set newString to all uppercase letters and print 
+ set newString to all lowercase letters and print
+ remove any occurrences of the character `y` at the trailing ends of the string and print
+ replace the space now at the beginning of newString with `y` and print
+ break up the string along occurrences of the `space character` print


<img align="left" src="/Lesson2/Images/L2Im3.png" width="900px" style="padding-right: 15px">






