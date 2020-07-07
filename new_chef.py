"""A maybe not so simple chef interpreter made with a functional method"""
import sys
from typing import List, Callable
from chef_token import token
from functions import loop
from name_to_function import name_to_function
from preprocessor import preprocess


# lexer (converts string to [function, [vars]])
def lexer(input: str) -> List[str]:
    """
    make tokens of the preproccessed input string
    :param input:
    :return:
    """

    def add_tokens(input: str, tokens: List) -> List[str]:
        new_tokens = tokens.copy()
        rows = input.split('\n', 1)
        words = rows[0].split(' ', 1)
        function = words[0]
        if function != '':
            if len(words) == 1:
                var = ''
            else:
                var = words[1].split()
            new_tokens.append(token(function, var))
        if len(rows) == 1:
            return new_tokens
        return add_tokens(rows[1], new_tokens)

    return add_tokens(input, [])


# parser (converts [function, [vars] to [function(), [vars]])
def parser(instructions: List):
    """
    make tokens of the preproccessed input string
    :param input:
    :return:
    """
    def replace_name_to_function(instructions: List, new_instructions: List, loops: List = []) -> List:
        # print(instructions)
        inst = name_to_function(instructions[0].get_function())
        if loops != [] and type(inst) != str:
            loops[-1].append(token(inst, instructions[0].get_variables()))
            return replace_name_to_function(instructions[1:], new_instructions, loops)
        if type(inst) == str:
            if inst == "loop_start":
                # in a lot of code the loop is just for the layout for the recipe and is non functional.
                if instructions[1].get_function() == "LOOP_END":
                    return replace_name_to_function(instructions[2:], new_instructions, loops)
                loops.append([instructions[0].get_variables()])
                return replace_name_to_function(instructions[1:], new_instructions, loops)
            if inst == "ENDLOOP":
                loops[-1].append("ENDLOOP")
                return replace_name_to_function(instructions[1:], new_instructions, loops)
            if inst == "loop_end":
                if loops == []:
                    raise ValueError("Loop ended without start")
                if len(loops) > 1:
                    loops[len(loops)-2].append(token(loop, loops.pop(-1)))
                    return replace_name_to_function(instructions, new_instructions, loops)
                else:
                    new_instructions.append(token(loop, loops.pop(-1)))
        else:
            new_instructions.append(token(inst, instructions[0].get_variables()))
        if len(instructions) > 1:
            replace_name_to_function(instructions[1:], new_instructions)
        return new_instructions
    return replace_name_to_function(instructions, [])


def run(instructions: List, debug: bool = False):
    state = [{}, [], []]
    if debug:
        print(List)

    def do_function(state: List, instructions: List):
        exe = instructions[0].get_function()
        variables = instructions[0].get_variables()
        if debug:
            print("State is now: " + str(state[0]) + "\n" + str(state[1]) + "\n" + str(state[2]))
            print("Calling" + str(exe) + " with vars: " + str(variables))
        new_state = exe(state, variables)
        if type(new_state) == str:  #error is returned
            raise RuntimeError(new_state)
        if len(instructions) > 1:
            do_function(new_state, instructions[1:])
    do_function(state, instructions)


def sub_main(file_name: str) -> str:
    """
    Main opens the file and runs the code directly
    :param file_name: The filename in this directory to run.
    note to self: run(parse(lex(text)))
    """
    print("\n\nRunning " + file_name)
    print("-------------------------------")

    s = preprocess(file_name, keep_file=True)
    run(parser(lexer(s)), debug=True)


def main():
    # sub_main("pretest.chef")
    # sub_main("tiny.chef")
    sub_main("run.chef")
    sub_main("higher.chef")
    sub_main("fruit.chef")


if __name__ == "__main__":
    main()
