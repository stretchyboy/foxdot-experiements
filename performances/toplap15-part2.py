##################################################################################
# Created with stems2foxdot by stretch
# From Gravity Hero
# © Rabbit Junk with Permission
# Thanks J.P.
###################################################################################
Samples.addPath("/home/meggleton/Projects/algorave/stems/Gravity Hero")
Clock.bpm = 175



p1 >> loop('art_of_def_guitar_01', sample=3, dur=2, rate=P([0,2,1,3,4,2]).map(getRate)) # 13 beats @ 660

d1 >> play("<x X ><(%^&*_)><  ($      )>").solo()


Thanks guys .. My first proper live strem sorry about the mono?



g3 >> loop('Gravity_Hero_Keys_01', sample=6, dur=16) # 7 beats @ 501
g1 >> loop('Gravity_Hero_Keys_01', sample=0, dur=16, delay=8) # 2 beats @ 10
g2 >> loop('Gravity_Hero_Keys_01', sample=0, dur=16, delay=12) # 2 beats @ 10


s1 >> loop('Gravity_Hero_Keys_01', sample=1, dur=60) # 59 beats @ 17

s1 >> loop('Gravity_Hero_Keys_01', sample=2, dur=120) # 120 beats @ 80

s1 >> loop('Gravity_Hero_Keys_01', sample=3, dur=60) # 57 beats @ 204

s1 >> loop('Gravity_Hero_Keys_01', sample=4, dur=4) # 3 beats @ 276

s1 >> loop('Gravity_Hero_Keys_01', sample=5, dur=212) # 212 beats @ 284

s1 >> loop('Gravity_Hero_Keys_01', sample=6, dur=16) # 7 beats @ 501

s1 >> loop('Gravity_Hero_Keys_01', sample=7, dur=64) # 61 beats @ 532

s1 >> loop('Gravity_Hero_Keys_01', sample=8, dur=104) # 102 beats @ 595

s2.stop()

s2 >> loop('Gravity_Hero_Vocals_01', sample=0, dur=64) # 6 beats @ 112 STEP

s2 >> loop('Gravity_Hero_Vocals_01', sample=1, dur=8) # 8 beats @ 127

s2 >> loop('Gravity_Hero_Vocals_01', sample=2, dur=12) # 10 beats @ 140

s2 >> loop('Gravity_Hero_Vocals_01', sample=3, dur=8) # 8 beats @ 159

s2 >> loop('Gravity_Hero_Vocals_01', sample=4, dur=8) # 7 beats @ 172

s2 >> loop('Gravity_Hero_Vocals_01', sample=5, dur=4) # 3 beats @ 186

s2 >> loop('Gravity_Hero_Vocals_01', sample=6, dur=8) # 7 beats @ 197

s2 >> loop('Gravity_Hero_Vocals_01', sample=7, dur=4) # 2 beats @ 210

s2 >> loop('Gravity_Hero_Vocals_01', sample=8, dur=4) # 3 beats @ 217

s2 >> loop('Gravity_Hero_Vocals_01', sample=9, dur=8) # 6 beats @ 230

s2 >> loop('Gravity_Hero_Vocals_01', sample=10, dur=4) # 4 beats @ 241

s2 >> loop('Gravity_Hero_Vocals_01', sample=11, dur=8) # 6 beats @ 249

s2 >> loop('Gravity_Hero_Vocals_01', sample=12, dur=8) # 8 beats @ 262

s2 >> loop('Gravity_Hero_Vocals_01', sample=13, dur=16) # 14 beats @ 272

s2 >> loop('Gravity_Hero_Vocals_01', sample=14, dur=8) # 8 beats @ 295

s2 >> loop('Gravity_Hero_Vocals_01', sample=15, dur=12) # 10 beats @ 308

s2 >> loop('Gravity_Hero_Vocals_01', sample=16, dur=8) # 8 beats @ 327

s2 >> loop('Gravity_Hero_Vocals_01', sample=17, dur=8) # 7 beats @ 340

s2 >> loop('Gravity_Hero_Vocals_01', sample=18, dur=68) # 66 beats @ 353

