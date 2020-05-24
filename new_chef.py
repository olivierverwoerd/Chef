"""A maybe not so simple chef interpreter made with a functional method"""
import sys
from typing import List, Callable
from preprocessor import preprocess
from lexer import lexer


def token_topping(file: str) -> List[str]:
    input = file.split('\n')
    tokens = ['NAME']
    def add_tokens(input: str, tokens: List[str]) -> List[str]:
        new_tokens = tokens.copy()

    return add_tokens(input, tokens)

def sub_main(file_name: str) -> str:
    """
    Main opens the file and runs the code directly
    :param file_name: The filename in this directory to run.

    note to self: run(parse(lex(text)))
    """
    print("Running " + file_name)
    print("-------------------------------")
    f = open(file_name, "r")
    recipe = f.read()
    s = preprocess(recipe)
    sf = open(file_name + ".ppf", "w")
    sf.write(s)
    sf.close()
    #print(token_topping(recipe))



def main():
    sub_main("pretest.chef")
    # sub_main("tiny.chef")
    #assert sub_main("tiny.chef") == "Hello world!"
    #assert sub_main("run.chef") == "Hello world!"
    #assert sub_main("higher.chef") == "112233445510203040504" # if 50 is added
    #assert sub_main("fruit.chef") == "504"


if __name__ == "__main__":
    main()
