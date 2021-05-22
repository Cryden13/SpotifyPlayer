from collections import OrderedDict as oDict
from re import split as re_split
from win32gui import FindWindow
from pathlib import Path
from win32con import (
    SWP_NOACTIVATE,
    SWP_NOMOVE,
    SWP_NOSIZE,
    SWP_SHOWWINDOW
)
from configparser import (
    ExtendedInterpolation as ExtInterp,
    ConfigParser
)
from win32api import (
    GetMonitorInfo,
    MonitorFromPoint
)
from typing import (
    Optional as O,
    TYPE_CHECKING
)
from os import (
    environ,
    chdir
)

chdir(Path(__file__).parents[1])

cfgfile = Path(__file__).parent.with_name('config.cfg')
cfg = ConfigParser(defaults=environ,
                   interpolation=ExtInterp())
cfg.optionxform = str
cfg.read_file(open(cfgfile))

# path vars
sct = 'Paths'
SPOTIFY_EXE = str(Path(cfg.get(sct, 'spotify_exe')).absolute())
SPOTIFY_AHK = str(Path(cfg.get(sct, 'ahk_exe')).absolute())
SPOTIFY_LINK = str(Path(cfg.get(sct, 'spotify_link')).absolute())

# text vars
sct = 'Text'
SPOTIFY_TITLE = cfg.get(sct, 'initial_spotify_title')
PLAYER_TITLE = cfg.get(sct, 'player_title')
lbltxt = re_split(pattern=r' *\| *',
                  string=cfg.get(sct, 'player_startup_text'))
STARTUP_TEXT_L = f'{lbltxt[0]:^15}'
STARTUP_TEXT_R = f'{lbltxt[-1]:^15}'
lbltxt = re_split(pattern=r' *\| *',
                  string=cfg.get(sct, 'player_shutdown_text'))
SHUTDOWN_TXT_L = f'{lbltxt[0]:^15}'
SHUTDOWN_TXT_R = f'{lbltxt[-1]:^15}'
FONT_DEF = cfg.get(sct, 'player_font')

# color vars
sct = 'Colors'
CLR_BG = cfg.get(sct, 'transparent')
CLR_TEXT = cfg.get(sct, 'text')
CLR_BTNS = cfg.get(sct, 'buttons')
CLR_BTN_HOVER = cfg.get(sct, 'button_hover')

# size vars
sct = 'Sizes'
BTN_SIZE = cfg.getint(sct, 'buttons')
LBL_W = cfg.getint(sct, 'text_width')
OFFSET_X = cfg.getint(sct, 'horizontal_offset')
OFFSET_Y = cfg.getint(sct, 'vertical_offset')

# btn point vars
sct = 'Button Points'
BTN_POINTS: oDict[str, list[int]] = oDict(
    prev=re_split(pattern=r' *, *',
                  string=cfg.get(sct, 'previous')),
    stop=re_split(pattern=r' *, *',
                  string=cfg.get(sct, 'stop')),
    play=re_split(pattern=r' *, *',
                  string=cfg.get(sct, 'play')),
    next=re_split(pattern=r' *, *',
                  string=cfg.get(sct, 'next'))
)

# advanced vars
sct = 'Advanced'
SCROLL_BREAK = f"{'':{cfg.getint(sct, 'scroll_break')}}"
SCROLL_MOTION = cfg.getint(sct, 'scroll_motion')
SCROLL_TICK = cfg.getfloat(sct, 'scroll_tick')
SCROLL_WAIT = cfg.getfloat(sct, 'scroll_pause')
DESKTOP_HWND = FindWindow(cfg.get(sct, 'desktop_win'), None)

# other vars
BOTTOM_FLAGS = SWP_NOACTIVATE | SWP_NOMOVE | SWP_NOSIZE
TOP_FLAGS = SWP_NOMOVE | SWP_NOSIZE | SWP_SHOWWINDOW


class Screen:
    screenInfo: dict[str, tuple[int]]
    screenInfo = GetMonitorInfo(
        MonitorFromPoint((0, 0))
    )
    monW: int = screenInfo.get('Monitor')[2]
    monH: int = screenInfo.get('Monitor')[3]
    taskbarH: int = monH - screenInfo.get('Work')[3]
    appW: int
    appH: int
    X: int
    Y: int

    def __init__(self):
        self.appW: int = (BTN_SIZE * 3 + LBL_W * 2)
        self.appH: int = max(BTN_SIZE, ((BTN_SIZE + self.taskbarH) // 2))
        self.X: int = round(self.monW - OFFSET_X - self.appW)
        self.Y: int = round(self.monH - OFFSET_Y - self.appH)


# cleanup
del (ConfigParser,
     ExtInterp,
     re_split,
     FindWindow,
     GetMonitorInfo,
     MonitorFromPoint,
     SWP_NOACTIVATE,
     SWP_NOMOVE,
     SWP_NOSIZE,
     SWP_SHOWWINDOW,
     environ,
     sct,
     lbltxt)
cfg['DEFAULT'].clear()
