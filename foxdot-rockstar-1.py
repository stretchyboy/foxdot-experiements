from rockstarpy.transpile import Transpiler

def rockstar(lyrics, printname="out"):
    transpiler = Transpiler()
    converted_code = printname+" = [] \n"

    for line in lyrics.split("\n"):
        converted_code += transpiler.transpile_line(line+"\n").replace("print",printname+".append")
    converted_code +="print("+printname+")"
    
    print(converted_code)
    return converted_code

exec(rockstar('''
Papa was a rolling stone. wherever he laid his hat was his home

Tommy was a docker
While Tommy aint 0,
Scream Tommy
Knock Tommy down
''', "dave"))

Clock.bpm = Papa

d1 >> play(" x-o-").every(Pvar(dave), "stutter")

