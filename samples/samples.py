from pony.orm import *
from music21 import pitch
import os
from shutil import copyfile


db = Database()
#set_sql_debug(True)

basefolder = os.path.join(os.path.expanduser("~"),".foxdot_samples")
if not os.path.exists(basefolder):
    os.makedirs(basefolder)

db.bind(provider='sqlite', filename=os.path.join(basefolder, 'database.sqlite'), create_db=True)

def getMidiByName(note, oct=4):
    p1 = pitch.Pitch(note)
    p1.octave = oct
    print(p1.midi)
    return p1.midi

class Tone(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    samples = Set('Sample')
    notes_map = Optional(Json)

    def getFolderPath(self):
        dir = "".join(x for x in self.name if x.isalnum())
        directory = os.path.join(os.path.expanduser("~"),".foxdot_samples", dir)
        if not os.path.exists(directory):
            os.makedirs(directory)
        return directory

    def makeMap(self):
        map = []
        for midi in range(120):
            #loop around samples
            lowscore = 100000000
            lowsample = None
            for s in self.samples:
                currscore = s.score(midi)
                #print("currscore", currscore,lowscore)
                if(currscore < lowscore):
                    lowscore = currscore
                    lowsample = s.get_pk()
            map.append(lowsample)
        self.notes_map = map

    def getSample(self, midi):
        sampleid = self.notes_map[midi]
        return self.samples[sampleid]


class Sample(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    tone = Required(Tone)
    length = Optional(int)
    bmp = Optional(int)
    midi = Required(int)
    notes = Set('Note')
    source = Optional(str)

    def getFilePath(self):
        file = "".join(x for x in self.name if x.isalnum())
        dir = self.tone.getFolderPath()
        path = os.path.join(dir, file)
        return path

    def score(self, midi):
        densityscore = 0
        if( self.midi > midi):
            densityscore = 5
        return densityscore +(10*abs(self.midi - midi))

    def getTransform(self, midi):
        return self.midi - midi

    def __init__(self,
        inputfilepath=None,
        tone=None,
        bmp = None,
        midi = None,
        notename = None,
        octave = None
     ):
        name = os.path.basename(inputfilepath)
        #print("name", name)
        if(notename and octave):
            p = pitch.Pitch(notename)
            p.octave = octave
            midi = p.midi
        super().__init__(
            tone = tone,
            name = name,
            midi=midi,
            bmp = bmp
            )
        file = "".join(x for x in name if x.isalnum())
        dir = tone.getFolderPath()
        path = os.path.join(dir, file)
        copyfile(inputfilepath, path)



class Note(db.Entity):
    id = PrimaryKey(int, auto=True)
    sample = Required(Sample)
    beat = Required(int)
    note = Required(int)


db.generate_mapping(create_tables=True)




with db_session:
    t = Tone(name='Fingered (bridge pickup) Rickenbacker bass (4001 - 1974)')
    filepath = "/home/meggleton/Downloads/Fingered (bridge pickup) Rickenbacker bass (4001 - 1974)/163021__project16__d-3-pp.wav"
    s = Sample(inputfilepath=filepath,
    tone=t,
    notename = "D",
    octave = 3)

    filepath = "/home/meggleton/Downloads/Fingered (bridge pickup) Rickenbacker bass (4001 - 1974)/162995__project16__f-3-pp.wav"
    s = Sample(inputfilepath=filepath,
    tone=t,
    notename = "F",
    octave = 3)


    filepath = "/home/meggleton/Downloads/Fingered (bridge pickup) Rickenbacker bass (4001 - 1974)/162969__project16__a2-pp.wav"
    s = Sample(inputfilepath=filepath,
    tone=t,
    notename = "A",
    octave = 2)

with db_session:
    t = Tone[1]
    t.makeMap()
