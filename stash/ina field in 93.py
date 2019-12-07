d1 >> play("<x (x-X-) >", amp=3, room=[1, 0.5], mix=[0.5,.5,1])

d2 >> play(P["<- [Xx] ><(^ [**] -) (*&^-) *>"].bubble(), amp=2)


Scale.default = Scale.major

b1 >> bass(P[0,4,5,3], dur=P[2,1,1,2], bits=12, striate=P[0,8,4])

p1 >> pads(dur=PDur(PRange(2,10),[10,12])).follow(b1) + (P[1,2,1]^P(0,2,1).bubble())

p1.every(10, "reverse")

p1.every(3, "stutter", 4, oct=4, pan=[-1,1])
