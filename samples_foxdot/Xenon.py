##################################################################################
# Created with stems2foxdot by stretch
# From Xenon
# © Rabbit Junk with Permission
###################################################################################
Samples.addPath("/home/meggleton/Projects/algorave/stems/Xenon")

Clock.bpm = 180

s1 >> loop('xenon_sum_grrrl_01', P[:8], sample=0, amp=Pvar([1,1],[8]), dur=1, tempo=130) # 5 beats @ 75

s1 >> loop('xenon_sum_grrrl_01', P[:4], sample=1, amp=Pvar([1,1],[4]), dur=1, tempo=130) # 2 beats @ 91

s1 >> loop('xenon_sum_grrrl_01', P[:4], sample=2, amp=Pvar([1,1],[4]), dur=1, tempo=130) # 4 beats @ 209

s1 >> loop('xenon_sum_grrrl_01', P[:12], sample=3, amp=Pvar([1,1],[12]), dur=1, tempo=130) # 11 beats @ 216

s1 >> loop('xenon_sum_grrrl_01', P[:4], sample=4, amp=Pvar([1,1],[4]), dur=1, tempo=130) # 4 beats @ 234

s1 >> loop('xenon_sum_grrrl_01', P[:12], sample=5, amp=Pvar([1,1],[12]), dur=1, tempo=130) # 11 beats @ 348

s1 >> loop('xenon_sum_grrrl_01', P[:8], sample=6, amp=Pvar([1,1],[8]), dur=1, tempo=130) # 7 beats @ 364

s1.stop()

s2 >> loop('xenon_vocals_01', P[:8], sample=0, amp=Pvar([1,1],[8]), dur=1, tempo=130) # 6 beats @ 108

s2 >> loop('xenon_vocals_01', P[:4], sample=1, amp=Pvar([1,1],[4]), dur=1, tempo=130) # 3 beats @ 118

s2 >> loop('xenon_vocals_01', P[:8], sample=2, amp=Pvar([1,1],[8]), dur=1, tempo=130) # 7 beats @ 123

s2 >> loop('xenon_vocals_01', P[:4], sample=3, amp=Pvar([1,1],[4]), dur=1, tempo=130) # 3 beats @ 136

s2 >> loop('xenon_vocals_01', P[:4], sample=4, amp=Pvar([1,1],[4]), dur=1, tempo=130) # 4 beats @ 144

s2 >> loop('xenon_vocals_01', P[:8], sample=5, amp=Pvar([1,1],[8]), dur=1, tempo=130) # 5 beats @ 158

s2 >> loop('xenon_vocals_01', P[:8], sample=6, amp=Pvar([1,1],[8]), dur=1, tempo=130) # 6 beats @ 169

s2 >> loop('xenon_vocals_01', P[:8], sample=7, amp=Pvar([1,1],[8]), dur=1, tempo=130) # 7 beats @ 239

s2 >> loop('xenon_vocals_01', P[:8], sample=8, amp=Pvar([1,1],[8]), dur=1, tempo=130) # 7 beats @ 247

s2 >> loop('xenon_vocals_01', P[:8], sample=9, amp=Pvar([1,1],[8]), dur=1, tempo=130) # 7 beats @ 255

s2 >> loop('xenon_vocals_01', P[:12], sample=10, amp=Pvar([1,1],[12]), dur=1, tempo=130) # 9 beats @ 263

s2 >> loop('xenon_vocals_01', P[:8], sample=11, amp=Pvar([1,1],[8]), dur=1, tempo=130) # 6 beats @ 275

s2 >> loop('xenon_vocals_01', P[:8], sample=12, amp=Pvar([1,1],[8]), dur=1, tempo=130) # 7 beats @ 292

s2 >> loop('xenon_vocals_01', P[:8], sample=13, amp=Pvar([1,1],[8]), dur=1, tempo=130) # 8 beats @ 300

s2 >> loop('xenon_vocals_01', P[:8], sample=14, amp=Pvar([1,1],[8]), dur=1, tempo=130) # 8 beats @ 371

s2 >> loop('xenon_vocals_01', P[:16], sample=15, amp=Pvar([1,1],[16]), dur=1, tempo=130) # 15 beats @ 379

s2 >> loop('xenon_vocals_01', P[:12], sample=16, amp=Pvar([1,1],[12]), dur=1, tempo=130) # 11 beats @ 395

s2 >> loop('xenon_vocals_01', P[:12], sample=17, amp=Pvar([1,1],[12]), dur=1, tempo=130) # 10 beats @ 411

s2 >> loop('xenon_vocals_01', P[:12], sample=18, amp=Pvar([1,1],[12]), dur=1, tempo=130) # 9 beats @ 427

s2 >> loop('xenon_vocals_01', P[:8], sample=19, amp=Pvar([1,1],[8]), dur=1, tempo=130) # 6 beats @ 441

s2 >> loop('xenon_vocals_01', P[:8], sample=20, amp=Pvar([1,1],[8]), dur=1, tempo=130) # 5 beats @ 458

s2 >> loop('xenon_vocals_01', P[:12], sample=21, amp=Pvar([1,1],[12]), dur=1, tempo=130) # 9 beats @ 468

s2.stop()

s3.stop()

s4 >> loop('xenon_guitar_130bpm', P[:20], sample=0, amp=Pvar([1,1],[20]), dur=1, tempo=130) # 17 beats @ 12

s4 >> loop('xenon_guitar_130bpm', P[:16], sample=1, amp=Pvar([1,1],[16]), dur=1, tempo=130) # 15 beats @ 30

#######
s4 >> loop('xenon_guitar_130bpm', P[;20], sample=2, amp=Pvar([1,1],[20]), dur=1, tempo=130) # 17 beats @ 144

