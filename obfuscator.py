# -*- coding utf-8 -*-

from random import randint
import re
import os
from typing import Tuple

message = '''
#==========Py_for_Py_obfuscation==========#
#  version: 1 (-alfa-)                    #
#  author: me                             #
#=========================================#
.
.
.
terms of use:
-do not duplicate names in\out function\class body. that may cause ERRORS
-do not use obfuscation more that one time, that may and should cause ERRORS
-try to avoid obfuscating large amount of code, better to split it on parts
-do not expect much, this is just a try ;)
.
.
.
using:
-enter full path to the file -> '''
file = input(message)
search = re.search(r'.*[\\/](.+)\.py', file)
fileName = search.group(1) if search is not None else file

message = '''-enter length of "new" names of variables -> '''
length = int(input(message))

message = '''-obfuscate constants?[y\\n] -> '''
constObf = input(message)

fileText = open(file, 'r+', encoding='utf-8').readlines()

comment_section = False                                                                         #
funcLevel = False                                                                               # useful flags
classLevel = False                                                                              #
                                                                                                # RegEx to find in text:
varFind = r'\s*(\D*\w+?)\s*?=\s*.+|return\s+(.+)|\s*(\w+?)\.'                                   # -variables
longVarFind = r'\D*\w+\s*?\+?=\s*?({})|return\s+({})|\b({})\s*?\+?=\s*?\D*\w+|\s*\b({})[[(]*?'  # -current variables

classFind = r'=\s*?({})|({})\.|\b({})'                                                          # -names of classes
funcFind = r'=\s*?({})|\b({})\b'                                                                # -names of functions
classFuncFind = r'(class|def) (\b\w+)\(*.*?\)*:'                                                # -start of func\class

constFind = r'(\w+)\s*?=\s*?(\d+)'                                                              # -num constants
importFind = r'\s*import\s+(\w+)'                                                               # -module imports
importNameFind = r'\s*?\b(randint)[\.(]'                                                        # -names of module

selfFind = r'\b{}\.(\D\w*?)\s*?=\s*?\w+|\b{}\.(\D\w*)\s*?'                                      # -self attributes

letters = 'lo01'                                                                                # basic letters for names

globalNames = {'classes': {}, 'functions': {}, 'vars': {'global': {}, 'enclosing': {}}, 'imports': {}}


def commentDelete(stroke) -> str:
    """deletes comments like #this or current in every stroke"""
    global comment_section

    result_stroke = ''
    if comment_section:
        if stroke.strip().startswith("'''") or stroke.strip().startswith('"""'):
            comment_section = False
        else:
            return result_stroke

    if stroke.strip().startswith("'''"):
        if stroke.strip().endswith("'''"):
            pass
        else:
            comment_section = True
        return result_stroke

    if stroke.strip().startswith('"""'):
        if stroke.strip().endswith('"""'):
            pass
        else:
            comment_section = True
        return result_stroke

    for symbol in stroke:
        if symbol != '#':
            result_stroke += symbol
        else:
            break

    return result_stroke.rstrip()


startName = 'l01ol1lo1ll1ol1ol1010ol1o01lo01lo01lo1l01l01'


def nameGen() -> str:
    """generates name of given length"""

    name = startName[:]
    for _ in range(length):
        name += letters[randint(0, len(letters) - 1)]
    name += 'l01ol1lo1ll1ol1ol1010ol1o01lo01lo01lo1l01l01'
    return name


globalNames['self'] = nameGen()


