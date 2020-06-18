
def do_function_to_name_in_list(self, function, name: str, ingredient_list: list, index=None):
    """
    does a function to a list or a specific name
    :param function: labda with values (list, index)
    :param name: Name of the ingredient to edit. and * to apply to all
    :param ingredient_list:
    :param index:
    :return:
    """
    list_len = len(ingredient_list)
    if list_len == 0:
        return None
    if index is None:
        return self.do_function_to_name_in_list(function, name, ingredient_list, list_len - 1)
    if index >= 0:
        if ingredient_list[index].get_name() == name:
            return function(ingredient_list, index)
        if name == '*':
            function(ingredient_list, index)
        return self.do_function_to_name_in_list(function, name, ingredient_list, index - 1)
    else:
        return None


def check_index(self, bowl_or_dish: list, minimum_index: int):
    """
    checks if an index is available and if not. Makes one
    :param bowl_or_dish: what list to check
    :param minimum_index: the index it has to contain.
    :return:
    """
    if len(bowl_or_dish) <= minimum_index:
        bowl_or_dish.append([])
        self.check_index(bowl_or_dish, minimum_index)
    return 0


def get_index(self, name: str, list):
    """
    get's the index of an ingredient from it's name in the ingredient list
    :param name: The name of the ingredient
    :param list: the list where to search for it's index
    :return:
    """
    get_index = lambda list, index: index
    return self.do_function_to_name_in_list(get_index, name, self.ingredients)


def get_amount_of_ingredient(self, name: str):
    """
    :param name: name of the ingredient
    :return: the amount of that ingredient
    """
    return self.ingredients[self.get_index(name, self.ingredients)].get_amount()


def set_amount_of_ingredient(self, name: str, amount: int):
    """
    sets the new amount of that ingredient
    :param name: ingredient name
    :param amount: the new amount of that ingredient
    """
    get_index = lambda list, index: index
    index = self.do_function_to_name_in_list(get_index, name, self.ingredients)
    self.ingredients[index].set_amount(amount)


def add_ingredient(self, ingredient):
    """
    This adds the value of ingredient to the value of the ingredient on top of the nth mixing bowl
    and stores the result in the nth mixing bowl.
    :param ingredient:
    :return:
    """
    get_index = lambda list, index: index
    existing_ingredient = self.do_function_to_name_in_list(get_index, ingredient.get_name(), self.ingredients)
    if not existing_ingredient:
        self.ingredients.append(ingredient)
    else:
        self.ingredients[existing_ingredient] = ingredient  # This is reached by the fold option.


def put_ingredient_into_the_mixing_bowl(self, name: str, mixing_bowl_number: int):
    """
    puts the ingredient it in front of the stack array.insert(0,a)
    :param name: name of ingredient
    :param mixing_bowl_number:
    :return:
    """
    self.check_index(self.mixingbowls, mixing_bowl_number)
    index = self.get_index(name, list)
    if index is not None:
        self.mixingbowls[mixing_bowl_number].insert(0, self.ingredients[index])
    else:
        print("There is no ingredient: " + name + " in the kitchen to put into the mixing bowl")


def fold(self, name: str, mixingbowl: int):
    """
    Opposite of put_ingredient_into_the_mixing_bowl.
    :param name:
    :param mixingbowl:
    :return:
    """
    get_index = lambda list, index: index
    index = self.do_function_to_name_in_list(get_index, name, self.mixingbowls[mixingbowl])
    if index is not None:
        self.add_ingredient(self.mixingbowls[mixingbowl][index])
        del self.mixingbowls[mixingbowl][index]
    else:
        print("There is no ingredient:" + name + " in the mixing bowl to put into the kitchen")