s4 >> loop('xenon_guitar_130bpm', P[:20], sample=3, amp=Pvar([1,1],[20]), dur=1, tempo=130) # 17 beats @ 162

s4 >> loop('xenon_guitar_130bpm', P[:8], sample=4, amp=Pvar([1,1],[8]), dur=1, tempo=130) # 7 beats @ 215

s4 >> loop('xenon_guitar_130bpm', P[:4], sample=5, amp=Pvar([1,1],[4]), dur=1, tempo=130) # 3 beats @ 224

s4 >> loop('xenon_guitar_130bpm', P[:20], sample=6, amp=Pvar([1,1],[20]), dur=1, tempo=130) # 18 beats @ 233

s4 >> loop('xenon_guitar_130bpm', P[:68], sample=7, amp=Pvar([1,1],[68]), dur=1, tempo=130) # 66 beats @ 277

s4 >> loop('xenon_guitar_130bpm', P[:12], sample=8, amp=Pvar([1,1],[12]), dur=1, tempo=130) # 9 beats @ 346

s4 >> loop('xenon_guitar_130bpm', P[:4], sample=9, amp=Pvar([1,1],[4]), dur=1, tempo=130) # 4 beats @ 356

s4 >> loop('xenon_guitar_130bpm', P[:4], sample=10, amp=Pvar([1,1],[4]), dur=1, tempo=130) # 2 beats @ 362

s4 >> loop('xenon_guitar_130bpm', P[:8], sample=11, amp=Pvar([1,1],[8]), dur=1, tempo=130) # 7 beats @ 364

s4 >> loop('xenon_guitar_130bpm', P[:12], sample=12, amp=Pvar([1,1],[12]), dur=1, tempo=130) # 9 beats @ 378

s4 >> loop('xenon_guitar_130bpm', P[:4], sample=13, amp=Pvar([1,1],[4]), dur=1, tempo=130) # 4 beats @ 388

s4 >> loop('xenon_guitar_130bpm', P[:4], sample=14, amp=Pvar([1,1],[4]), dur=1, tempo=130) # 2 beats @ 394

s4 >> loop('xenon_guitar_130bpm', P[:8], sample=15, amp=Pvar([1,1],[8]), dur=1, tempo=130) # 8 beats @ 396

s4 >> loop('xenon_guitar_130bpm', P[:64], sample=16, amp=Pvar([1,1],[64]), dur=1, tempo=130) # 63 beats @ 413

s4.stop()

s5 >> loop('xenon_keys_01', P[:4], sample=0, amp=Pvar([1,1],[4]), dur=1, tempo=130) # 2 beats @ 97

s5 >> loop('xenon_keys_01', P[:4], sample=1, amp=Pvar([1,1],[4]), dur=1, tempo=130) # 2 beats @ 102

s5 >> loop('xenon_keys_01', P[2,4,5,2,1], sample=2, amp=Pvar([1,1],[8]), dur=1, tempo=130) # 5 beats @ 108

s5 >> loop('xenon_keys_01', P[:4], sample=3, amp=Pvar([1,1],[4]), dur=1, tempo=130) # 2 beats @ 209

s5 >> loop('xenon_keys_01', P[:4], sample=4, amp=Pvar([1,1],[4]), dur=1, tempo=130) # 2 beats @ 225

s5 >> loop('xenon_keys_01', P[:4], sample=5, amp=Pvar([1,1],[4]), dur=1, tempo=130) # 2 beats @ 229

s5 >> loop('xenon_keys_01', P[:4], sample=6, amp=Pvar([1,1],[4]), dur=1, tempo=130) # 4 beats @ 233

s5 >> loop('xenon_keys_01', P[:20], sample=7, amp=Pvar([1,1],[20]), dur=1, tempo=130) # 18 beats @ 240

s5 >> loop('xenon_keys_01', P[:4], sample=8, amp=Pvar([1,1],[4]), dur=1, tempo=130) # 3 beats @ 308

s5 >> loop('xenon_keys_01', P[:4], sample=9, amp=Pvar([1,1],[4]), dur=1, tempo=130) # 3 beats @ 314

s5 >> loop('xenon_keys_01', P[:8], sample=10, amp=Pvar([1,1],[8]), dur=1, tempo=130) # 6 beats @ 323

s5 >> loop('xenon_keys_01', P[:4], sample=11, amp=Pvar([1,1],[4]), dur=1, tempo=130) # 3 beats @ 330

s5 >> loop('xenon_keys_01', P[:4], sample=12, amp=Pvar([1,1],[4]), dur=1, tempo=130) # 2 beats @ 341

s5 >> loop('xenon_keys_01', P[:4], sample=13, amp=Pvar([1,1],[4]), dur=1, tempo=130) # 2 beats @ 345

s5 >> loop('xenon_keys_01', P[:4], sample=14, amp=Pvar([1,1],[4]), dur=1, tempo=130) # 2 beats @ 357

s5 >> loop('xenon_keys_01', P[:4], sample=15, amp=Pvar([1,1],[4]), dur=1, tempo=130) # 2 beats @ 361

s5 >> loop('xenon_keys_01', P[:4], sample=16, amp=Pvar([1,1],[4]), dur=1, tempo=130) # 3 beats @ 365

s5 >> loop('xenon_keys_01', P[:32], sample=17, amp=Pvar([1,1],[32]), dur=1, tempo=130) # 32 beats @ 373

s5 >> loop('xenon_keys_01', P[:68], sample=18, amp=Pvar([1,1],[68]), dur=1, tempo=130) # 68 beats @ 412

s5.stop()

s6.stop()
