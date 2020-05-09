# Chef interpreter
![image](https://user-images.githubusercontent.com/22635990/80474326-9db83580-8947-11ea-951b-d731f99f3a00.png)


## Uitleg video
https://youtu.be/k1imKpUVZ18

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

To-do
Fold ingredient into [nth] mixing bowl.
This removes the top value from the nth mixing bowl and places it in the ingredient.
Add ingredient [to [nth] mixing bowl].
This adds the value of ingredient to the value of the ingredient on top of the nth mixing bowl and stores the result in the nth mixing bowl.
Remove ingredient [from [nth] mixing bowl].
This subtracts the value of ingredient from the value of the ingredient on top of the nth mixing bowl and stores the result in the nth mixing bowl.
Combine ingredient [into [nth] mixing bowl].
This multiplies the value of ingredient by the value of the ingredient on top of the nth mixing bowl and stores the result in the nth mixing bowl.
Divide ingredient [into [nth] mixing bowl].
This divides the value of ingredient into the value of the ingredient on top of the nth mixing bowl and stores the result in the nth mixing bowl.
Add dry ingredients [to [nth] mixing bowl].
This adds the values of all the dry ingredients together and places the result into the nth mixing bowl.
Liquefy | Liquify ingredient.
This turns the ingredient into a liquid, i.e. a Unicode character for output purposes. (Note: The original specification used the word "Liquify", which is a spelling error. "Liquify" is deprecated. Use "Liquefy" in all new code.)
Stir [the [nth] mixing bowl] for number minutes.
This "rolls" the top number ingredients in the nth mixing bowl, such that the top ingredient goes down that number of ingredients and all ingredients above it rise one place. If there are not that many ingredients in the bowl, the top ingredient goes to tbe bottom of the bowl and all the others rise one place.
Stir ingredient into the [nth] mixing bowl.
This rolls the number of ingredients in the nth mixing bowl equal to the value of ingredient, such that the top ingredient goes down that number of ingredients and all ingredients above it rise one place. If there are not that many ingredients in the bowl, the top ingredient goes to the bottom of the bowl and all the others rise one place.
Mix [the [nth] mixing bowl] well.
This randomises the order of the ingredients in the nth mixing bowl.
Clean [nth] mixing bowl.
This removes all the ingredients from the nth mixing bowl.
Verb the ingredient.
This marks the beginning of a loop. It must appear as a matched pair with the following statement. The loop executes as follows: The value of ingredient is checked. If it is non-zero, the body of the loop executes until it reaches the "until" statement. The value of ingredient is rechecked. If it is non-zero, the loop executes again. If at any check the value of ingredient is zero, the loop exits and execution continues at the statement after the "until". Loops may be nested.
Verb [the ingredient] until verbed.
This marks the end of a loop. It must appear as a matched pair with the above statement. verbed must match the Verb in the matching loop start statement. The Verb in this statement may be arbitrary and is ignored. If the ingredient appears in this statement, its value is decremented by 1 when this statement executes. The ingredient does not have to match the ingredient in the matching loop start statement.
Set aside.
This causes execution of the innermost loop in which it occurs to end immediately and execution to continue at the statement after the "until".