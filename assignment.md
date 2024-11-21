<!-- omit in toc -->
# Problem Set 5

## Python - Object-Oriented Programming, Decorators, and Context Managers

For this homework, you will design a set of Python classes to model the behavior of different types of gases: real gases and ideal gases. **Some of the design parameters for these classes are already defined in the provided testing file (`test_gases.py`).** However, please read the assignment explanation before moving to this file. Using this file will come later in Part 2.

Ideal gases are commonly used to introduce thermodynamic concepts, with their behavior described by the equation:

$$
PV = nRT
$$

where:

- \( P \) represents pressure,
- \( V \) is the volume,
- \( n \) is the number of moles,
- \( R \) is the ideal gas constant, and
- \( T \) is the temperature.

The behavior of real gases is more complex. Real gases can be modeled different equations with one of them being the van der Waals equation. The van der Waals gas equation takes particle volume and interactions into account through parameters \( a \) and \( b \), as described by the equation:

$$
\left( P + \frac{a n^{2}} {V^{2}} \right) ( V - nb) = nRT
$$


This homework will have three main parts: **Class Design**, **Testing**, and **Documentation and Discussion**. You should first think about class structure (without implementing code), then use the provided tests in (2) to write your code.


### Part 1 - Class Design

Design a class structure to model the behavior of gases. You should create two classes for this: `IdealGas` and `RealGas`. Decide whether to use inheritance or composition, and whether a base class is needed. You do not need to write code yet - more details such as what should be in the constructor for Part 2. Think about the equations for `RealGas` and `IdealGas`when making your decision.

You have a few options when it comes to designing the two classes. You might choose to write one as a base class then utilize inheritance, or you may decide to implement them separately. Consider properties such as temperature, volume, and moles, and determine where they belong in your design.


### Part 2 - Developing with Test Driven Development

Test Driven Development to develop your code. [Test Driven Development](https://en.wikipedia.org/wiki/Test-driven_development) is a development technique where tests are created before the code is developed. 

Tests for ideal gases are provided in `test_gases.py`. Use the provided tests to guide your implementation of the classes. You should write your `IdealGas` class so that these tests pass. 

In addition to using the provided tests, you should also develop your `RealGas` class. You should also write additional tests for your `RealGas` class.

### Part 3  PyTest Decorators and Context Managers

The provided tests are written as individual tests. You should refactor the tests to use the [pytest parametrize](https://docs.pytest.org/en/7.3.x/how-to/parametrize.html). You will also identify a context manager used in the provided tests that is part of pytest which will allow you to test for expected exceptions.


### Documentation and Discussion

As always, you should include overview information about how to install and run your code in the `README.md` file. In addition, you should include a discussion of your class design decisions.

1. **Class Design Decisions**: Discuss the relationship between `RealGas` and `IdealGas`. Did you choose to use inheritance, composition, or separate classes? What factors influenced your decision?

2. **Shared Properties**: Explain how you handled shared properties like temperature, volume, and moles. Why did you place these attributes in certain classes, and how did that contribute to code clarity and reusability?

3. **Mixing Behavior**: Describe how you approached the implementation of gas mixing parameters. Where did you implement these methods, and how did the equations guide your design decisions?

4. **Decorator Usage**: Where did you use `@property` in your class? Why was it useful for your design? Did you use any other decorators, and how did they simplify or improve your code?

5. **Testing and Design Alignment**: How did the provided test cases influence your class design? Did you need to adjust your design decisions to ensure your classes passed the tests? 

6. **Future Extensibility**: If you needed to model other real gas equations beyond the van der Waals equation, how would your design change, if at all? Was your current approach flexible enough to accommodate this?

## Debugging a C++ application

The file `crashes.cpp` contains a program that sometimes crashes. Use your
debugging knowledge to find the issue.

Write up the cause of the issue in the README file.
Include any output from debuggers or sanitizers that helped you.


## Profiling C++ Code

In this repo is a file `mcsim_cpp.cpp` which contains code for the `mcscim`
package from the bootcamp. Using `gprof`, profile this code and include the
output in a file in this repo. Iinclude anything you find surprising
or interesting. Put this information into the README.

Do the above for two optimzation levels - `-O0` and `-O3`. Is there anything
interesting about one compared to the other?


## Profiling Python Code

Similar to the above, but profiling the `mcsim_psl.py` program with python's
cProfile. There are no optimization levels, so only one profiler run needs
to be done. You can visualize the results using a program called [snakeviz](https://jiffyclub.github.io/snakeviz/). Is there anything taking a surprising amount of time?

## Documentation and Discussion

Add answers to the questions from the sections above in your `README`. Your code should also contain a `Makefile` with targets for profiling the Python and C++ code.

<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config">
    MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
</script>

