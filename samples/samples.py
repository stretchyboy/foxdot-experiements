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

    def getClosestSample(self, midi):
        sampleid = self.notes_map[midi]
        if(sampleid):
            return Sample[sampleid]
        return False

    def getNotePlayInfo(self, midi):
        sample = self.getClosestSample(midi)
        if(sample):
            transform = sample.getTransform(midi)
            return (sample.filename, transform)
        return False

def getFileName(name, sample=0):
    return '{0:03d}_'.format(sample)+name
    #return '{0:03d}_'.format(sample)+("".join(x for x in name if x.isalnum()).lower()) + ".wav"

class Sample(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    filename = Required(str)
    sample = Required(int)
    tone = Required(Tone)
    length = Optional(int)
    bpm = Optional(int)
    midi = Required(int)
    notes = Set('Note')
    source = Optional(str)

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
        bpm = None,
        midi = None,
        notename = None,
        octave = None
     ):

        name = os.path.basename(inputfilepath)
        #samples = Sample.select(tone=tone).count()
        sample = select(s for s in Sample if s.tone == tone).count()

        print("sample", sample)
        filename = getFileName(name, sample)
        print("filename", filename)

        if(notename and octave):
            p = pitch.Pitch(notename)
            p.octave = octave
            midi = p.midi

        super().__init__(
            tone = tone,
            name = name,
            midi = midi,
            bpm = bpm,
            sample=sample,
            filename=filename
            )

        dir = tone.getFolderPath()
        path = os.path.join(dir, filename)
        copyfile(inputfilepath, path)

    def after_delete(self):
        self.tone.makeMap()

    def after_insert(self):
        self.tone.makeMap()

    def after_update():
        self.tone.makeMap()

class Note(db.Entity):
    id = PrimaryKey(int, auto=True)
    sample = Required(Sample)
    startatbeat = Required(int)
    endatbeat = Required(int)
    midi = Required(int)


db.generate_mapping(create_tables=True)

@db_session
def get_or_create_tone(name):
    if Tone.exists(name=name):
        return Tone.get(name=name)
    return Tone(name=name)

@db_session
def get_or_create_tone_from_sample(
    inputfilepath=None,
    bpm = None,
    midi = None,
    notename = None,
    octave = None):

    tonefolderpath = os.path.dirname(inputfilepath)
    tonefolder = os.path.basename(tonefolderpath)
    #print("tonefolder", tonefolder)

    t = get_or_create_tone(tonefolder)
    s = get_or_create_sample(
        inputfilepath=inputfilepath,
        tone=t,
        bpm = bpm,
        midi = midi,
        notename = notename,
        octave = octave)

    #t.makeMap()

    return t,s

@db_session
def get_or_create_sample(
    inputfilepath=None,
    tone=None,
    bpm = None,
    midi = None,
    notename = None,
    octave = None):

    if(notename and octave):
        p = pitch.Pitch(notename)
        p.octave = octave
        midi = p.midi

    if Sample.exists(tone=tone, midi=midi):
        return Sample.get(tone=tone, midi=midi)
    return Sample(
        inputfilepath=inputfilepath,
        tone=tone,
        bpm = bpm,
        midi = midi,
        notename = notename,
        octave = octave)

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Load Samplesfor FoxDot.'
        )
    parser.add_argument('-p','--path', nargs='?', metavar='PATH', type=str,
                        help='inputfilepath')
    #parser.add_argument('-f','--file', nargs='?', type=argparse.FileType('r'),
    #                 default=sys.stdin)

    parser.add_argument('-b','--bpm', type=int, nargs='?', default=110,
                        help='BPM of sample')

    parser.add_argument('-n','--note', type=str, nargs='?', default=None,
                        help='Note name of sample')

    parser.add_argument('-o','--octave', type=int, nargs='?', default=None,
                        help='Octave of sample')

    parser.add_argument('-m','--midi', type=int, nargs='?', default=None,
                        help='Midi number of sample')

    parser.add_argument('-t','--test', action='store_true', help="Run test suite")
    parser.add_argument('-l','--list', action='store_true', help="List available tones")

    # TODO: add -t for test
    # TODO: add -l for list get_or_create_tone_from_sample

    args = parser.parse_args()


    if(args.path):
        with db_session:
            t, s = get_or_create_tone_from_sample(
                inputfilepath = os.path.abspath(args.path),
                bpm=args.bpm,
                notename = args.note,
                octave = args.octave,
                midi=args.midi
            )

        with db_session:
            print(t.getNotePlayInfo(60))

    elif(args.test):
        with db_session:
            t, s = get_or_create_tone_from_sample(
                inputfilepath = "/home/meggleton/Downloads/Fingered (bridge pickup) Rickenbacker bass (4001 - 1974)/163021__project16__d-3-pp.wav",
                notename = "D",
                octave = 3)

            t, s = get_or_create_tone_from_sample(
                inputfilepath = "/home/meggleton/Downloads/Fingered (bridge pickup) Rickenbacker bass (4001 - 1974)/162995__project16__f-3-pp.wav",
                notename = "F",
                octave = 3)

            t, s = get_or_create_tone_from_sample(
                inputfilepath = "/home/meggleton/Downloads/Fingered (bridge pickup) Rickenbacker bass (4001 - 1974)/162969__project16__a2-pp.wav",
                notename = "A",
                octave = 2)

            print(t.getNotePlayInfo(60))

    elif(args.list):
        print('List')

    else:
        parser.print_usage()

if __name__ == "__main__":
    main()
