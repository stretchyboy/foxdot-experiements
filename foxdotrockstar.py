import traceback
import sys
import timeout_decorator
import functools
from rockstarpy.transpile import Transpiler
import logging

# create logger with 'spam_application'
logger = logging.getLogger('fdrs')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(ch)

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class UpdaterHandler(FileSystemEventHandler):
    def __init__(self, filename, namespace=None, printname=None):
        self.logger = logging.getLogger('fdrs')
        self.logger.info('Creating an instance of UpdaterHandler')

        self.do_rsf = functools.partial(rsf, filename, namespace=namespace, printname=printname)


    def on_any_event(self, event):
        self.logger.info("An event")
        self.logger.info(event.event_type)

        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            self.logger.info( "Received created event - %s." % event.src_path)

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            self.logger.info( "Received modified event - %s." % event.src_path)
            # TODO check its the right file ??
            self.do_rsf()


observer = Observer()
observer.start()
#observer.stop()

transpiler = Transpiler()

def extract(dct, namespace=None):
    if not namespace: namespace = globals()
    namespace.update(dct)

def rsf(filename, namespace=None, printname=None):
    logger.info("Running rsf "+filename)
    f = open(filename, "r")
    lyrics = f.read()
    logger.info("lyrics length "+str(len(lyrics)))
    rs(lyrics, namespace, printname)

def stalk(filename, namespace=None, printname=None):
    rsf(filename, namespace, printname)
    event_handler = UpdaterHandler(filename, namespace, printname)
    observer.schedule(event_handler, ".")

#@timeout_decorator.timeout(5)
def rs(lyrics, namespace=None, printname=None):
    if printname:
        converted_code = printname+" = [] \n"
    else:
        converted_code = ""

    for line in lyrics.split("\n"):
        converted_line = transpiler.transpile_line(line+"\n")
        if printname:
            converted_line = converted_line.replace("print",printname+".append")
        converted_code += converted_line

    if printname:
        converted_code +="print("+printname+")"

    print(converted_code)

    try:
        exec(converted_code)
        extract(locals(), namespace)
    except SyntaxError:
        print ("Your words don't mean much too me. (Syntax error)")
    #return converted_code

if __name__ == '__main__':
    rs('''
Tommy was a docker
While Tommy ain't nothing
Scream Tommy
Knock Tommy down
''', locals())
