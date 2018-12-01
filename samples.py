Clock.bpm=110

d1 >> play("x  -")

d1 >> play("x  <*->")

d1 >> play("x  <*-[--]>")

d1 >> play("<xxxx[xx]>  <*-[--]>")

d1 >> play("<$$xx[---%]>  <*-[--]>").every(4, "reverse").every(3, "stutter")

p1 >> play("* $ * x-").every(4, "reverse").every(7, "stutter")


s1 >> loop('Bullet/808s', sample=18, dur=8) # 2 beats @ 312

s2 >> loop('Bullet/Backing_Vocals', sample=1, dur=2, slide=0.5, slidedelay=0.5) # 2 beats @ 72

s2 >> loop('Bullet/Backing_Vocals', sample=2, dur=2) # 2 beats @ 80

s2 >> loop('Bullet/Backing_Vocals', sample=3, dur=2) # 2 beats @ 88

s2 >> loop('Bullet/Backing_Vocals', sample=4, dur=2) # 2 beats @ 96

s2 >> loop('Bullet/Backing_Vocals', sample=5, dur=2) # 2 beats @ 160

s2 >> loop('Bullet/Backing_Vocals', sample=6, dur=2) # 2 beats @ 168

s2 >> loop('Bullet/Backing_Vocals', sample=7, dur=2) # 2 beats @ 176

s2 >> loop('Bullet/Backing_Vocals', sample=8, dur=2) # 2 beats @ 184

s2 >> loop('Bullet/Backing_Vocals', sample=9, dur=1) # 1 beats @ 240

s2 >> loop('Bullet/Backing_Vocals', sample=10, dur=1) # 1 beats @ 247

s2 >> loop('Bullet/Backing_Vocals', sample=11, dur=1) # 1 beats @ 256

s2 >> loop('Bullet/Backing_Vocals', sample=12, dur=2) # 2 beats @ 263

s2 >> loop('Bullet/Backing_Vocals', sample=13, dur=2) # 2 beats @ 272

s2 >> loop('Bullet/Backing_Vocals', sample=14, dur=2) # 2 beats @ 280

s2.stop()

s2 >> loop('Bullet/Backing_Vocals', sample=15, dur=16) # 2 beats @ 288

s2 >> loop('Bullet/Backing_Vocals', sample=16, dur=8, crush=0.5, bits=8) # 2 beats @ 296

s3 >> loop('Bullet/Bass_Guitar', sample=1, dur=48) # 48 beats @ 16

s3 >> loop('Bullet/Bass_Guitar', sample=2, dur=85) # 85 beats @ 67

s3 >> loop('Bullet/Bass_Guitar', sample=3, dur=53) # 53 beats @ 155

s3 >> loop('Bullet/Bass_Guitar', sample=4, dur=9) # 9 beats @ 216

s3 >> loop('Bullet/Bass_Guitar', sample=5, dur=1) # 1 beats @ 228

s3 >> loop('Bullet/Bass_Guitar', sample=6, dur=1) # 1 beats @ 232

s3 >> loop('Bullet/Bass_Guitar', sample=7, dur=1) # 1 beats @ 236

s3 >> loop('Bullet/Bass_Guitar', sample=8, dur=27) # 27 beats @ 240

s3 >> loop('Bullet/Bass_Guitar', sample=9, dur=46) # 46 beats @ 272

s4 >> loop('Bullet/Bullet_Vocals_MAIN', sample=1, dur=30) # 30 beats @ 33

s4 >> loop('Bullet/Bullet_Vocals_MAIN', sample=2, dur=37) # 37 beats @ 65

s4 >> loop('Bullet/Bullet_Vocals_MAIN', sample=3, dur=37) # 37 beats @ 120

s4 >> loop('Bullet/Bullet_Vocals_MAIN', sample=4, dur=32) # 32 beats @ 159

s4 >> loop('Bullet/Bullet_Vocals_MAIN', sample=5, dur=0) # 0 beats @ 207

s4 >> loop('Bullet/Bullet_Vocals_MAIN', sample=6, dur=3, vib=4, vibdepth=0.4) # 3 beats @ 212

s4 >> loop('Bullet/Bullet_Vocals_MAIN', sample=7, dur=8) # 3 beats @ 220

s4 >> loop('Bullet/Bullet_Vocals_MAIN', sample=8, dur=4) # 4 beats @ 228

s4 >> loop('Bullet/Bullet_Vocals_MAIN', sample=9, dur=8) # 1 beats @ 235

s4 >> loop('Bullet/Bullet_Vocals_MAIN', sample=10, dur=PDur(4,64), chop=8) # 64 beats @ 238

c4 >> loop('Bullet/Bullet_Vocals_MAIN', sample=9, dur=32, echo=2) # 4 beats @ 315

s5 >> loop('Bullet/Lead_Guitars', sample=1, dur=29) # 29 beats @ 73

s5 >> loop('Bullet/Lead_Guitars', sample=2, dur=29, drive=0.1) # 29 beats @ 161

s5 >> loop('Bullet/Lead_Guitars', sample=3, dur=PDur(5,30), 	coarse=4) # 29 beats @ 273

s3.stop()

s6 >> loop('Bullet/Rhythm_Guitars', sample=1, dur=15) # 15 beats @ 16

s6 >> loop('Bullet/Rhythm_Guitars', sample=2, dur=75) # 75 beats @ 44

s6 >> loop('Bullet/Rhythm_Guitars', sample=3, dur=PDur(31,75), chop=4, hpf=linvar([0,2000],32)) # 75 beats @ 132

s6 >> loop('Bullet/Rhythm_Guitars', sample=4, dur=14) # 14 beats @ 223

s6 >> loop('Bullet/Rhythm_Guitars', sample=5, dur=27) # 27 beats @ 240

s6 >> loop('Bullet/Rhythm_Guitars', sample=6, dur=PDur(20,46), chop=4) # 46 beats @ 272

