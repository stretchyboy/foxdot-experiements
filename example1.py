from foxdotrockstar import *

d1 >> play("[-x] [( X($    *      [*[%]]     )X)]+", sample=P([0,1,2,3],15))

rsf("Midnight.rock", locals())

stalk("tommy.rock", locals(), "tommies")

rsf("Getting There.rock", locals(), "places") 



Clock.bpm = 90 #2*Midnight(Papa, 100)


d1 >> play(P["x-o-"])#.every(3, "bubble")#.every(4, "amen"))

@PlayerMethod
def loving(self):
    global Clock
    Clock.bpm = Lovin(Clock.bpm, 10)

rsf("FizzBuzz.rock", locals(), "fizzbuzz")
p1 >> bass(fizzbuzz, dur=PDur(17, 24))#.every(10, "loving")


p2 >> viola(fizzbuzz, dur=PDur(7, 16)).every(5, "reverse")#.every(10, "loving")

p2.stop()

print(SynthDefs)

print(Clock.bpm)

d1.never("loving")

d1 >> play("x($%)(-x)[<o->*]", dist=0.5).every(12, "reverse").every(5, "stutter",)
