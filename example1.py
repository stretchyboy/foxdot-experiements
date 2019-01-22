from foxdotrockstar import *
stalk("tommy.rock", locals(), "tommies")

p1 >> arpy(tommies)

Clock.bpm = 90 #2*Midnight(Papa, 100)


d1 >> play(P["x-o-"])#.every(3, "bubble")#.every(4, "amen"))

stalk("FizzBuzz.rock", locals(), "fizzbuzz")

p1 >> bass(fizzbuzz, dur=PDur(17, 24))#.every(10, "loving")


p2 >> viola(fizzbuzz, dur=PDur(7, 16)).every(5, "reverse")#.every(10, "loving")

p2.stop()

print(SynthDefs)

print(Clock.bpm)

#@PlayerMethod
#def loving(self):
#    global Clock
#    Clock.bpm = Lovin(Clock.bpm, 10)

#d1.never("loving")

