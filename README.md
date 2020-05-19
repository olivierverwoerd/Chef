# ATP Chef interpreter HER - WIP
![image](https://i.insider.com/58751b46dd0895e71f8b47b1?width=800&format=jpeg)

## Uitleg video
TBA

An very serious Advanced Technical Programming program
https://esolangs.org/wiki/chef


The basics of Chef:
Solids are int, Liquids are Chars

More info on how to use this delicious language here:
https://www.dangermouse.net/esoteric/chef.html


The actual assignment Must-haves: 
~~● Choose a (subset of) language, adhering to the abovementioned requirements: Chef~~
● Make an interpreter for your chosen (subset of a) language that can execute a file containing a correct script in this chosen language, and prints any output to the command line.
(Correctly implementing the must-haves, while adhering to all requirements, will land you a 5.5 out of 10 already.)
From Chapter 3:
○ Classes (e.g., for the Tokens and AST)
Chef, Kitchen, Ingredient
○ Inheritance
(Chef has Kitchen)
○ Object printing functions for every class (via __str__)
yes
○ “Private” variables (via information hiding) whenever appropriate
yes

○ Aspect-oriented programming through decorators (e.g., to obtain runtime
statistics of your programme, to do memoisation, etc.).
NOT YET

● From Chapter 4:
○ The programme must be written in a functional programming style.
○ All functions must be type-annotated (according to the format in Section 4.4),
both in the comments, and in the function definition itself.
yes
○ At least 3 applications of the functions: map, foldr, foldl, zipWith, zip, or other
higher order functions. 
()

NB: these higher-order functions have standard python
implementation; you do not need to implement them yourself (in fact, we strongly
advise you not to). For example, map is a standard function that can be used
without importing any libraries. foldl is called reduce in Python and is part of the
functools library for higher order functions. (Which is a very useful library that you

 
Should-haves:  The following functionality is optional. Each correctly implemented should-have will get you 
additional points. Note though that only the maximum is indicated. The lecturer may only award a proportion of the maximum number of points mentioned.  
● [max 3 points] Error-messaging ​Nothing is more annoying than your interpreter refusing your code without telling you what’s wrong, and on which line. Please implement proper error messages.  
● [max 4 points] Visualisation ​When learning how to program, it is very useful to see what’s going on in memory as the programme runs through the lines. Especially with notoriously difficult to grasp languages, such as Assembler. Please help a junior student out.  
● [max 3 points] Advanced language features ​It is easy enough to have a basic Turing complete language - even Brainfuck is Turing complete (​https://softwareengineering.stackexchange.com/questions/315919/how-is-brainfuck-turi ng-complete​). However, some advanced features, like defining your own functions, might be very nice to have. Anything beyond bare-bone Turing-complete languages will land you extra credit. (Yes, Assembler is “advanced” in this sense.)  
_● [max 2 points] Creating your own (UNUSED)_
● [max 2 points] Instruction-and-show-off video ​You can earn two points by making a (decent) instruction video on how to use the language and your interpreter, and how the interpreter works (code-wise). The minimal duration of this video is 5 min, and the max duration 15min.