def createNumFunc(num, isPositive=None) -> Tuple[str, str]:
    """creates function for reflection of a number"""
    names = []

    for _ in range(100):
        names.append(nameGen())
    return (f'''
def {names[0]}():
    {names[1]}={str(['dI3453KcUN245625(*&(%*LKSHF(W%SaS12352kjalsdjf3487SFH&$#LSGLKSJT($#%(SDGLSKJSTsfhjsljt3845ysdlh3563453kjfISHFSHF*^$SHFI@#$*@#&^%$SHOSAFhq3859467ghqk39834S!@#$%^&*('] * num)} 
    {names[4]},{names[3]},{names[2]} = {names[1]},[sdflkjljSDFKJSDLKJYHRKJSLFHLSKDJFjlsdkfhslhsdf for sdflkjljSDFKJSDLKJYHRKJSLFHLSKDJFjlsdkfhslhsdf in {names[1]}], len({names[1]}) * 1024 
    {names[5]}='{names[5] * 4}'
    {names[69]}={isPositive}
    {names[3]},{names[5]},{names[2]},{names[4]}=[(k,v) for k,v in enumerate({names[5]})],{names[5]},{names[2]}*len({names[5]}),{names[4]} 
    {names[6]}=100000000/10000000
    {names[23]}={[5]}*len({names[1]})
    {names[34]},{names[35]},{names[41]},{names[39]},{names[30]},{names[67]}={names[23]},{names[23]},{names[23]},{names[23]},{names[23]},{names[23]}
    {names[41]},{names[39]},{names[34]},{names[35]},{names[67]},{names[30]}={names[67]},{names[39]},{names[35]},{names[34]},{names[30]},{names[41]}
    if len({names[34]})==len({names[35]})-23:
        return {names[35]}
    if len({names[41]})==len({names[39]})-23:
        return {names[39]}
    if len({names[1]}) <= 0:
        return len({names[1]})
    if len({names[30]})==len({names[67]})-23:
        return {names[30]}
    if not {names[69]}:
        return int('-' + len({names[1]}))
    {names[7]}=int(len({names[5]})*(2**{names[6]}))
    if len({names[1]})==len({names[5]}) - 54:
        return {names[4]}
    elif {names[3]}=={names[4]}:
        return {names[7]}*len({names[5]})
    elif {names[1]}=={names[5]}:
        return {names[4]}
    elif len({names[1]})==int({names[2]}/{names[7]}):
        return int({names[2]}/{names[7]})
    else:
        pass
''', names[0])


fileName = re.sub(r'.py', '', fileName)
constFile = open('{}.py'.format(fileName + '_obfuscated'), 'w', encoding='utf-8')
newFile = open('someFile.py', 'w', encoding='utf-8')