def reduce(self, side: str, name: str, operator: str, mixingbowl: int, index=None, last_value=None):
    """
    a foldl and foldr implementation
    :param side: 'left' or 'right' depending on the fold
    :param name:  the inital value as amount by ingredient name
    :param operator: '+','-','*','/'
    :param mixingbowl: where to apply reduce
    :param index: index to work in.
    :param last_value: the result in the previous recursion
    :return:
    """
    if index == None:
        if name != '':
            index_ingredient = self.get_index(name, self.ingredients)
            last_value = self.ingredients[index_ingredient].get_amount()
        if side == "right":
            self.mixingbowls[mixingbowl].reverse()
        index = len(self.mixingbowls[mixingbowl]) - 1
        return self.reduce(side, name, operator, mixingbowl, index, last_value)

    new_value = 0
    value = self.mixingbowls[mixingbowl][index].get_amount()
    if operator == '+':
        new_value = last_value + value
    elif operator == '-':
        new_value = last_value - value
    elif operator == '*':
        new_value = last_value * value
    elif operator == '/':
        new_value = last_value / value
    if index > 0:
        self.reduce(side, name, operator, mixingbowl, index - 1, new_value)
    else:
        self.mixingbowls[mixingbowl] = [Ingredient(int(new_value), self.mixingbowls[mixingbowl][0].get_state(),
                                                   self.mixingbowls[mixingbowl][0].get_name())]


def zipwith(self, bowl_a: int, bowl_b: int, operator='+', index=None):
    """
    another haskell funtion added on top chef.
    :param bowl_a: index of the first bowl. Values are overided here
    :param bowl_b: index of the second bowl. Does not change
    :param operator:'+','-','*','/'
    :param index: used for recursion
    """
    if index == None:
        if len(self.mixingbowls[bowl_a]) == len(self.mixingbowls[bowl_b]) and (bowl_a != bowl_b):
            self.zipwith(bowl_a, bowl_b, operator, len(self.mixingbowls[bowl_a]) - 1)
        else:
            print("You cant zip with different size mixing bowls")
    elif index >= 0:
        if operator == '+':
            self.mixingbowls[bowl_a][index] = Ingredient(
                int((self.mixingbowls[bowl_a][index].get_amount() + self.mixingbowls[bowl_b][index].get_amount())),
                self.mixingbowls[bowl_a][index].get_state(), self.mixingbowls[bowl_a][index].get_name())
        elif operator == '-':
            self.mixingbowls[bowl_a][index].set_amount(
                self.mixingbowls[bowl_a][index].get_amount() - self.mixingbowls[bowl_b][index].get_amount())
        elif operator == '*':
            self.mixingbowls[bowl_a][index].set_amount(
                self.mixingbowls[bowl_a][index].get_amount() * self.mixingbowls[bowl_b][index].get_amount())
        elif operator == '/':
            self.mixingbowls[bowl_a][index].set_amount(
                self.mixingbowls[bowl_a][index].get_amount() / self.mixingbowls[bowl_b][index].get_amount())
        self.zipwith(bowl_a, bowl_b, operator, index - 1)
    return


def put_mixing_bowl_onto_the_bakingdish(self, mixing_bowl_number: int, bakingdish_number: int):
    """
    This copies all the ingredients from the nth mixing bowl to the pth baking dish,
    retaining the order and putting them on top of anything already in the baking dish.
    :param mixing_bowl_number: index of mixingbowl
    :param bakingdish_number: index of bakingdish
    :return:
    """
    self.check_index(self.mixingbowls, mixing_bowl_number)
    self.check_index(self.bakingdishes, bakingdish_number)
    self.bakingdishes[bakingdish_number] = self.mixingbowls[mixing_bowl_number].copy()


def serve(self, num=0) -> str:
    """
    sends the bakingdish(es) back as a string
    :param num: How many baking dishes are being served
    :return: string
    """
    if num == 0:
        num = len(self.bakingdishes)
    result = ""
    for bakingdish in self.bakingdishes[0:num]:
        for item in bakingdish:
            result += item.serve()
    return result


def liquify(self, name: str):
    """
    This turns the ingredient into a liquid, i.e. a Unicode character for output purposes.
    :param name: name of the ingredient to liquify
    """
    liquify = lambda list, index: list[index].liquefy()
    self.do_function_to_name_in_list(liquify, name, self.ingredients)


def liquify_mixingbowl(self, index: int):
    """
    This turns all the ingredients in the nth mixing bowl into a liquid,
    i.e. a Unicode characters for output purposes.
    :param index: index of the mixingbowl
    """
    liquify = lambda list, index: list[index].liquefy()
    self.do_function_to_name_in_list(liquify, '*', self.mixingbowls[index])


