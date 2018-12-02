import traceback
import sys
import timeout_decorator

from rockstarpy.transpile import Transpiler

transpiler = Transpiler()

def extract(dct, namespace=None):
    if not namespace: namespace = globals()
    namespace.update(dct)

def rsf(filename, namespace=None, printname=None):
    f = open(filename, "r")
    lyrics = f.read()
    rs(lyrics, namespace, printname)

@timeout_decorator.timeout(5)
def rs(lyrics, namespace=None, printname=None):
    if printname:
        converted_code = printname+" = [] \n"
    else:
        converted_code = ""

    for line in lyrics.split("\n"):
        converted_line = transpiler.transpile_line(line+"\n")
        if printname:
            converted_line = converted_line.replace("print",printname+".append")
        converted_code += converted_line

    if printname:
        converted_code +="print("+printname+")"

    print(converted_code)

    try:
        exec(converted_code)
        extract(locals(), namespace)
    except SyntaxError:
        print ("Your words don't mean much too me. (Syntax error)")
    #return converted_code

if __name__ == '__main__':
    rs('''
Tommy was a docker
While Tommy ain't nothing
Scream Tommy
Knock Tommy down
''', locals())
