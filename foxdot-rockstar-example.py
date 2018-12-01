from foxdotrockstar import *

#Transpile the following rockstar code into python and run it
#code runs between the '''s 
#in the rockstar code ()s are comments
rs('''
Papa was a rolling stone (Papa = 175)

(loops down from 16)
Tommy was a docker (Tommy = 16)
While Tommy aint 0, (should be nothing, but there is a bug )
Scream Tommy 
Knock Tommy down (Tommy --)

(Finds the remainder of first num divided by second)
Midnight takes your heart and your soul
While your heart is as high as your soul
Put your heart without your soul into your heart

Give back your heart

(adds the 2 parameters together)
Lovin takes my hope and my strength
Give back my hope with my strength

''', locals(),"tommies") # brutal bit of python to get the variables and functions out of the Rockstar
#the "tommies" takes alls the whispers and shouts etc. and puts them into an array called tommies

Clock.bpm = Midnight(Papa, 200) # sets bpm to 175%200  

# Another brutal bit of python to use Lovin in an .every on a Player object
@PlayerMethod
def loving(self):
    global Clock
    Clock.bpm = Lovin(Clock.bpm, 2)  


p1 >> pluck([0,4]).every(3, "loving")

d1 >> play("x-o-").every(Pvar(tommies), "stutter")
# And cancel it with
#p1.never("loving")

