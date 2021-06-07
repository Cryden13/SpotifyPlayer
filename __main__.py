from warnings import simplefilter
from commandline import openfile
from winnotify import playSound
from pathlib import Path
from sys import argv
import logging

try:
    from .lib.constants import SPOTIFY_EXE, SPOTIFY_AHK
    from .src.changeshortcut import changeShortcut
    from .player import GUI
except ImportError:
    from subprocess import run
    pth = Path(__file__).parent
    run(['py', '-m', pth.name, 'console'], cwd=pth.parent)
    raise SystemExit


def main():
    logfile = Path(__file__).parent.joinpath('lib', 'logging.log')
    logging.basicConfig(filename=logfile,
                        level=logging.DEBUG,
                        format='\n[%(asctime)s] %(funcName)s - %(levelname)s:',
                        datefmt='%m/%d/%Y %I:%M:%S%p')
    changeShortcut(SPOTIFY_EXE)
    simplefilter('ignore', category=UserWarning)
    try:
        gui = GUI()
        gui.mainloop()
    except Exception:
        logging.exception('')
        raise
    finally:
        if logfile.read_text() and argv[-1] != 'console':
            playSound()
            openfile(logfile)
        changeShortcut(SPOTIFY_AHK)


if __name__ == '__main__':
    main()
