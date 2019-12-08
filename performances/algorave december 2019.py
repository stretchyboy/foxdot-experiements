Clock.bpm=180

d1 >> play("([xx]-[--]) X ", sample=[2,2,4])
d2 >> play("< s ss [ss] s ><(( -)*[--])(- -)  (+ - )>", sample=[2,3,4])

Scale.default = Scale.major

p1 >> growl(P[0,2,1,2,3,1].palindrome(), amp=linvar([0,0.7], 32), dur=PDur(P[5,3,7].palindrome(), 16), start=nextbar)
p3 >>  squish(P[0,2,1,2,3,1].palindrome(),  amp=var([0.7,0], 32),dur=PDur(P[3,4,7].palindrome(), 16), start=nextbar)

p2 >> space(p1.pitch.accompany(), amp=var([0.5,0], 24), dur=PDur(P[3,4], 16), start=nextbar)

p4 >> jbass(p1.pitch.accompany()+(0,1,2), amp=var([0.5,0], 24), dur=PDur(P[3,4], 16), start=nextbar)

p1.solo()


p_all.amp=linvar([0.5,0], [16, inf], start=nextbar)




##################################################################################
# Created with stems2foxdot by stretch
# From Xenon
# © Rabbit Junk with Permission
###################################################################################
Samples.addPath("/home/meggleton/Projects/algorave/stems/Xenon")

Clock.bpm = 180

##
s1 >> loop('xenon_sum_grrrl_01', P[:4], sample=2, amp=Pvar([0,0,0,0,1],[4]), dur=1, tempo=130) # 4 beats @ 209

s2 >> loop('xenon_vocals_01', P[:8], sample=19, amp=Pvar([1,0,0,0],[8]), dur=1, tempo=130) # 6 beats @ 441


s4 >> loop('xenon_guitar_130bpm', P[1,4,6,2,5,5,2,9].palindrome(), sample=1, amp=Pvar([2,0],[16]), dur=1, tempo=130) # 15 beats @ 30

g4 >> loop('xenon_guitar_130bpm', P[1,2,4,5,7,3,5,9].palindrome(), sample=2, amp=Pvar([0,2],[16]), dur=1, tempo=130) # 17 beats @ 144
s4 >> loop('xenon_guitar_130bpm', P[:20], sample=3, amp=Pvar([1,0],[20]), dur=1, tempo=130) # 17 beats @ 162


s5 >> loop('xenon_keys_01', P[2,4,5,2,1], sample=2, amp=Pvar([1,1],[8]), dur=1, tempo=130) # 5 beats @ 108

##################################################################################
# Created with stems2foxdot by stretch
# From Gravity Hero
# © Rabbit Junk with Permission
###################################################################################
Samples.addPath("/home/meggleton/Projects/algorave/stems/Gravity Hero")
Clock.bpm = 175

d1 >> loop('gravity_hero_loops_01', P[2,0,2,1,10,8,2,1,:8].palindrome(), sample=0, amp=Pvar([1,0],[1]), dur=1, tempo=175) # 61 beats @ 16

s1 >> loop('gravity_hero_loops_01',  P[:8,2,0,2,1,10,8,2,1].palindrome(), sample=2, amp=Pvar([0,1],[1]), dur=1, tempo=175) # 12 beats @ 92



##################################################################################
# Created with stems2foxdot by stretch
# From Bullet
# © Hyro the Hero with Permission
###################################################################################
Samples.addPath("/home/meggleton/Projects/algorave/stems/Bullet")
Clock.bpm = 110

s1 >> loop('Lead_Guitars', P[1,2,4,2,0,5,3, 3,2,9].palindrome(), sample=0, amp=Pvar([1,0],[16]), dur=1, tempo=110) # 31 beats @ 73

s1 >> loop('Lead_Guitars', P[:32], sample=1, amp=Pvar([1,0],[32]), dur=1, tempo=110) # 31 beats @ 161



p1 >> squish( [4, 4, 4, 2, 1, 0, 4, 4, 4, 4, 2, 1, 0, 5, 5, 6, 3, 2, 1, 6, 6, 4, 4, 3, 1, 2, 4, 4, 4, 2, 1, 0, 4, 4, 4, 4, 2, 1, 0, 5, 5, 6, 3, 2, 1, 4, 4, 4, 4, 5, 4, 3, 1, 0, 4, 2, 2, 2, 2, 2, 2, 2, 4, 0, 1, 2, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 2, 1, 4, 2, 2, 2, 2, 2, 2, 2, 4, 0, 1, 2, 3, 3, 3, 3, 3, 2, 2, 2, 2, 4, 4, 3, 1, 0], dur=[0.5, 0.5, 1.0, 1.0, 1.0, 1.0, 3.0, 0.5, 0.5, 1.0, 1.0, 1.0, 1.0, 3.0, 0.5, 1.0, 1.0, 1.0, 1.0, 3.0, 0.5, 1.0, 1.0, 1.0, 1.0, 3.0, 0.5, 0.5, 1.0, 1.0, 1.0, 1.0, 3.0, 0.5, 0.5, 1.0, 1.0, 1.0, 1.0, 3.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.5, 0.5, 1.0, 1.0, 1.0, 1.0, 3.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.5, 0.5, 3.0, 1.0, 1.0, 1.5, 0.5, 1.0, 1.0, 1.0, 0.5, 0.5, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 2.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.5, 0.5, 3.0, 1.0, 1.0, 1.5, 0.5, 1.0, 1.0, 1.0, 0.5, 0.5, 1.0, 1.0, 1.0, 1.0, 3.0] , oct=[3.0, 3.0, 3.0, 4.0, 4.0, 4.0, 3.0, 3.0, 3.0, 3.0, 4.0, 4.0, 4.0, 3.0, 3.0, 3.0, 4.0, 4.0, 4.0, 3.0, 3.0, 4.0, 4.0, 4.0, 4.0, 4.0, 3.0, 3.0, 3.0, 4.0, 4.0, 4.0, 3.0, 3.0, 3.0, 3.0, 4.0, 4.0, 4.0, 3.0, 3.0, 3.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0], drive=2 , amp=linvar([0,1], [32, inf], start=nextbar))
#changed to lazer towards end to clean it up
