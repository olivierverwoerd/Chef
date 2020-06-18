from typing import List, Callable


def exe(state, function, varlist: List):
    if len(varlist) == 1:
        return function(state, varlist[0])
    elif len(varlist) == 2:
        return function(state, varlist[0], varlist[1])
    elif len(varlist) == 3:
        return function(state, varlist[0], varlist[1], varlist[2])
    else:
        return "Error: Too many variables"

def ignore(state: List):
    return state
def loop(state: List, functions, amount: int):
    print("-")
def take(state: List, name: str):
    print()
def put(state: List, name: str):
    print()
def fold(state: List, name: str):
    print()
def add(state: List, name: str):
    print()
def remove(state: List, name: str):
    print()
def combine(state: List, name: str):
    print()
def divide(state: List, name: str):
    print()
def add_dry(state: List, name: str):
    print()
def liquify(state: List, name: str):
    print()
def liquify_content(state: List, name: str):
    print()
def stir_for(state: List, name: str):
    print()
def stir(state: List, name: str):
    print()
def mix(state: List, name: str):
    print()
def clean(state: List, name: str):
    print()
def pour(state: List, name: str):
    print()
def loop_start(state: List, name: str):
    print()
def loop_end(state: List, name: str):
    print()
def serve(state: List, name: str):
    print()
def serve_with(state: List, name: str):
    print()
def refrigerate(state: List, name: str):
    print()