s2 >> loop('Gravity_Hero_Vocals_01', sample=19, dur=4) # 3 beats @ 465

s2 >> loop('Gravity_Hero_Vocals_01', sample=20, dur=8) # 6 beats @ 477

s2 >> loop('Gravity_Hero_Vocals_01', sample=21, dur=8) # 8 beats @ 497

s2 >> loop('Gravity_Hero_Vocals_01', sample=22, dur=24) # 24 beats @ 510

s2 >> loop('Gravity_Hero_Vocals_01', sample=23, dur=8) # 8 beats @ 543

s2 >> loop('Gravity_Hero_Vocals_01', sample=24, dur=12) # 10 beats @ 556

s2 >> loop('Gravity_Hero_Vocals_01', sample=25, dur=12) # 10 beats @ 575

s2 >> loop('Gravity_Hero_Vocals_01', sample=26, dur=100) # 100 beats @ 593

s2.stop()

s3.stop()

z1 >> loop('gravity_hero_guitar_01', sample=0, dur=8, delay=0) # 4 beats @ 81
z2 >> loop('gravity_hero_guitar_01', sample=1, dur=8, delay=4) # 4 beats @ 89
z3 >> loop('gravity_hero_guitar_01', sample=5, dur=16, delay=8) # 16 beats @ 337

s4 >> loop('gravity_hero_guitar_01', sample=2, dur=4) # 4 beats @ 104

s4 >> loop('gravity_hero_guitar_01', sample=3, dur=72) # 69 beats @ 116

s4 >> loop('gravity_hero_guitar_01', sample=4, dur=84) # 83 beats @ 252

s4 >> loop('gravity_hero_guitar_01', sample=5, dur=16) # 16 beats @ 337

s4.stop()

s4 >> loop('gravity_hero_guitar_01', sample=6, dur=36) # 34 beats @ 356

s4 >> loop('gravity_hero_guitar_01', sample=7, dur=16) # 13 beats @ 393

s4 >> loop('gravity_hero_guitar_01', sample=8, dur=12) # 12 beats @ 409

s4 >> loop('gravity_hero_guitar_01', sample=9, dur=12) # 10 beats @ 427

s4 >> loop('gravity_hero_guitar_01', sample=10, dur=96) # 94 beats @ 500

s4 >> loop('gravity_hero_guitar_01', sample=11, dur=36) # 34 beats @ 596

s4 >> loop('gravity_hero_guitar_01', sample=12, dur=16) # 13 beats @ 633

s4 >> loop('gravity_hero_guitar_01', sample=13, dur=12) # 11 beats @ 649

s4 >> loop('gravity_hero_guitar_01', sample=14, dur=16) # 14 beats @ 664

s4 >> loop('gravity_hero_guitar_01', sample=15, dur=16) # 16 beats @ 681

s4.stop()

s5 >> loop('gravity_hero_loops_01', sample=0, dur=4) # 2 beats @ 22

s5 >> loop('gravity_hero_loops_01', sample=1, dur=8) # 6 beats @ 26

s5 >> loop('gravity_hero_loops_01', sample=2, dur=4) # 2 beats @ 38

s5 >> loop('gravity_hero_loops_01', sample=3, dur=8) # 6 beats @ 42

s5 >> loop('gravity_hero_loops_01', sample=4, dur=28) # 25 beats @ 51

s5 >> loop('gravity_hero_loops_01', sample=5, dur=4) # 2 beats @ 193

s5 >> loop('gravity_hero_loops_01', sample=6, dur=8) # 6 beats @ 197

s5 >> loop('gravity_hero_loops_01', sample=7, dur=4) # 2 beats @ 209

s5 >> loop('gravity_hero_loops_01', sample=8, dur=8) # 6 beats @ 213

s5 >> loop('gravity_hero_loops_01', sample=9, dur=4) # 2 beats @ 225

s5 >> loop('gravity_hero_loops_01', sample=10, dur=8) # 6 beats @ 229

s5 >> loop('gravity_hero_loops_01', sample=11, dur=8) # 6 beats @ 241

s5.stop()