def clean(self, index: int):
    """
    This removes all the ingredients from the nth mixing bowl
    :param index: index of mixing bowl
    """
    self.check_index(self.mixingbowls, index)
    self.mixingbowls[index] = []


def combine(self, name: str, index: int):
    """
    This multiplies the value of ingredient by the value of the ingredient on top of the nth mixing bowl
    and stores the result in the nth mixing bowl.
    :param name: name of the ingredient to take the value
    :param index: mixingbowl index
    """
    index_ingredient = self.get_index(name, self.ingredients)
    self.mixingbowls[index][0].set_amount(self.ingredients[index_ingredient].get_amount() *
                                          self.mixingbowls[index][0].get_amount())


def divide(self, name: str, index: int):
    """
    This divides the value of ingredient into the value of the ingredient on top of the nth mixing bowl
    stores the result in the nth mixing bowl.
    :param name: name of the ingredient to take the value
    :param index: mixingbowl index
    """
    index_ingredient = self.get_index(name, self.ingredients)
    self.mixingbowls[index][0].set_amount(int(self.ingredients[index_ingredient].get_amount() /
                                              self.mixingbowls[index][0].get_amount()))


def add(self, name: str, index: int):
    """
    This adds the value of ingredient to the value of the ingredient on top of the nth mixing bowl
    stores the result in the nth mixing bowl.
    :param name:
    :param index: mixingbowl index
    :return:
    """
    index_ingredient = self.get_index(name, self.ingredients)
    self.mixingbowls[index][0].set_amount(self.ingredients[index_ingredient].get_amount() +
                                          self.mixingbowls[index][0].get_amount())


def remove(self, name: str, index):
    """
    This subtracts the value of ingredient from the value of the ingredient on top of the nth mixing bowl
    stores the result in the nth mixing bowl.
    :param name:
    :param index:
    :return:
    """
    index_ingredient = self.get_index(name, self.ingredients)
    self.mixingbowls[index][0].set_amount(self.ingredients[index_ingredient].get_amount() -
                                          self.mixingbowls[index][0].get_amount())


def add_dry(self, mixingbowl: int, index=None):
    """
    This adds the values of all the dry ingredients together and places the result into the nth mixing bowl.
    :param mixingbowl: mixingbowl index
    :param index:
    :return:
    """
    self.check_index(self.mixingbowls, mixingbowl)
    list_len = len(self.ingredients)
    if list_len == 0:
        return None
    if index is None:
        return self.add_dry(mixingbowl, list_len - 1)
    if index >= 0:
        if self.ingredients[index].get_state() == "dry":
            self.mixingbowls[mixingbowl][0].set_amount(self.ingredients[index].get_amount())
    else:
        return None


def stir(self, mixingbowl: int, amount: int):
    """
    This "rolls" the top number ingredients in the nth mixing bowl,
    such that the top ingredient goes down that number of ingredients and all ingredients above it rise one place.
    If there are not that many ingredients in the bowl, the top ingredient goes to tbe bottom of the bowl and all the others rise one place.
    :param mixingbowl: mixingbowl index
    :param amount: how many times it shoud be stired
    :return:
    """
    self.mixingbowls[mixingbowl].insert(amount, self.mixingbowls[mixingbowl].pop(0))


def stir_ingredient(self, mixingbowl: int, name):
    """
    This rolls the number of ingredients in the nth mixing bowl equal to the value of ingredient,
    such that the top ingredient goes down that number of ingredients and all ingredients above it rise one place.
    If there are not that many ingredients in the bowl,
    the top ingredient goes to the bottom of the bowl and all the others rise one place.
    :param mixingbowl: mixingbowl index
    :param name: name of the ingredient to take the value
    """
    index_ingredient = self.get_index(name, self.ingredients)
    amount = self.ingredients[index_ingredient].get_amount()
    self.stir(mixingbowl, amount)


def mix(self, mixingbowl: int):
    """
    This randomises the order of the ingredients in the nth mixing bowl.
    :param mixingbowl: mixingbowl index
    """
    random.shuffle(self.mixingbowls[mixingbowl])