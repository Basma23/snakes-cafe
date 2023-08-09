# Lab: Class 1 - Intro to Python

## Overview

Today you'll begin working on a command line utility which will mimic the functionality of a point of sale restaurant system using your basic Python tools and understanding of the basics of the language.

## Feature Tasks and Requirements

- When run, the program should print an intro message and the menu for the restaurant
- The restaurant's menu should include appetizers, entrees, desserts, and beverages.
- The program should prompt the user for an order
- When a user enters an item, the program should print an acknowledgment of their input
- The program should tell the user how to exit
- The program's content should match included sample exactly
  - The > character represents user input line and should not be printed out

```console
$ python snakes_cafe.py
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
>
```

### Entering an order

```console
***********************************
** What would you like to order? **
***********************************
> Wings

** 1 order of Wings have been added to your meal **

> Wings

** 2 orders of Wings have been added to your meal **
```

### Exiting

```console
> quit
```
