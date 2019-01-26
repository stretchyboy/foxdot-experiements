# foxdot-experiements
stuff and nonsense for performing with foxdot. good stuff will spinoff into its own repo

so far we have a :

* few tests usinmg the early stages of https://github.com/stretchyboy/stems2foxdot
* the start of strapping Rockstar(https://github.com/dylanbeattie/rockstar)  to FoxDot, using https://github.com/yanorestes/rockstar-py

## For the Rockstar code
 * use python3
 * pip3 install numpy timeout_decorator watchdog rockstarfoxdot
 * pip3 install -U git+https://github.com/yanorestes/rockstar-py.git

### Instructions

Start up FoxDot as normal

Before trying to run any Rockstar run this line

```
from rockstarfoxdot import *
```

#### rs(lyrics, namespace=None, printname=None)
Use rockstar in-line
```
rs('''
Papa was a rolling stone
''', locals())
```

When run this will exec this python in your FoxDot
```
Papa = 175
```

#### rsf(filename, namespace=None, printname=None)
Use rockstar from a file
```
rsf("FizzBuzz.rock", locals(), "fizzbuzz")
p1 >> bass(fizzbuzz, dur=PDur(17, 24))
```

When run this will exec the rockstar from "FizzBuzz.rock" in your FoxDot and place anything you 'Shout'ed 'Said' or 'Scream'ed into a list called fizzbuzz.

Then it will play those notes on the bass in FoxDot player p1

**rsf()** has a timeout protecting you from infinite loops in the rockstar

#### stalk(filename, namespace=None, printname=None)
Use rockstar from a file and rerun when the file is changed

```
stalk("FizzBuzz.rock", locals(), "fizzbuzz")
```

When run this will exec the rockstar from "FizzBuzz.rock" in your FoxDot and place anything you 'Shout'ed 'Said' or 'Scream'ed into a list called fizzbuzz.

It will rerun this exec whenever the rockstar code is changed

**stalk()** has **no** timeout protecting you from infinite loops in the rockstar
