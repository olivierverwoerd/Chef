"""A maybe not so simple chef interpreter made with a functional method"""
import sys
from typing import List, Callable
from chef_token import token
from functions import exe, loop
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
        if len(words) == 1:
            var = ''
        else:
            var = words[1].split()
        new_tokens.append(token(function, var))
        if len(rows) == 0 or rows[1] == '':
            return tokens
        return add_tokens(rows[1], new_tokens)

    return add_tokens(input, [])


# parser (converts [function, [vars] to [function(), [vars]])
def parser(instructions: List, debug: bool = False):
    """
    make tokens of the preproccessed input string
    :param input:
    :return:
    """
    #print(instructions[0].get_variables())
    def replace_name_to_function(instructions: List, new_instructions: List) -> List:
        print(instructions[0].get_function())
        new_instructions.append(token(name_to_function(instructions[0].get_function()), instructions[0].get_variables()))
        if len(instructions) > 1:
            replace_name_to_function(instructions[1:], new_instructions)
        return new_instructions
    return replace_name_to_function(instructions, [])


def run(instructions: List, debug: bool = False):
    state = [{}, [], []]
    if debug:
        print(List)

    def do_function(state: List, instructions: List):
        new_state = exe(state, instructions[0].get_function(), instructions[0].get_variables())
        if len(instructions) > 1:
            do_function(new_state, instructions[1:])

    do_function(state, instructions)

def sub_main(file_name: str) -> str:
    """
    Main opens the file and runs the code directly
    :param file_name: The filename in this directory to run.
    note to self: run(parse(lex(text)))
    """
    print("Running " + file_name)
    print("-------------------------------")

    s = preprocess(file_name, True)
    # lexer [['TITLE', ['hello_world_souffle']], ['INGREDIENTS', ''], ['ADD_INGREDIENT', ['72', 'DRY', 'haricot_beans']], ['ADD_INGREDIENT', ['101', 'DRY', 'eggs']],
    p = parser(lexer(s))
    run(p, debug=True)


def main():
    sub_main("pretest.chef")
    # sub_main("tiny.chef")
    # assert sub_main("tiny.chef") == "Hello world!"
    # assert sub_main("run.chef") == "Hello world!"
    # assert sub_main("higher.chef") == "112233445510203040504" # if 50 is added
    # assert sub_main("fruit.chef") == "504"


if __name__ == "__main__":
    main()
