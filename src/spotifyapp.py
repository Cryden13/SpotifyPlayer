from pywinauto.timings import wait_until as win_wait_until
from pywinauto.controls.hwndwrapper import HwndWrapper
from pywinauto.application import Application
from tkinter import messagebox as Mbox
from operator import ne as op_ne
from time import sleep
from win32gui import (
    SetForegroundWindow,
    SetWindowPos,
    ShowWindow
)
from win32con import (
    HWND_BOTTOM,
    HWND_TOP,
    SW_SHOWNOACTIVATE
)

from ..lib.constants import *

if TYPE_CHECKING:
    from ..player import GUI


class SpotifyApp:
    app: Application
    base: HwndWrapper
    win: HwndWrapper
    startTitle: str
    posY: int
    hideloop: int

    def __init__(self, root: "GUI"):
        self.startApp()
        self.startTitle = self.getText()
        root.updateText(self.startTitle)
        self.showSpotify()
        self.hideloop = 0
        ct = 0
        while True:
            try:
                if self.win.has_focus() or self.base.has_focus():
                    break
                self.win.minimize()
                sleep(0.1)
                self.win.restore()
                SetWindowPos(self.win.handle, HWND_TOP,
                             0, 0, 0, 0, TOP_FLAGS)
            except Exception as ex:
                print(ex)
            ct += 1
            if ct == 10:
                self.showError()
                ct = 0
                self.showSpotify()

    def startApp(self) -> None:
        self.win = None
        i = 0
        while not self.win:
            if i == 4:
                self.showError()
                i = 0
            if i in [0, 2]:
                try:
                    Application().connect(title=SPOTIFY_TITLE).kill(soft=True)
                except:
                    pass
                self.app = Application().start(SPOTIFY_EXE)
            try:
                self.base = self.app.top_window().wrapper_object()
                self.win = self.base.top_level_parent()
                self.win.set_transparency(0)
                self.posY = self.base.rectangle().top
                self.win.move_window(y=-50)
                win_wait_until(timeout=3,
                               retry_interval=0.05,
                               func=self.win.window_text,
                               value=SPOTIFY_TITLE)
            except:
                i += 1

    def getText(self) -> str:
        sleep(2.5)
        # mute
        self.win.send_keystrokes('^{DOWN 16}')
        sleep(0.5)
        # start playing
        self.win.send_keystrokes('{SPACE}')
        try:
            win_wait_until(timeout=2,
                           retry_interval=0.1,
                           func=self.win.window_text,
                           value=SPOTIFY_TITLE,
                           op=op_ne)
            sleep(0.1)
            nowPlaying = str(self.win.window_text())
        except:
            nowPlaying = str('  -  ')
        # stop playing
        self.win.send_keystrokes('{SPACE}')
        sleep(0.1)
        # set volume to mid
        self.win.send_keystrokes('^{UP 8}')
        return nowPlaying

    def hideSpotify(self) -> None:
        self.win.set_transparency(0)
        ShowWindow(self.win.handle, SW_SHOWNOACTIVATE)
        sleep(0.1)
        self.posY = self.base.rectangle().top
        SetWindowPos(self.win.handle, HWND_BOTTOM, 0, 0, 0, 0, BOTTOM_FLAGS)
        self.win.move_window(y=-50)
        if self.win.has_focus():
            if self.hideloop > 9:
                self.hideloop = 0
            try:
                SetForegroundWindow(DESKTOP_HWND)
                self.hideloop = 0
            except:
                self.hideloop += 1
                self.hideSpotify()

    def showSpotify(self) -> None:
        self.win.move_window(y=max(self.posY, 0))
        self.win.set_transparency(255)

    @staticmethod
    def showError() -> None:
        if Mbox.askyesno("Error", "Python can't seem to hook Spotify. Would you like to keep trying?\n(Note that Spotify can be open but not playing)"):
            return
        else:
            raise SystemExit