for stroke in fileText:  # parse strokes
    clear_stroke = commentDelete(stroke)  # clear from comments

    if clear_stroke:

        search = re.search(r'(\\t)+', repr(clear_stroke))  #
        #
        if search is not None:  # change \t to 4 spaces
            count = search.group().count('\\t')  #
            clear_stroke = re.sub(f'{search.group()}', '    ' * count, clear_stroke)  #

        if 'self.' in clear_stroke or '(self)' in clear_stroke:  # ruins 'self'
            clear_stroke = re.sub('self', f'{globalNames["self"]}', clear_stroke)  # doesnt make sense but why not

        current_stroke = clear_stroke.split(' ')  #
        level = current_stroke.count('')  # to count indents

        if funcLevel or classLevel:  #
            if level < 4:  # check the func\class level
                funcLevel, classLevel = False, False  #

        # this finds constants in line and subs it to function call ===================================================#

        if constObf == 'y':

            search = re.search(constFind, clear_stroke)

            if search is not None:

                number = int(search.group(2))

                newName = nameGen()

                if level >= 4 and funcLevel:
                    if search.group(2) not in globalNames['vars']['enclosing'].keys():
                        globalNames['vars']['enclosing'][search.group(1)] = {'newName': newName, 'level': level}
                else:
                    if search.group(2) not in globalNames['vars']['global'].keys():
                        globalNames['vars']['global'][search.group(1)] = {'newName': newName, 'level': level}

                if number >= 11:

                    number_1, number_2 = createNumFunc(number - (number % 10), True), createNumFunc(number % 10, True)
                    constFile.write(f'''
                    {number_1[0]}
                    {number_2[0]}
''')
                    clear_stroke = f'''{' ' * level}{newName}={number_1[1]}()+{number_2[1]}()'''
                    newFile.write(clear_stroke + '\n')
                    continue

                elif 0 <= number <= 10:

                    number = createNumFunc(number, True)
                    constFile.write(f'''{number[0]}''')
                    clear_stroke = f'''{' ' * level}{newName}={number[1]}()'''
                    newFile.write(clear_stroke + '\n')
                    continue

                else:

                    number = createNumFunc(int(re.sub('-', '', str(number))), False)
                    constFile.write(f'''{number[0]}''')
                    clear_stroke = f'''{' ' * level}{newName}={number[1]}()'''
                    newFile.write(clear_stroke + '\n')

        else:
            pass

        # =============================================================================================================#
        #                                                                                                              #
        # this find self. attributes                                                                                   #
        #                                                                                                              #
        # =============================================================================================================#

        for key in globalNames['imports'].keys():

            search = re.search(importNameFind, clear_stroke)

            if search is not None:
                clear_stroke = re.sub(f'{key}', globalNames['imports'][key], clear_stroke)

        search = re.search(importFind, clear_stroke)

        if search is not None and search.group(1) is not None:
            newName = nameGen()
            globalNames['imports'][search.group(1)] = newName
            clear_stroke += f' as {newName}'

        # =============================================================================================================#
        #                                                                                                              #
        # this finds declarations of classes or functions                                                              #                                                                                                           #
        #                                                                                                              #
        # =============================================================================================================#

        search = re.search(classFuncFind, clear_stroke)

        if search is not None and search.group(1) == 'class':

            classLevel = True

            newName = nameGen()
            if search.group(2) not in globalNames['classes'].keys():
                globalNames['classes'][search.group(2)] = newName

            clear_stroke = re.sub(f'{search.group(2)}', newName, clear_stroke)

        elif search is not None and search.group(1) == 'def':

            funcLevel = True

            if not search.group(2).startswith('__') and not search.group(1).startswith('_'):

                newName = nameGen()
                if search.group(2) not in globalNames['functions'].keys():
                    globalNames['functions'][search.group(2)] = {'newName': newName, 'level': level}

                clear_stroke = re.sub(f'{search.group(2)}', newName, clear_stroke)

        # =============================================================================================================#
        #                                                                                                              #
        # this find global\enclosing variables in stroke and subs them                                                 #
        #                                                                                                              #
        # =============================================================================================================#

        for variable in globalNames['vars']['enclosing'].keys():

            search = re.search(fr'\.{variable}', clear_stroke)

            if search is not None and level >= 4:
                clear_stroke = re.sub(f'{variable}', globalNames['vars']['enclosing'][variable]['newName'],
                                      clear_stroke)

            search = re.search(longVarFind.format(variable, variable, variable, variable), clear_stroke)

            if search is not None and level >= globalNames['vars']['enclosing'][variable]['level']:
                clear_stroke = re.sub(f'{variable}', globalNames['vars']['enclosing'][variable]['newName'],
                                      clear_stroke)

            if search is not None and search.group(2) is not None and level >= \
                    globalNames['vars']['enclosing'][variable]['level']:
                clear_stroke = re.sub(f'{variable}', globalNames['vars']['enclosing'][variable]['newName'],
                                      clear_stroke)

            if search is not None and search.group(3) is not None and level >= \
                    globalNames['vars']['enclosing'][variable]['level']:
                clear_stroke = re.sub(f'{variable}', globalNames['vars']['enclosing'][variable]['newName'],
                                      clear_stroke)

            if search is not None and search.group(4) is not None and level >= \
                    globalNames['vars']['enclosing'][variable]['level']:
                clear_stroke = re.sub(f'{variable}', globalNames['vars']['enclosing'][variable]['newName'],
                                      clear_stroke)

        for variable in globalNames['vars']['global'].keys():

            search = re.search(longVarFind.format(variable, variable, variable, variable), clear_stroke)

            if search is not None and search.group(1) is not None:
                clear_stroke = re.sub(f'{variable}', globalNames['vars']['global'][variable]['newName'],
                                      clear_stroke)

            if search is not None and search.group(2) is not None:
                clear_stroke = re.sub(f'{variable}', globalNames['vars']['global'][variable]['newName'],
                                      clear_stroke)

            if search is not None and search.group(3) is not None:
                clear_stroke = re.sub(f'{variable}', globalNames['vars']['global'][variable]['newName'],
                                      clear_stroke)

            if search is not None and search.group(4) is not None:
                clear_stroke = re.sub(f'{variable}', globalNames['vars']['global'][variable]['newName'],
                                      clear_stroke)

        # =============================================================================================================#
        #                                                                                                              #
        # this finds names of classes\functions in test and subs them                                                  #
        #                                                                                                              #
        # =============================================================================================================#

        for key in globalNames['classes'].keys():
            search = re.search(classFind.format(key, key, key), clear_stroke)

            if search is not None and search.group(1) is not None:
                clear_stroke = re.sub(f'{key}', f'{globalNames["classes"][key]}', clear_stroke)

            if search is not None and search.group(2) is not None:
                clear_stroke = re.sub(f'{key}', f'{globalNames["classes"][key]}', clear_stroke)

            if search is not None and search.group(3) is not None:
                clear_stroke = re.sub(f'{key}', f'{globalNames["classes"][key]}', clear_stroke)

        for key in globalNames['functions'].keys():
            search = re.search(funcFind.format(key, key), clear_stroke)

            if search is not None and search.group(1) is not None:
                clear_stroke = re.sub(f'{key}', f'{globalNames["functions"][key]["newName"]}', clear_stroke)

            if search is not None and search.group(2) is not None:
                clear_stroke = re.sub(f'{key}', f'{globalNames["functions"][key]["newName"]}', clear_stroke)

        # =============================================================================================================#
        #                                                                                                              #
        # this tracks remaining names of variables due to their level
        #                                                                                                              #
        # =============================================================================================================#

        search = re.search(varFind, clear_stroke)
        if search is not None:

            if funcLevel:

                if search.group(1) is not None and \
                        search.group(1) not in globalNames['vars']['enclosing'].keys() and \
                        search.group(1) not in globalNames['vars']['global'].keys() and not search.group(1).startswith(
                    startName):
                    newName = nameGen()
                    globalNames['vars']['enclosing'][search.group(1)] = {'newName': newName, 'level': level}
                    clear_stroke = re.sub(f'{search.group(1)}', newName, clear_stroke)

                if search.group(2) is not None and \
                        search.group(2) not in globalNames['vars']['enclosing'].keys() and \
                        search.group(2) not in globalNames['vars']['global'].keys() and not search.group(2).startswith(
                    startName):
                    newName = nameGen()
                    globalNames['vars']['enclosing'][search.group(2)] = {'newName': newName, 'level': level}
                    clear_stroke = re.sub(f'{search.group(2)}', newName, clear_stroke)

                if search.group(3) is not None and \
                        search.group(3) not in globalNames['vars']['enclosing'].keys() and \
                        search.group(3) not in globalNames['vars']['global'].keys() and not search.group(3).startswith(
                    startName):
                    newName = nameGen()
                    globalNames['vars']['enclosing'][search.group(3)] = {'newName': newName, 'level': level}
                    clear_stroke = re.sub(f'{search.group(3)}', newName, clear_stroke)

            elif classLevel:

                if search.group(1) is not None and \
                        search.group(1) not in globalNames['vars']['enclosing'].keys() and \
                        search.group(1) not in globalNames['vars']['global'].keys() and not search.group(1).startswith(
                    startName):
                    newName = nameGen()
                    globalNames['vars']['global'][search.group(1)] = {'newName': newName, 'level': level}
                    clear_stroke = re.sub(f'{search.group(1)}', newName, clear_stroke)

                if search.group(2) is not None and \
                        search.group(2) not in globalNames['vars']['enclosing'].keys() and \
                        search.group(2) not in globalNames['vars']['global'].keys() and not search.group(2).startswith(
                    startName):
                    newName = nameGen()
                    globalNames['vars']['global'][search.group(2)] = {'newName': newName, 'level': level}
                    clear_stroke = re.sub(f'{search.group(2)}', newName, clear_stroke)

                if search.group(3) is not None and \
                        search.group(3) not in globalNames['vars']['enclosing'].keys() and \
                        search.group(3) not in globalNames['vars']['global'].keys() and not search.group(3).startswith(
                    startName):
                    newName = nameGen()
                    globalNames['vars']['global'][search.group(3)] = {'newName': newName, 'level': level}
                    clear_stroke = re.sub(f'{search.group(3)}', newName, clear_stroke)

            else:

                if search.group(1) is not None and \
                        search.group(1) not in globalNames['vars']['global'].keys() and not search.group(1).startswith(
                    startName):
                    newName = nameGen()
                    globalNames['vars']['global'][search.group(1)] = {'newName': newName, 'level': level}
                    clear_stroke = re.sub(f'{search.group(1)}', newName, clear_stroke)

                if search.group(2) is not None and \
                        search.group(2) not in globalNames['vars']['global'].keys() and not search.group(2).startswith(
                    startName):
                    newName = nameGen()
                    globalNames['vars']['global'][search.group(2)] = {'newName': newName, 'level': level}
                    clear_stroke = re.sub(f'{search.group(2)}', newName, clear_stroke)

                if search.group(3) is not None and \
                        search.group(3) not in globalNames['vars']['global'].keys() and not search.group(3).startswith(
                    startName):
                    newName = nameGen()
                    globalNames['vars']['global'][search.group(3)] = {'newName': newName, 'level': level}
                    clear_stroke = re.sub(f'{search.group(3)}', newName, clear_stroke)

        search = re.search(selfFind.format(globalNames['self'], globalNames['self']), clear_stroke)

        if search is not None:

            if search.group(1) is not None and search.group(1) not in globalNames['vars']['enclosing'].keys():
                newName = nameGen()
                globalNames['vars']['global'][search.group(1)] = {'newName': newName, 'level': level}
                clear_stroke = re.sub(f'{search.group(1)}', newName, clear_stroke)

            if search.group(2) is not None and search.group(2) not in globalNames['vars']['enclosing'].keys():
                newName = nameGen()
                globalNames['vars']['global'][search.group(2)] = {'newName': newName, 'level': level}
                clear_stroke = re.sub(f'{search.group(2)}', newName, clear_stroke)

        newFile.write(clear_stroke + '\n')

