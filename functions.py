from typing import List, Callable
import random


def check_amount_of_list(state, mixingbowl: int = 1, bakingplate: int = 1):
    while len(state[1]) < mixingbowl + 1:
        state[1].append([])
    while len(state[2]) < bakingplate + 1:
        state[2].append([])
    return state


def get_ingredient_value(state, ingredient: str):
    if ingredient in state[0].keys():
        return state[0][ingredient]
    else:
        raise ValueError("The ingredient: " + ingredient + ", isn't added in ingredients\n" + str(state[0]))


def do_simple_math(state, variables, operator):
    name = str(variables[0])
    mixingbowl = int(variables[1]) - 1
    value = get_ingredient_value(state, name)
    is_char = False
    if type(value) == str:
        value = ord(value)
    if len(state[1]) < mixingbowl or len(state[1][mixingbowl]) == 0:
        return "Unable to preform add with mixingbowl: " + str(mixingbowl + 1)
    old_value = state[1][mixingbowl][0]
    if type(old_value) == str:
        is_char = True
        old_value = ord(old_value)
    if operator == "+":
        value = old_value + value
    if operator == "-":
        value = old_value - value
    if operator == "*":
        value = old_value * value
    if operator == "/":
        value = int(old_value / value)
    if is_char:
        chr(value)
    state[1][mixingbowl][0] = value
    return state


def ignore(state: List, variables: List):
    return state


def execute_list(state: List, functions: List, remaining_times: int):
    """
    Used in loops
    remaining times is also given here to return if a set aside statement is given
    """

    if functions[0] == "ENDLOOP":
        remaining_times = 1
    else:
        exe = functions[0].get_function()
        variables = functions[0].get_variables()
        state = exe(state, variables)
    if type(state) == str:  # error is returned
        raise RuntimeError(state)
    if len(functions) == 1:
        return state, (remaining_times - 1)
    return execute_list(state, functions[1:], remaining_times)


def loop(state: List, variables: List):
    """
    preforms an inner loop
    """
    name = str(variables[0][0])
    functions = variables[1:]
    value = get_ingredient_value(state, name)
    if type(value) == str:
        value = ord(value)

    def execute_loop(state: List, functions: List, remaining_times: int):
        if remaining_times == 0:
            return state
        state, remaining_times = execute_list(state, functions.copy(), remaining_times)
        return execute_loop(state, functions, remaining_times)
    return execute_loop(state, functions, value)


def add_ingredient(state: List, variables: List):
    value = int(variables[0])
    name = str(variables[2])
    if variables[1] == "LIQUID":
        value = chr(value)
    state[0][name] = value
    return state


def take(state: List, variables: List):
    name = str(variables[0])
    value = int(input("How much " + name + "shall we add?: "))
    state[0][name] = value
    return state


def put(state: List, variables: List):
    name = str(variables[0])
    mixingbowl = int(variables[1])-1
    value = get_ingredient_value(state, name)
    state = check_amount_of_list(state, mixingbowl)
    state[1][mixingbowl].insert(0,value)
    return state


# Not a haskell fold.
def fold(state: List, variables: List):
    name = str(variables[0])
    mixingbowl = int(variables[1])-1
    if len(state[1]) < mixingbowl or len(state[1][mixingbowl]) == 0:
        return "Unable to preform fold with mixingbowl: " + str(mixingbowl+1)
    state[0][name] = state[1][mixingbowl][0]
    return state


def add(state: List, variables: List):
    return do_simple_math(state, variables, "+")


def remove(state: List, variables: List):
    return do_simple_math(state, variables, "-")


def combine(state: List, variables: List):
    return do_simple_math(state, variables, "*")


def divide(state: List, variables: List):
    return do_simple_math(state, variables, "/")


def add_drys(state: List, variables: List, values = None):
    if values == None:
        mixingbowl = int(variables[0]) - 1
        values = list(state[0].values())
        if len(values) == 0:
            return state
        state = check_amount_of_list(state, mixingbowl)
        return add_drys(state, variables, values)
    if type(values[0]) == int:
        state[1][int(variables[0])-1].append(values[0])
    if len(values) == 1:
        return state
    return add_drys(state, variables, values[1:])


def liquefy(state: List, variables: List):
    name = str(variables[0])
    value = get_ingredient_value(state, name)
    if type(value) != str:
        state[0][name] = chr(value)
    return state


def liquefy_contents(state: List, variables: List, values = None):
    mixingbowl = int(variables[0]) - 1
    if values is None:
        state = check_amount_of_list(state, mixingbowl)
        if len(state[1][mixingbowl]) == 0:
            return state
        values = state[1][mixingbowl].copy()
        state[1][mixingbowl].clear()
        return liquefy_contents(state, variables, values)
    if type(values[0]) == str:
        state[1][mixingbowl].append(values[0])
    else:
        state[1][mixingbowl].append(chr(values[0]))
    if len(values) == 1:
        return state
    return liquefy_contents(state, variables, values[1:])


