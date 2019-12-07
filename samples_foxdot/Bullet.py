##################################################################################
# Created with stems2foxdot by stretch
# From Bullet
# © Hyro the Hero with Permission until Jan 2019
###################################################################################
Samples.addPath("/home/meggleton/Projects/algorave/stems/Bullet")
Clock.bpm = 110

s1 >> loop('Lead_Guitars', P[:32], sample=0, amp=Pvar([1,1],[32]), dur=1, tempo=110) # 31 beats @ 73

s1 >> loop('Lead_Guitars', P[:32], sample=1, amp=Pvar([1,1],[32]), dur=1, tempo=110) # 31 beats @ 161

s1 >> loop('Lead_Guitars', P[:32], sample=2, amp=Pvar([1,1],[32]), dur=1, tempo=110) # 31 beats @ 273

s1.stop()

s2 >> loop('Bullet_Vocals_MAIN', P[:32], sample=0, amp=Pvar([1,1],[32]), dur=1, tempo=110) # 32 beats @ 33

s2 >> loop('Bullet_Vocals_MAIN', P[:40], sample=1, amp=Pvar([1,1],[40]), dur=1, tempo=110) # 39 beats @ 65

s2 >> loop('Bullet_Vocals_MAIN', P[:40], sample=2, amp=Pvar([1,1],[40]), dur=1, tempo=110) # 39 beats @ 120

s2 >> loop('Bullet_Vocals_MAIN', P[:36], sample=3, amp=Pvar([1,1],[36]), dur=1, tempo=110) # 34 beats @ 159

s2 >> loop('Bullet_Vocals_MAIN', P[:4], sample=4, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 2 beats @ 207

s2 >> loop('Bullet_Vocals_MAIN', P[:8], sample=5, amp=Pvar([1,1],[8]), dur=1, tempo=110) # 5 beats @ 212

s2 >> loop('Bullet_Vocals_MAIN', P[:8], sample=6, amp=Pvar([1,1],[8]), dur=1, tempo=110) # 5 beats @ 220

s2 >> loop('Bullet_Vocals_MAIN', P[:8], sample=7, amp=Pvar([1,1],[8]), dur=1, tempo=110) # 6 beats @ 228

s2 >> loop('Bullet_Vocals_MAIN', P[:4], sample=8, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 3 beats @ 235

s2 >> loop('Bullet_Vocals_MAIN', P[:68], sample=9, amp=Pvar([1,1],[68]), dur=1, tempo=110) # 66 beats @ 238

s2 >> loop('Bullet_Vocals_MAIN', P[:8], sample=10, amp=Pvar([1,1],[8]), dur=1, tempo=110) # 6 beats @ 315

s2.stop()

s3 >> loop('808s', P[:4], sample=0, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 4 beats @ 16

s3 >> loop('808s', P[:4], sample=1, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 4 beats @ 32

s3 >> loop('808s', P[:4], sample=2, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 4 beats @ 48

s3 >> loop('808s', P[:4], sample=3, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 4 beats @ 72

s3 >> loop('808s', P[:4], sample=4, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 4 beats @ 88

s3 >> loop('808s', P[:4], sample=5, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 4 beats @ 104

s3 >> loop('808s', P[:4], sample=6, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 4 beats @ 224

s3 >> loop('808s', P[:4], sample=7, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 4 beats @ 240

s3 >> loop('808s', P[:4], sample=8, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 4 beats @ 272

s3 >> loop('808s', P[:4], sample=9, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 4 beats @ 288

s3 >> loop('808s', P[:4], sample=10, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 4 beats @ 304

s3 >> loop('808s', P[:4], sample=11, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 4 beats @ 312

s3.stop()

s4 >> loop('Rhythm_Guitars', P[:20], sample=0, amp=Pvar([1,1],[20]), dur=1, tempo=110) # 17 beats @ 16

s4 >> loop('Rhythm_Guitars', P[:80], sample=1, amp=Pvar([1,1],[80]), dur=1, tempo=110) # 77 beats @ 44

s4 >> loop('Rhythm_Guitars', P[:80], sample=2, amp=Pvar([1,1],[80]), dur=1, tempo=110) # 77 beats @ 132

s4 >> loop('Rhythm_Guitars', P[:16], sample=3, amp=Pvar([1,1],[16]), dur=1, tempo=110) # 16 beats @ 223

s4 >> loop('Rhythm_Guitars', P[:32], sample=4, amp=Pvar([1,1],[32]), dur=1, tempo=110) # 29 beats @ 240

s4 >> loop('Rhythm_Guitars', P[:48], sample=5, amp=Pvar([1,1],[48]), dur=1, tempo=110) # 48 beats @ 272

s4.stop()

s5 >> loop('Backing_Vocals', P[:4], sample=0, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 4 beats @ 72

s5 >> loop('Backing_Vocals', P[:4], sample=1, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 4 beats @ 80

s5 >> loop('Backing_Vocals', P[:4], sample=2, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 4 beats @ 88

s5 >> loop('Backing_Vocals', P[:4], sample=3, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 4 beats @ 96

s5 >> loop('Backing_Vocals', P[:4], sample=4, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 4 beats @ 160

s5 >> loop('Backing_Vocals', P[:4], sample=5, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 4 beats @ 168

s5 >> loop('Backing_Vocals', P[:4], sample=6, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 4 beats @ 176

s5 >> loop('Backing_Vocals', P[:4], sample=7, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 4 beats @ 184

s5 >> loop('Backing_Vocals', P[:4], sample=8, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 3 beats @ 240

s5 >> loop('Backing_Vocals', P[:4], sample=9, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 3 beats @ 247

s5 >> loop('Backing_Vocals', P[:4], sample=10, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 3 beats @ 256

s5 >> loop('Backing_Vocals', P[:4], sample=11, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 4 beats @ 263

s5 >> loop('Backing_Vocals', P[:4], sample=12, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 4 beats @ 272

s5 >> loop('Backing_Vocals', P[:4], sample=13, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 4 beats @ 280

s5 >> loop('Backing_Vocals', P[:4], sample=14, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 4 beats @ 288

s5 >> loop('Backing_Vocals', P[:4], sample=15, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 4 beats @ 296

s5.stop()

s6 >> loop('Bass_Guitar', P[:52], sample=0, amp=Pvar([1,1],[52]), dur=1, tempo=110) # 50 beats @ 16

s6 >> loop('Bass_Guitar', P[:88], sample=1, amp=Pvar([1,1],[88]), dur=1, tempo=110) # 87 beats @ 67

s6 >> loop('Bass_Guitar', P[:56], sample=2, amp=Pvar([1,1],[56]), dur=1, tempo=110) # 55 beats @ 155

s6 >> loop('Bass_Guitar', P[:12], sample=3, amp=Pvar([1,1],[12]), dur=1, tempo=110) # 11 beats @ 216

s6 >> loop('Bass_Guitar', P[:4], sample=4, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 3 beats @ 228

s6 >> loop('Bass_Guitar', P[:4], sample=5, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 3 beats @ 232

s6 >> loop('Bass_Guitar', P[:4], sample=6, amp=Pvar([1,1],[4]), dur=1, tempo=110) # 3 beats @ 236

s6 >> loop('Bass_Guitar', P[:32], sample=7, amp=Pvar([1,1],[32]), dur=1, tempo=110) # 29 beats @ 240

s6 >> loop('Bass_Guitar', P[:48], sample=8, amp=Pvar([1,1],[48]), dur=1, tempo=110) # 48 beats @ 272

s6.stop()
