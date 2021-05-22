from win32com.client import Dispatch


def changeShortcut(newPath: str) -> None:
    link = Dispatch("WScript.Shell").CreateShortcut(SPOTIFY_LINK)
    link.Targetpath = newPath
    link.save()


if __name__ == '__main__':
    from spotifyplayer.lib.constants import SPOTIFY_LINK, SPOTIFY_AHK
    changeShortcut(SPOTIFY_AHK)
else:
    from ..lib.constants import SPOTIFY_LINK, SPOTIFY_AHK