def stir_for(state: List, variables: List):
    mixingbowl = int(variables[0])-1
    state = check_amount_of_list(state, mixingbowl)
    if len(state[1][mixingbowl]) < 2:
        return state
    amount = int(variables[1])
    if amount > len(state[1][mixingbowl]):
        amount = len(state[1][mixingbowl])-1
    state[1][mixingbowl].insert(amount, state[1][mixingbowl].pop(0))
    return state


def stir(state: List, variables: List):
    name = str(variables[0])
    value = get_ingredient_value(state, name)
    if type(value) == str:
        value = ord(value)
    variables[1] = value
    return stir_for(state, variables)


def mix(state: List, variables: List):
    mixingbowl = int(variables[0])-1
    state = check_amount_of_list(state, mixingbowl)
    random.shuffle(state[1][mixingbowl])
    return state


def clean(state: List, variables: List):
    mixingbowl = int(variables[0])-1
    state = check_amount_of_list(state, mixingbowl)
    state[1][mixingbowl].clear()
    return state


def pour(state: List, variables: List):
    mixingbowl = int(variables[0])-1
    bakingplate = int(variables[1])-1
    state = check_amount_of_list(state, mixingbowl, bakingplate)
    mixing = state[1][mixingbowl]
    new_plate = mixing.copy()
    new_plate.extend(state[2][bakingplate])
    state[2][bakingplate] = new_plate
    return state


# higher order extra's all
def zipwith(state: List, variables: List):
    mixingbowl_1 = int(variables[0])-1
    operator = variables[1]
    mixingbowl_2 = int(variables[2])-1
    if operator == 'out':
        state[1][mixingbowl_1] = list(map(lambda a, b: a - b, state[1][mixingbowl_1], state[1][mixingbowl_2]))
    elif operator == 'times':
        state[1][mixingbowl_1] = list(map(lambda a, b: a * b, state[1][mixingbowl_1], state[1][mixingbowl_2]))
    elif operator == 'divide':
        state[1][mixingbowl_1] = list(map(lambda a, b: a / b, state[1][mixingbowl_1], state[1][mixingbowl_2]))
    else: #add
        state[1][mixingbowl_1] = list(map(lambda a, b: a + b, state[1][mixingbowl_1], state[1][mixingbowl_2]))
    return state

def foldl(state: List, variables: List):
    name = str(variables[0])
    value = get_ingredient_value(state, name)
    function = variables[1]
    mixingbowl = int(variables[2])-1

    def haskell_loop(function: str, start_number: int, list: List):
        if len(list) == 0:
            return start_number
        if len(list) == 1:
            if function == 'out':
                return start_number - list[0]
            elif function == 'times':
                return start_number * list[0]
            elif function == 'halve':
                return start_number / list[0]
            else: # in
                return start_number + list[0]
        else:
            if function == 'out':
                return haskell_loop(function, start_number, list[:-1]) - list[-1]
            elif function == 'times':
                return haskell_loop(function, start_number, list[:-1]) * list[-1]
            elif function == 'halve':
                return haskell_loop(function, start_number, list[:-1]) / list[-1]
            else:  # in
                return haskell_loop(function, start_number, list[:-1]) + list[-1]
    state[1][mixingbowl] = [int(haskell_loop(function, value, state[1][mixingbowl]))]
    return state


def foldr(state: List, variables: List):
    name = str(variables[0])
    value = get_ingredient_value(state, name)
    function = variables[1]
    mixingbowl = int(variables[2])-1

    def haskell_loop(function: str, start_number: int, list: List):
        if len(list) == 0:
            return start_number
        if len(list) == 1:
            if function == 'out':
                return list[0] - start_number
            elif function == 'times':
                return list[0] * start_number
            elif function == 'halve':
                return list[0] / start_number
            else:  # in
                return list[0] + start_number
        else:
            if function == 'out':
                return list[0] - haskell_loop(function, start_number, list[1:])
            elif function == 'times':
                return list[0] * haskell_loop(function, start_number, list[1:])
            elif function == 'halve':
                return list[0] / haskell_loop(function, start_number, list[1:])
            else:  # in
                return list[0] + haskell_loop(function, start_number, list[1:])
    state[1][mixingbowl] = [int(haskell_loop(function, value, state[1][mixingbowl]))]
    return state


def serve(state: List, variables: List):
    bakingplate = int(variables[0])-1
    state = check_amount_of_list(state, bakingplate=bakingplate)
    output = state[2][bakingplate]
    print(''.join(map(str, output)), end='')
    return state


def refrigerate(state: List, variables: List):
    return serve(state, ['1'])

