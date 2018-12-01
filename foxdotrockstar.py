from rockstarpy.transpile import Transpiler

def extract(dct, namespace=None):
    if not namespace: namespace = globals()
    namespace.update(dct)

def rs(lyrics, printname="out",namespace=None):
    transpiler = Transpiler()
    converted_code = printname+" = [] \n"

    for line in lyrics.split("\n"):
        converted_code += transpiler.transpile_line(line+"\n").replace("print",printname+".append")
    converted_code +="print("+printname+")"

    print(converted_code)
    exec(converted_code)

    extract(locals(), namespace)
    #return converted_code
