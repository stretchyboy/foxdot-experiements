##################################################################################
# Created with stems2foxdot by stretch
# From Gravity Hero
# © Rabbit Junk with Permission
###################################################################################
Samples.addPath("/home/meggleton/Projects/algorave/stems/Gravity Hero")
Clock.bpm = 175

d1 >> loop('gravity_hero_loops_01', P[2,0,2,1,10,8,2,1,:8].palindrome(), sample=0, amp=Pvar([1,0],[1]), dur=1, tempo=175) # 61 beats @ 16

d1.solo()

s1 >> loop('gravity_hero_loops_01', P[:8], sample=1, amp=Pvar([1,1],[8]), dur=1, tempo=175) # 8 beats @ 81

s1 >> loop('gravity_hero_loops_01',  P[:8,2,0,2,1,10,8,2,1].palindrome(), sample=2, amp=Pvar([0,1],[1]), dur=1, tempo=175) # 12 beats @ 92

s1.solo()

s1 >> loop('gravity_hero_loops_01', P[:64], sample=3, amp=Pvar([1,1],[64]), dur=1, tempo=175) # 60 beats @ 189

s1 >> loop('gravity_hero_loops_01', P[:8], sample=4, amp=Pvar([1,1],[8]), dur=1, tempo=175) # 5 beats @ 253

s1 >> loop('gravity_hero_loops_01', P[:8], sample=5, amp=Pvar([1,1],[8]), dur=1, tempo=175) # 2 beats @ 468

s1 >> loop('gravity_hero_loops_01', P[:8], sample=6, amp=Pvar([1,1],[8]), dur=1, tempo=175) # 3 beats @ 475

s1 >> loop('gravity_hero_loops_01', P[:8], sample=7, amp=Pvar([1,1],[8]), dur=1, tempo=175) # 3 beats @ 483

s1 >> loop('gravity_hero_loops_01', P[:8], sample=8, amp=Pvar([1,1],[8]), dur=1, tempo=175) # 4 beats @ 491

s1 >> loop('gravity_hero_loops_01', P[:8], sample=9, amp=Pvar([1,1],[8]), dur=1, tempo=175) # 4 beats @ 502

s1.stop()

s2.stop()

s3 >> loop('gravity_hero_guitar_01', P[:8], sample=0, amp=Pvar([1,1],[8]), dur=1, tempo=175) # 5 beats @ 80

s3 >> loop('gravity_hero_guitar_01', P[:8], sample=1, amp=Pvar([1,1],[8]), dur=1, tempo=175) # 5 beats @ 88

s3 >> loop('gravity_hero_guitar_01', P[:16], sample=2, amp=Pvar([1,0],[16]), dur=1, tempo=175) # 12 beats @ 96

t3 >> loop('gravity_hero_guitar_01', P[:16], sample=3, amp=Pvar([0,1],[16]), dur=1, tempo=175) # 70 beats @ 115

s3 >> loop('gravity_hero_guitar_01', P[:192], sample=4, amp=Pvar([1,1],[192]), dur=1, tempo=175) # 188 beats @ 251

s3 >> loop('gravity_hero_guitar_01', P[:200], sample=5, amp=Pvar([1,1],[200]), dur=1, tempo=175) # 198 beats @ 499

s3.stop()

s4 >> loop('Gravity_Hero_Vocals_01', P[:8], sample=0, amp=Pvar([1,1],[8]), dur=1, tempo=175) # 3 beats @ 15

s4 >> loop('Gravity_Hero_Vocals_01', P[:8], sample=1, amp=Pvar([1,1],[8]), dur=1, tempo=175) # 3 beats @ 28

s4 >> loop('Gravity_Hero_Vocals_01', P[:8], sample=2, amp=Pvar([1,1],[8]), dur=1, tempo=175) # 6 beats @ 41

s4 >> loop('Gravity_Hero_Vocals_01', P[:24], sample=3, amp=Pvar([1,1],[24]), dur=1, tempo=175) # 20 beats @ 99

s4 >> loop('Gravity_Hero_Vocals_01', P[:16], sample=4, amp=Pvar([1,1],[16]), dur=1, tempo=175) # 10 beats @ 127

s4 >> loop('Gravity_Hero_Vocals_01', P[:16], sample=5, amp=Pvar([1,1],[16]), dur=1, tempo=175) # 10 beats @ 140

s4 >> loop('Gravity_Hero_Vocals_01', P[:16], sample=6, amp=Pvar([1,1],[16]), dur=1, tempo=175) # 10 beats @ 159

s4 >> loop('Gravity_Hero_Vocals_01', P[:8], sample=7, amp=Pvar([1,1],[8]), dur=1, tempo=175) # 7 beats @ 172

