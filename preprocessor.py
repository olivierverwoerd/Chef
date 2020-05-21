import re

def remove_number_extention(line: str) -> str:
    line = line.replace('1st' , '1')
    line = line.replace('2nd' , '2')
    line = line.replace('3rd' , '3')
    line = line.replace('1th' , '1')
    line = line.replace('2th' , '2')
    line = line.replace('3th' , '3')
    line = line.replace('4th' , '4')
    line = line.replace('5th' , '5')
    line = line.replace('6th' , '6')
    line = line.replace('7th' , '7')
    line = line.replace('8th' , '8')
    line = line.replace('9th' , '9')
    line = line.replace('0th' , '0')
    return line

def remove_too_many_spaces(line: str) -> str:
    line = line.replace('    ', ' ')
    line = line.replace('   ', ' ')
    line = line.replace('  ', ' ')
    return line

def preprocess(file: str) -> str:
    liquids = ["dash", "cup", "l", "ml", "dashes", "cups"]
    def loop(file: str, r: str = "", state = "TITLE"):
        tmp = ''
        #spits according to what's nessesary
        if state == "INGREDIENTS":
            tmp = file.split('\n', 1)
        elif state == "METHOD":
            if len(file) == 0:
                return r
            else:
                if file[0] == ' ':
                    file = file[1:]
                tmp = file.split('.', 1)
                tmp[0] = tmp[0].replace('\n', '')
        else:
            tmp = file.split('.', 1)
        line = tmp[0].lower()
        if state == "TITLE" and line != '\n':
            r += "TITLE\n"
            r += line.replace(' ', '_')
            state = "NONE"

        if state == "METHOD":
            line = remove_number_extention(line)
            line = line.replace("the mixing bowl", '0')
            line = line.replace("baking dish", '0')
            line = re.sub(' (hours|hour|contents of|'
                          'from refrigerator|minutes|well|contents of|'
                          'mixing bowl| baking dish|into|the|of |with |for)',
                          ' ', line)
            line = remove_too_many_spaces(line)
            words = line.split(' ', 1)
            print(words)
            r += words[0].upper() + " "
            r += words[1]

        if state == "INGREDIENTS":
            if line == "method.":
                r = r[:-1]
                r += "METHOD"
                state = "METHOD"
            elif line != '': # ignore empty lines
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
            r += "INGREDIENTS"
            state = "INGREDIENTS"
            tmp[1] = tmp[1][1:] # skip last newline
        if len(tmp) == 1: #end of the file
            return r
        else:
            return loop(tmp[1], r + '\n', state)
    return (loop(file))