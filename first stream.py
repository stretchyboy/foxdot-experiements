from foxdotrockstar import *

rsf("FizzBuzz.rock", locals(), "fizzes")

rsf("tommy.rock", locals(), "tommies")

rsf("Getting There.rock", locals())


print(SynthDefs)

d1 >> play("x <-0>[--]", amp=[1,0.5]).every(7, "stutter")

p1 >> sitar(tommies, amp=0.3, dur=P(fizzes)/4,  pan=(-1, 1), pshift=(0, 0.125)).every(3,"shuffle")

p2 >> swell().accompany(p1).every(4, "reverse").offbeat().spread()

d1.stop()

p3 >> orient().accompany(p1).every(4, "reverse").offbeat().spread()

d1.stop()

p1 >> arpy(fizzes, dur=PDur(fizzes, 32).rotate([6,2,3,4])).every(6, "stutter")

p1 >> arpy(P(fizzes), dur=PDur(fizzes, 8)).every(16, "stutter")

p1.stop()

d2 >> play(P["x-o-"]).every(3, "bubble").every(4, "amen"))

d2 >> play("-(x[xx*]) <*-[--]>").every(5, "amen").every(4, "stutter")

d2.solo()

s1 >> loop('Bullet/808s', sample=0, dur=8) # 2 beats @ 312

s2.stop()

Clock.bpm = Papa

s1 >> loop('Bullet/808s', sample=1, dur=4) # 3 beats @ 16


s2 >> loop('Bullet/Backing_Vocals', sample=1, chop=2, dur=PDur(2,30)) # Aim Shot 3 beats @ 72

s2 >> loop('Bullet/Bullet_Vocals_MAIN', sample=0, chop=2, dur=PDur(2,13)) # 

s3 >> loop('Bullet/Rhythm_Guitars', sample=2, dur=8) # 30 beats @ 73


p1.never("loving")

@PlayerMethod
def loving(self):
    global Clock
    Clock.bpm = Lovin(Clock.bpm, 10)
