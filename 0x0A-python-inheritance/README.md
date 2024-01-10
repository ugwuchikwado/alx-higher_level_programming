# 0x0A. Python - Inheritance

## General


   * Why Python programming is awesome
   * What is a superclass, baseclass or parentclass
   * What is a subclass
   * How to list all attributes and methods of a class or instance
   * When can an instance have new attributes
   * How to inherit class from another
   * How to define a class with multiple base classes
   * What is the default class every class inherit from
   * How to override a method or attribute inherited from the base class
   * Which attributes or methods are available by heritage to subclasses
   * What is the purpose of inheritance
   * What are, when and how to use isinstance, issubclass, type and super built-in functions

## Reqyurements
### Python Scripts


  *  Allowed editors: vi, vim, emacs
  *  All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
  *  All your files should end with a new line
  *  The first line of all your files should be exactly #!/usr/bin/python3
  *  A README.md file, at the root of the folder of the project, is mandatory
  *  Your code should use the pycodestyle (version 2.8.*)
  *  All your files must be executable
  *  The length of your files will be tested using wc

# Tasks

### 0.Lookup

Write a function that returns the list of available attributes and methods of an object:

  *  Prototype: def lookup(obj):
  *  Returns a list object
  *  You are not allowed to import any module

### 1. My List

Write a class MyList that inherits from list:

  *  Public instance method: def print_sorted(self): that prints the list, but sorted (ascending sort)
  *  You can assume that all the elements of the list will be of type int
  *  You are not allowed to import any module

### 2. Exact same object

Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.

  *  Prototype: def is_same_class(obj, a_class):
  *  You are not allowed to import any module

### 3. Same Class or Inherit from

Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.

  *  Prototype: def is_kind_of_class(obj, a_class):
  *  You are not allowed to import any module

### 4. Only Subclass of

Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.

  *  Prototype: def inherits_from(obj, a_class):
  *  You are not allowed to import any module

### 5. Geometry module

Write an empty class BaseGeometry.

   * You are not allowed to import any module

### 6. mprove geometry

Write a class BaseGeometry (based on 5-base_geometry.py).

   * Public instance method: def area(self): that raises an Exception with the message area() is not implemented
   * You are not allowed to import any module

### 7. Integer Validator

Write a class BaseGeometry (based on 6-base_geometry.py).

  *  Public instance method: def area(self): that raises an Exception with the message area() is not implemented
  *  Public instance method: def integer_validator(self, name, value): that validates value:
        you can assume name is always a string
        if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
        if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0
 *   You are not allowed to import any module

### 8. Rectangle

Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).

  *  Instantiation with width and height: def __init__(self, width, height):
        width and height must be private. No getter or setter
        width and height must be positive integers, validated by integer_validator

### 9. Full Reactangle

Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)

    Instantiation with width and height: def __init__(self, width, height)::
        width and height must be private. No getter or setter
        width and height must be positive integers validated by integer_validator
    the area() method must be implemented
    print() should print, and str() should return, the following rectangle description: [Rectangle] <width>/<height>

### 10. Square #1

Write a class Square that inherits from Rectangle (9-rectangle.py):

    Instantiation with size: def __init__(self, size)::
        size must be private. No getter or setter
        size must be a positive integer, validated by integer_validator
    the area() method must be implemented


### 11. Square #2

Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).

    Instantiation with size: def __init__(self, size)::
        size must be private. No getter or setter
        size must be a positive integer, validated by integer_validator
    the area() method must be implemented
    print() should print, and str() should return, the square description: [Square] <width>/<height>

### 12. My Integer

Write a class MyInt that inherits from int:

    MyInt is a rebel. MyInt has == and != operators inverted
    You are not allowed to import any module

### 13. Can I

Write a function that adds a new attribute to an object if it’s possible:

    Raise a TypeError exception, with the message can't add new attribute if the object can’t have new attribute
    You are not allowed to use try/except
    You are not allowed to import any module
