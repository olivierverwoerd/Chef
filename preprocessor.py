import re
import sys

def remove_number_extention(line: str) -> str:
    line = line.replace('1st', '1')
    line = line.replace('2nd', '2')
    line = line.replace('3rd', '3')
    line = line.replace('1th', '1')
    line = line.replace('2th', '2')
    line = line.replace('3th', '3')
    line = line.replace('4th', '4')
    line = line.replace('5th', '5')
    line = line.replace('6th', '6')
    line = line.replace('7th', '7')
    line = line.replace('8th', '8')
    line = line.replace('9th', '9')
    line = line.replace('0th', '0')
    return line


def remove_too_many_spaces(line: str) -> str:
    line = line.replace('    ', ' ')
    line = line.replace('   ', ' ')
    line = line.replace('  ', ' ')
    return line


def preprocess(file_name: str, keep_file: bool) -> str:
    liquids = ["dash", "cup", "l", "ml", "dashes", "cups"]
    commands = ["put","liquefy","pour","fold","add","remove","combine","divide","stir","mix",
             "clean","pour","set","refrigerate","serve","serves","take", "zipwith", "foldl", "foldr"]
    commands_with_double_values = ["zipwith", "pour", "foldl", "foldr"]
    f = open(file_name, "r")
    file = f.read()
    f.close()

    def loop(file: str, r: str = "", state="TITLE"):
        tmp = ''
        #spits according to what's nessesary
        if state == "INGREDIENTS":
            tmp = file.split('\n', 1)
        elif state == "METHOD":
            if len(file) == 0:
                if keep_file:
                    sf = open(file_name + ".ppf", "w")
                    sf.write(r)
                    sf.close()
                return r
            else:
                if file[0] == ' ':
                    file = file[1:]
                tmp = file.split('.', 1)
                tmp[0] = tmp[0].replace('\n', '')
        else:
            tmp = file.split('.', 1)
        line = tmp[0].lower()
        if state == "TITLE":
            if r[-1:] == '\n':
                r = r[:-2]
            if line != '\n':
                if len(line) != 0:
                    r += "TITLE "
                    name = line.replace('\n', '')
                    r += name.replace(' ', '_')
                    state = "NONE"


        if state == "METHOD":
            line = remove_number_extention(line)
            line = line.replace("the mixing bowl", '1')
            line = line.replace("the baking dish", '1')
            words = line.split(' ')
            line = re.sub(' (hours|hour|contents of|to|'
                          'from|minutes|minute|well|contents of|refrigerator|and|the|of |with |for|'
                          'mixing bowl|baking dish|into)',
                          ' ', line)
            line = remove_too_many_spaces(line)
            word = line.split(' ', 1)
            if word[1][-1] == ' ':
                word[1] = word[1][:-1]
            if words[0] not in commands and words[0] != '\n':
                if words[-2] == "until":
                    r += "LOOP_END "
                    r += word[1].split(" until")[0].replace(" ", "_")
                elif words[1] == "the":
                    r += "LOOP_START "
                    r += word[1].replace(' ', '_')
                else:
                    raise Exception("PREPROCESSOR ERROR:" + str(words))
            else:
                if words[0] == 'liquefy':
                    if words[1] == "contents":
                        r += "LIQUEFY_CONTENTS "
                        r += word[1]
                    else:
                        r += "LIQUEFY " + word[1].replace(' ', '_')
                elif words[0] == 'add' and words[1] == "dry":
                    r += "ADD_DRYS " + words[4]
                elif words[0] == 'stir' and words[-3] == "for":
                    r += "STIR_FOR " + word[1]
                elif words[0] == 'set' and words[1] == "aside":
                    r += "ENDLOOP"
                elif words[0] == "take":
                    r += "TAKE " + word[1].replace(' ', '_')
                elif words[0] == "serve" or words[0] == "serves":
                    if words[1] == "with":
                        r += "SERVE_WITH " + word[1].replace(' ', '_')
                        r += '\n'
                        state = "TITLE"
                    else:
                        r += 'SERVES ' + word[1] + '\n'
                        state = "TITLE"
                else:
                    r += word[0].upper() + " "
                    if word[0] in commands_with_double_values:
                        r += word[1]
                    else:
                        r += word[1].replace(' ', '_', len(word[1].split(' '))-2)


        if state == "INGREDIENTS":
            if line == "method.":
                r = r[:-1]
                r += "METHOD"
                state = "METHOD"
            elif line != '' and line[:12] != "cooking time" and line[:8] != "pre-heat": # ignore empty lines
                l = line.split(' ')
                type = ''
                name = ''
                if len(l) < 3:
                    type = " DRY "
                    name += l[1]
                else:
                    if l[1] in liquids:
                        type = " LIQUID "
                    else:
                        type = " DRY "
                    name += line.split(' ', 2)[2].replace(' ', '_')
                r += "ADD_INGREDIENT "
                r += l[0]
                r += type
                r += name
        if line == "\n\ningredients":
            r = r[:-2]
            r += "\nINGREDIENTS"
            state = "INGREDIENTS"
            tmp[1] = tmp[1][1:] # skip last newline
        if len(tmp) == 1: #end of the file
            if keep_file:
                sf = open(file_name + ".ppf", "w")
                sf.write(r)
                sf.close()
            return r
        else:
            if r != '':
                r += '\n'
            return loop(tmp[1], r, state)
    return loop(file)