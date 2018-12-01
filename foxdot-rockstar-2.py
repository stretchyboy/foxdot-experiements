from foxdotrockstar import *

rs('''
Papa was a rolling stone. wherever he laid his hat was his home

Tommy was a docker
While Tommy aint 0,
Scream Tommy
Knock Tommy down
''', "dave", locals())

Clock.bpm = Papa

d1 >> play(" x-o-").every(Pvar(dave), "stutter")
