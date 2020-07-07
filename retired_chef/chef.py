"""A simple chef interpreter made with a functional method"""
import re
from kitchen import *
from ingredient import *


class Chef:
    """
    This is the chef. Basically the file parser nothing special here
    """
    def __init__(self, recipe: str, objective="", kitchen=None, debug=False):
        self.recipe = recipe.lower()
        self.recipe_lines = re.split("\n|\. ",recipe.lower())
        if kitchen == None:
            self.kitchen = Kitchen([], [[]], [[]])
        else:
            self.kitchen = kitchen
        self.objective = objective
        self.serving_queue = ""
        self.already_made = []
        self.debug = debug
        self.loop_counter = []
        self.loop_endings = []
        self.loop_lines = []


    def __str__(self):
        if self.objective == "":
            return "Hello. I am the chef."
        return "Hello. I am sous chef. I'm just here to make: " + self.objective

    @property
    def cook(self): #Reads the code
        """
        0: "title",
        1: "comment", (unused)
        2: "ingredient list",
        3: "cooking time",
        4: "oven temperature",
        5: "methods",
        6: "serve amount"
        7: "refrigerate"
        :return:
        """
        progress = 0
        line_index = 0
        # for line in self.recipe_lines:
        while line_index < len(self.recipe_lines):
            line = self.recipe_lines[line_index]
            line_index += 1
            if progress is 0:
                for served in self.already_made:
                    if line.startswith(served):
                        while not (line.startswith("serve") or line.startswith("refrigerat")):
                            line = self.recipe_lines[line_index]
                            line_index += 1
                        if line_index >= len(self.recipe_lines):
                            return # done with all
                        line = self.recipe_lines[line_index]
                        line_index += 1
                        break
                if self.objective == "":
                    print("Cooking: " + line)
                else:
                    print("Cooking side dish: " + self.objective)
                    sub_line_index = 0
                    while sub_line_index < len(self.recipe_lines):
                        line = self.recipe_lines[sub_line_index]
                        sub_line_index += 1
                        if line.startswith(self.objective):
                            line_index = sub_line_index
                            break


                progress = 1

            if line is "" and (progress == 1 or progress == 3 or progress == 4):
                progress += 1

            if line.startswith("cooking time"):
                    progress = 5
            if line.startswith("pre-heat"):
                progress = 5
            if line.startswith("serve"):
                progress = 6
            if line.startswith("refrigerate"):
                progress = 7

            if progress is 3:  # ingredients
                p = re.findall(
                    r'(([0-9]*) ?(k?g|pinch(?:es)?|m?l|dash(?:es)?|cups?|teaspoons?|tablespoons?)? ?([a-zA-Z ]+))',
                    line)
                if len(p) is 0:
                    print("Somethings wrong with the ingredient:" + line)
                else:
                    if (p[0][2] in ("dash", "cup", "l", "ml", "dashes", "cups")):
                        state = "liquid"
                    elif (p[0][2] in ("heaped", "level", "g", "kg", "pinch(es)?", "pinches")):
                        state = "dry"
                    else:
                        state = "unknown"
                    self.kitchen.add_ingredient(Ingredient(int(p[0][1]), state, str(p[0][3])))

            if progress is 6:  # serve
                p = re.findall(r'(serves) (\d+)', line)
                if len(p) is 0:
                    p = re.findall(r'(serve with) ([a-zA-Z ]+\.)', line)
                    if len(p) is 0:
                        print("Nothing to serve with")
                    else:
                        Sous_chef = Chef(self.recipe, p[0][1], Kitchen([], self.kitchen.get_mixingbowls().copy(), self.kitchen.get_bakingdishes().copy()), debug=self.debug)
                        self.already_made.append(p[0][1])
                        self.serving_queue += Sous_chef.cook
                        self.serving_queue += self.kitchen.serve()
                        return self.serving_queue
                else:
                    s = self.kitchen.serve(int(p[0][1]))
                    return s
                progress = 0

            if progress is 7:  # serve
                if line == "refrigerate":
                    return
                p = re.findall(r'(refrigerate for) (\d*) (\w*)', line)
                return self.kitchen.serve(int(p[0][1]))

            # Method tree ------------------------------------------------------------
            if progress is 5:
                if line == "" \
                        or line.startswith("bake") \
                        or line.startswith("wait until baked") \
                        or line.startswith("method") \
                        or line.startswith("cooking time") \
                        or line.startswith("pre-heat"):
                    continue # just ignore that

                if self.debug:
                    print(line)
                take = re.findall(r"take ([a-zA-Z]+) from refrigerator", line)
                put = re.findall(r"^put ?([a-zA-Z ]+) into (?:the )?(?:([1-9]\d*)(?:st|nd|rd|th) )?mixing bowl", line)
                fold = re.findall(r"fold ([a-zA-Z ]+) into (?:the )?(?:([1-9]\d*)(?:st|nd|rd|th) )?mixing bowl", line)
                add = re.findall(r"add ([a-zA-Z ]+?) to (?:([1-9]\d*)(?:st|nd|rd|th) )?mixing bowl", line)
                add_dry = re.findall(r"add dry ingredients to (?:the )?(?:([1-9]\d*)(?:st|nd|rd|th) )?mixing bowl", line)
                remove = re.findall(r"remove ([a-zA-Z ]+?) from (?:the )?(?:([1-9]\d*)(?:st|nd|rd|th) )?mixing bowl", line)
                combine = re.findall(r"combine ([a-zA-Z ]+?) into (?:the )?(?:([1-9]\d*)(?:st|nd|rd|th) )?mixing bowl", line)
                divide = re.findall(r"divide ([a-zA-Z ]+?) into (?:the )?(?:([1-9]\d*)(?:st|nd|rd|th) )?mixing bowl", line)
                liquify = re.findall(r"(liquefy) (the )?([a-zA-Z ]+)\.", line)
                liquify_contents = re.findall(r"(liquefy (the )?contents of the) ([1-9]\d*)?[a-zA-Z ]+", line)
                stir = re.findall(r"stir (the )?([1-9]\d*)?([a-zA-Z ]+)?mixing bowl for (\d+)", line) #?([a-zA-Z ]+)?mixing bowl for (\d+)
                stir_ingredient = re.findall(r"stir ([a-zA-Z ]+?) into (?:the )?(?:(1st|2nd|3rd|[0-9]+th) )?mixing bowl", line)
                mix = re.findall(r"mix the (?:([1-9]\d*)(?:st|nd|rd|th) )?mixing bowl well", line)
                clean = re.findall(r"(clean the) ([1-9]\d*)?[a-zA-Z ]+", line)
                pour = re.findall(r"(pour contents of the) ([1-9]\d*)?[a-zA-Z ]+ ([1-9]\d*)?", line)
                verb_until = re.findall(r"([a-zA-Z]+) (the )?([a-zA-Z ]+)?until ([a-zA-Z ]+)", line)
                verb = re.findall(r"([a-zA-Z]+) the ([a-zA-Z ]+)", line)
                zipwith = re.findall(r"zipwith (?:the )?(?:([1-9]\d*)(?:st|nd|rd|th) )?mixing bowl (with|without|times|halve) (?:the )?(?:([1-9]\d*)(?:st|nd|rd|th) )?mixing bowl", line)
                reduce = re.findall(r"(foldl|foldr) ([a-zA-Z]+)? (into|out|times|halve) (?:the )?(?:([1-9]\d*)(?:st|nd|rd|th) )?mixing bowl", line)
                if len(take) == 1:
                    anwer = input("How much " + take[0] + " shall we add this time?: ")
                    p = re.findall(r'([0-9]*) ?(k?g|pinch(?:es)?|m?l|dash(?:es)?|cups?|teaspoons?|tablespoons?)?',
                    anwer)
                    if len(p) == 2:
                        state ="unknown"
                        if (p[0][1] in ("dash", "cup", "l", "ml", "dashes", "cups")):
                            state = "liquid"
                        elif (p[0][1] in ("heaped", "level", "g", "kg", "pinch(es)?", "pinches")):
                            state = "dry"
                        self.kitchen.add_ingredient(Ingredient(int(p[0][0]), state, take[0]))
                    else:
                        self.kitchen.add_ingredient(Ingredient(0, "unknown", take[0]))
                        print("Or we add non. That's fine")

                elif len(put) == 1:
                    mixing_index = 0
                    if put[0][1] != '':
                        mixing_index = int(put[0][1]) - 1
                    self.kitchen.put_ingredient_into_the_mixing_bowl(put[0][0], mixing_index)
                elif len(fold) == 1:
                    mixing_index = 0
                    if fold[0][1] != '':
                        mixing_index = int(fold[0][1]) - 1
                    self.kitchen.fold(fold[0][0], mixing_index)
                elif len(add) == 1:
                    mixing_index = 0
                    if add[0][1] != '':
                        mixing_index = int(add[0][1]) - 1
                    self.kitchen.add(add[0][0], mixing_index)
                elif len(add_dry) == 1:
                    mixing_index = 0
                    if add_dry[0][1] != '':
                        mixing_index = int(add_dry[0][1]) - 1
                    self.kitchen.add_dry(mixing_index)
                elif len(remove) == 1:
                    mixing_index = 0
                    if remove[0][1] != '':
                        mixing_index = int(remove[0][1]) - 1
                    self.kitchen.remove(remove[0][0], mixing_index)
                elif len(combine) == 1:
                    mixing_index = 0
                    if combine[0][1] != '':
                        mixing_index = int(combine[0][1]) - 1
                    self.kitchen.combine(combine[0][0], mixing_index)
                elif len(divide) == 1:
                    mixing_index = 0
                    if divide[0][1] != '':
                        mixing_index = int(divide[0][1]) - 1
                    self.kitchen.divide(divide[0][0], mixing_index)
                elif len(liquify_contents) == 1:
                    mixing_index = 0
                    if liquify_contents[0][2] != '':
                        mixing_index = int(liquify_contents[0][2]) - 1
                    self.kitchen.liquify_mixingbowl(mixing_index)
                elif len(liquify) == 1:
                    self.kitchen.liquify(liquify[0][2])
                elif len(stir) == 1:
                    mixing_index = 0
                    if stir[0][1] != '':
                        mixing_index = int(stir[0][1]) - 1
                    self.kitchen.stir(mixing_index, int(stir[0][3]))
                elif len(stir_ingredient) == 1:
                    mixing_index = 0
                    if stir[0][1] != '':
                        mixing_index = int(stir[0][1]) - 1
                    self.kitchen.stir_ingredient(mixing_index, int(stir[0][0]))
                elif len(mix) == 1:
                    self.kitchen.mix(int(mix[0]) - 1)
                elif len(clean) == 1:
                    mixing_index = 0
                    if clean[0][1] != '':
                        mixing_index = int(clean[0][1]) - 1
                    self.kitchen.clean(mixing_index)
                elif len(pour) >= 1:
                    mixing_index = 0
                    baking_index = 0
                    if pour[0][1] != '':
                        mixing_index = int(pour[0][1]) - 1
                    if pour[0][2] != '':
                        baking_index = int(pour[0][2]) - 1
                    self.kitchen.put_mixing_bowl_onto_the_bakingdish(mixing_index, baking_index)
                elif len(zipwith) == 1:
                    mixing_indexA = 0
                    mixing_indexB = 0
                    function = '+'
                    if zipwith[0][0] != '':
                        mixing_indexA = int(zipwith[0][0]) - 1
                    if zipwith[0][2] != '':
                        mixing_indexB = int(zipwith[0][2]) - 1
                    if zipwith[0][1] == 'without':
                        function = '-'
                    if zipwith[0][1] == 'times':
                        function = '*'
                    if zipwith[0][1] == 'halve':
                        function = '/'
                    self.kitchen.zipwith(mixing_indexA, mixing_indexB, function)
                elif len(reduce) == 1:
                    mixing_index = 0
                    side = "left"
                    operator = '+'
                    if reduce[0][0] == 'foldr':
                        side = "right"
                    if reduce[0][2] == 'out':
                        operator = '-'
                    if reduce[0][2] == 'times':
                        operator = '*'
                    if reduce[0][2] == 'halve':
                        operator = '/'
                    if reduce[0][3] != '':
                        mixing_index = int(reduce[0][3]) - 1
                    self.kitchen.reduce(side, reduce[0][1], operator, mixing_index)
                elif len(verb_until) == 1:
                    if verb_until[0][3] in self.loop_endings:
                        index = self.loop_endings.index(verb_until[0][3])
                        if self.loop_counter[index] == 0:
                            del self.loop_endings[index]
                            del self.loop_lines[index]
                            del self.loop_counter[index]
                        else:
                            self.loop_counter[index] -= 1
                            line_index = self.loop_lines[index]
                    else:
                        print("The loop is not correctly closed by a verb+ed")
                elif len(verb) == 1:
                    end_trigger = verb[0][0]
                    if end_trigger[-1] != 'e':
                        end_trigger += 'e'
                    end_trigger += 'd'
                    self.loop_endings.append(end_trigger)
                    self.loop_lines.append(line_index+1)
                    self.loop_counter.append(self.kitchen.get_amount_of_ingredient(verb[0][1]))
                else:
                    if line == "set aside.":
                        self.loop_counter[-1] = 0
                    else:
                        print("That instruction wasn't very cash money of you. Please change: " + line)
            # END of Method tree ------------------------------------------------------------

            elif line.startswith("ingredients"):
                progress = 3

            elif line.startswith("method."):
                progress = 5

            if self.debug:
                print(self.kitchen)


def run(file_name: str, debug=False) -> str:
    """
    Main opens the file and runs the code directly
    :param file_name: The filename in this directory to run.
    """
    print("Running " + file_name)
    print("-------------------------------")
    f = open(file_name, "r")
    recipe = f.read()
    Gordon_Ramsay = Chef(recipe, debug=debug)
    dinner = Gordon_Ramsay.cook
    del Gordon_Ramsay
    return dinner


def main():
    #assert run("tiny.chef") == "Hello world!"
    print(run("run.chef", debug=True))
    #assert run("higher.chef") == "112233445510203040504" # if 50 is added
    #assert run("fruit.chef") == "504"


if __name__ == "__main__":
    main()
