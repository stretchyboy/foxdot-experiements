from foxdotrockstar import *

rsf("Midnight.rock", locals())

rsf("tommy.rock", locals(), "tommies")

rsf("Getting There.rock", locals(), "places") 

rsf("FizzBuzz.rock", locals(), "fizzbuzz")

Clock.bpm = 2*Midnight(Papa, 100)

@PlayerMethod
def loving(self):
    global Clock
    Clock.bpm = Lovin(Clock.bpm, 10)


p1 >> bass(fizzbuzz, dur=PDur(17, 24))#.every(10, "loving")


p2 >> viola(fizzbuzz, dur=PDur(7, 16)).every(5, "reverse")#.every(10, "loving")

p2.stop()

print(SynthDefs)

print(Clock.bpm)

d1.never("loving")

d1 >> play("x($%)(-x)[<o->*]", dist=0.5).every(12, "reverse").every(5, "stutter").every(10, "loving")

