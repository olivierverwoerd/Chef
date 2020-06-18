from functions import exe, loop, take, put, fold, add, remove, combine, divide, add_dry, liquify, liquify_content, \
    stir_for, stir, mix, clean, pour, loop_start, loop_end, serve, serve_with, refrigerate, ignore


def name_to_function(name: str):
    if name == "TITLE" or name == "INGREDIENTS" or name == "TITLE":
        return ignore
    elif name == "TAKE":
        return take
    elif name == "PUT":
        return put
    elif name == "FOLD":
        return fold
    elif name == "ADD":
        return add
    elif name == "REMOVE":
        return remove
    elif name == "COMBINE":
        return combine
    elif name == "DIVIDE":
        return divide
    elif name == "ADD_DRY":
        return add_dry
    elif name == "LIQUIFY":
        return liquify
    elif name == "LIQUIFY_CONTENT":
        return liquify_content
    elif name == "STIR_FOR":
        return stir_for
    elif name == "STIR":
        return stir
    elif name == "MIX":
        return mix
    elif name == "CLEAN":
        return clean
    elif name == "POUR":
        return pour
    elif name == "LOOP_START":
        return loop_start
    elif name == "LOOP_END":
        return loop_end
    elif name == "SERVE":
        return serve
    elif name == "SERVE_WITH":
        return serve_with
    elif name == "REFRIGERATE":
        return refrigerate
    else:
        raise Exception("ERROR " + name + ", Isn't a valid function")
