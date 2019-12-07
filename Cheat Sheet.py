Scale.default = Scale.major

start=nextbar

print(SynthDefs)

bmp = linvar([180,220], [32, inf], start=nextbar)
Clock.update_tempo(bmp)

amp=linvar([1,0], [32, inf], start=nextbar)

#chords  + (0,1,2)

'''
noise great for quick effect
varsaw,
lazer =pewpew
growl jungly talking drum
bass end of piano
dirt slightly scuzzy keys
rave
scatter quite quite
charm
bell
gong a bit more tublar bell y at the top end_b
soprano waily
dub dubby
viola ok
scratch record scratch quite quire
klank',
feel' floaty
glass',very light
soft' soft bells
quin', synthy
pluck', plucky Syntt
spark', Synth
blip', like
ripple',
creep' long saw,
orient', not very chinesem
zap', short
marimba',
fuzz', aggresive
bug', jittery
pulse', 'saw',
snick', tapping noise
twang', eeeurgh
karp',korean harp?
arpy', 'nylon',
donk', hitting a pipe
squish', wet pipe??
swell', brassish
razz',
sitar'  trangy
star',
jbass',
sawbass',lots louder than jbass
prophet', 80's
pads',
pasha',
ambi',round
space' like,
keys',
dbass',
sinepad' xylo with the edge]