s4 >> loop('Gravity_Hero_Vocals_01', P[:8], sample=8, amp=Pvar([1,1],[8]), dur=1, tempo=175) # 4 beats @ 185

s4 >> loop('Gravity_Hero_Vocals_01', P[:8], sample=9, amp=Pvar([1,1],[8]), dur=1, tempo=175) # 8 beats @ 196

s4 >> loop('Gravity_Hero_Vocals_01', P[:8], sample=10, amp=Pvar([1,1],[8]), dur=1, tempo=175) # 3 beats @ 210

s4 >> loop('Gravity_Hero_Vocals_01', P[:8], sample=11, amp=Pvar([1,0],[8]), dur=1, tempo=175) # 5 beats @ 216

s4 >> loop('Gravity_Hero_Vocals_01', P[:8], sample=12, amp=Pvar([1,1],[8]), dur=1, tempo=175) # 7 beats @ 229

s4 >> loop('Gravity_Hero_Vocals_01', P[:8], sample=13, amp=Pvar([1,1],[8]), dur=1, tempo=175) # 4 beats @ 241

s4 >> loop('Gravity_Hero_Vocals_01', P[:8], sample=14, amp=Pvar([1,1],[8]), dur=1, tempo=175) # 7 beats @ 248

s4 >> loop('Gravity_Hero_Vocals_01', P[:32], sample=15, amp=Pvar([1,1],[32]), dur=1, tempo=175) # 25 beats @ 262

s4 >> loop('Gravity_Hero_Vocals_01', P[:16], sample=16, amp=Pvar([1,1],[16]), dur=1, tempo=175) # 10 beats @ 295

s4 >> loop('Gravity_Hero_Vocals_01', P[:16], sample=17, amp=Pvar([1,1],[16]), dur=1, tempo=175) # 10 beats @ 308

s4 >> loop('Gravity_Hero_Vocals_01', P[:16], sample=18, amp=Pvar([1,1],[16]), dur=1, tempo=175) # 10 beats @ 327

s4 >> loop('Gravity_Hero_Vocals_01', P[:8], sample=19, amp=Pvar([1,1],[8]), dur=1, tempo=175) # 7 beats @ 340

s4 >> loop('Gravity_Hero_Vocals_01', P[:80], sample=20, amp=Pvar([1,0,1,0],[80]), dur=1, tempo=175) # 79 beats @ 353

s4 >> loop('Gravity_Hero_Vocals_01', P[:8], sample=21, amp=Pvar([1,1],[8]), dur=1, tempo=175) # 4 beats @ 465

s4 >> loop('Gravity_Hero_Vocals_01', P[:8], sample=22, amp=Pvar([1,1],[8]), dur=1, tempo=175) # 6 beats @ 477

s4 >> loop('Gravity_Hero_Vocals_01', P[:16], sample=23, amp=Pvar([1,1],[16]), dur=1, tempo=175) # 9 beats @ 496

s4 >> loop('Gravity_Hero_Vocals_01', P[:32], sample=24, amp=Pvar([1,1],[32]), dur=1, tempo=175) # 26 beats @ 509

s4 >> loop('Gravity_Hero_Vocals_01', P[:16], sample=25, amp=Pvar([1,1],[16]), dur=1, tempo=175) # 10 beats @ 543

s4 >> loop('Gravity_Hero_Vocals_01', P[:16], sample=26, amp=Pvar([1,1],[16]), dur=1, tempo=175) # 10 beats @ 556

s4 >> loop('Gravity_Hero_Vocals_01', P[:16], sample=27, amp=Pvar([1,1],[16]), dur=1, tempo=175) # 11 beats @ 575

t4 >> loop('Gravity_Hero_Vocals_01', P[:80], sample=28, amp=Pvar([0,1,0,1],[80]), dur=1, tempo=175) # 101 beats @ 593

s4.stop()

s5 >> loop('Gravity_Hero_Keys_01', P[:72], sample=0, amp=Pvar([1,1],[72]), dur=1, tempo=175) # 69 beats @ 8

s5 >> loop('Gravity_Hero_Keys_01', P[:200], sample=1, amp=Pvar([1,1],[200]), dur=1, tempo=175) # 200 beats @ 80

s5 >> loop('Gravity_Hero_Keys_01', P[:248], sample=2, amp=Pvar([1,1],[248]), dur=1, tempo=175) # 242 beats @ 284

s5 >> loop('Gravity_Hero_Keys_01', P[:168], sample=3, amp=Pvar([1,1],[168]), dur=1, tempo=175) # 167 beats @ 532

s5.stop()
