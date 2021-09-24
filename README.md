Week 5 Problem Set
==================

**NOTE**: Some students have had problems compiling problem sets on Mac OS.
This is due to the Apple compiler being very conservative with its choice of
C++ standards. Using the C++11 standard should make this work -- use `g++ -std=c++11`
to enable this.

Sorting w/ Lookup
------------------------------

The file `sort_atoms.cpp` contains a vector of strings, with each
string containing an element symbol.

1.) Sort this list such that all elements are in order by their element
    number (not in alphabetical order). Print out this sorted vector.

2.) Find the unique elements of the vector (ie, remove duplicates), and print those out.

**Hint**: For #1, you should create a lookup table with an std::map, which you can use
to find the element number given a symbol. Then you need to write a custom
comparison function.


Calculating the Molecular Formula
---------------------------------

The file `molecule.cpp` contains some pieces of the now-familar molecule class.
Your task is to write a function to calculate the molecular formula as a string
from the atoms contained in the class.

For this exercise, it is enough to repeat the elements (ie, HHO rather than H2O).
However, the symbols should be in alphabetical order. For an extra challenge, try
making a proper chemical formula string with the numbers.

**Hint**: It would be helpful to have another lookup table as in the previous problem,
but going in the opposite direction.