newFile.close()

with open('someFile.py', 'r+') as temporaryFile:
    for i in temporaryFile.readlines():
        constFile.write(i)


os.remove('someFile.py')

# with open('alsoTest.py', 'w') as file:
#     file.write(createNumFunc(40))
#     file.write(createNumFunc(2))

# import ast
# from pprint import pprint
#
# stats = {'import': [], 'fromImport': [], 'classes': {},
#          'standAloneFunction': {}, 'globalVariables': {}}
#
#
# with open("testFile.py", "r") as source:
#     globalTree = ast.parse(source.read())
#
#
# def main(tree=None, fromwho=None):
#     global globalTree
#
#     tree = tree if tree is not None else globalTree
#
#     analyzer = Analyzer(fromwho)
#     analyzer.visit(tree)
#     analyzer.report()
#
#
# class Analyzer(ast.NodeVisitor):
#     global stats
#
#     def __init__(self, fromWho):
#         self.fromWho = fromWho
#
#     @staticmethod
#     def nameGen(name):
#         return str(sum(id(i) // 1000 for i in name))
#
#     # def visit_Import(self, node):
#     #     for alias in node.names:
#     #         self.stats["import"].append(alias.name)
#     #     self.generic_visit(node)
#
#     # def visit_ImportFrom(self, node):
#     #     for alias in node.names:
#     #         self.stats["from"].append(alias.name)
#     #     self.generic_visit(node)
#
#     def visit_Name(self, node):
#         if node.id not in ('len', 'for', 'range', 'print', ''):
#             stats['globalVariables'][node.id] = Analyzer.nameGen(node.id)
#         pass
#
#     def visit_ClassDef(self, node):
#         stats['classes'][node.name] = {'vars': {},
#                                        'funcs': {},
#                                        'parents': []}
#         for obj in node.body:
#             if 'Assign' in str(obj):
#                 if 'Name' in str(obj.value):
#                     stats['classes'][node.name]['vars'][obj.targets[0].id] = [
#                         Analyzer.nameGen(obj.targets[0].id), Analyzer.nameGen(obj.value.id)
#                     ]
#                 else:
#                     stats['classes'][node.name]['vars'][obj.targets[0].id] = [
#                         Analyzer.nameGen(obj.targets[0].id), None
#                     ]
#
#             else:
#                 main(obj, node.name)
#
#     def visit_FunctionDef(self, node):
#         if self.fromWho is not None:
#             stats['classes'][self.fromWho]['funcs'][node.name] = {
#                 'args': {}, 'vars': {}
#             }
#             for obj in node.body:
#                 if 'Assign' in str(obj):
#                     for t in obj.targets:
#                         if 'Attribute' in str(t):
#                             stats['classes'][self.fromWho]['funcs'][node.name]['vars'][t.attr] = [
#                                 Analyzer.nameGen(t.attr), obj.value.attr
#                             ]
#                         else:
#                             stats['classes'][self.fromWho]['funcs'][node.name]['vars'][t.id] = [
#                                 Analyzer.nameGen(t.id), None
#                             ]
#         else:
#             stats['standAloneFunction'][node.name] = {
#                 'args': {}, 'vars': {}
#             }
#             for obj in node.body:
#                 if 'Assign' in str(obj):
#                     for t in obj.targets:
#                         if 'Name' in str(obj.value):
#                             stats['standAloneFunction'][node.name]['vars'][t.id] = [
#                                 Analyzer.nameGen(t.id), obj.value.id
#                             ]
#                         else:
#                             stats['standAloneFunction'][node.name]['vars'][t.id] = [
#                                 Analyzer.nameGen(t.id), None
#                             ]
#
#
#     @staticmethod
#     def report():
#         pprint(stats)
#         pass
#
#
# main()
