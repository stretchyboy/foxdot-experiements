from rockstarpy.transpile import Transpiler

def extract(dct, namespace=None):
    if not namespace: namespace = globals()
    namespace.update(dct)

def rsf(filename, namespace=None, printname=None):
    f = open(filename, "r")
    lyrics = f.read()
    rs(lyrics, namespace, printname)

def rs(lyrics, namespace=None, printname=None):
    transpiler = Transpiler()
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

    ##print(converted_code)
    exec(converted_code)

    extract(locals(), namespace)
    #return converted_code
