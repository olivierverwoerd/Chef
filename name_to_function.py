from functions import take, put, fold, add, remove, combine, divide, add_drys, liquefy, liquefy_contents, \
    stir_for, stir, mix, clean, pour, serve, refrigerate, ignore, add_ingredient, \
    zipwith, foldl, foldr


def name_to_function(name: str):
    if name == "TITLE" or name == "INGREDIENTS" or name == "METHOD":
        return ignore
    elif name == "ADD_INGREDIENT":
        return add_ingredient
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
    elif name == "ADD_DRYS":
        return add_drys
    elif name == "LIQUEFY":
        return liquefy
    elif name == "LIQUEFY_CONTENTS":
        return liquefy_contents
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
    elif name == "ZIPWITH":
        return zipwith
    elif name == "FOLDL":
        return foldl
    elif name == "FOLDR":
        return foldr
    elif name == "LOOP_START":
        return "loop_start"
    elif name == "LOOP_END":
        return "loop_end"
    elif name == "ENDLOOP":
        return "ENDLOOP"
    elif name == "SERVES":
        return serve
    elif name == "SERVE_WITH":
        return "serve_with"
    elif name == "REFRIGERATE":
        return refrigerate
    else:
        raise Exception("ERROR " + name + ", Isn't a valid function")
