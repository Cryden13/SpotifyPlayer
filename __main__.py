from contextlib import redirect_stdout
from warnings import simplefilter
from traceback import format_exc
from commandline import openfile
from winnotify import playSound
from datetime import datetime
from pathlib import Path
from sys import argv

try:
    from .lib.constants import SPOTIFY_EXE, SPOTIFY_AHK
    from .src.changeshortcut import changeShortcut
    from .player import GUI
except ImportError:
    from subprocess import run
    pth = Path(__file__).parent
    run(['py', '-m', pth.name, 'console'], cwd=pth.parent)
    raise SystemExit


class main:
    def __init__(self):
        if argv[-1] == 'console':
            self.run()
        else:
            self.doLog()
        changeShortcut(SPOTIFY_AHK)

    def run(self):
        simplefilter('ignore', category=UserWarning)
        changeShortcut(SPOTIFY_EXE)
        gui = GUI()
        gui.mainloop()

    def doLog(self):
        errlog = Path(__file__).parent.joinpath('lib', 'errorlog.txt')
        errlog.unlink(missing_ok=True)
        with errlog.open('w') as log:
            with redirect_stdout(log):
                try:
                    self.run()
                except:
                    log.write(f'\n{datetime.now()}\n{format_exc()}')
        if errlog.read_text():
            playSound()
            openfile(errlog)
        else:
            errlog.unlink(missing_ok=True)


if __name__ == '__main__':
    main()
