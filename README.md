# [Spotify Player](https://github.com/Cryden13/Python/tree/main/spotifyplayer)

This is a small app that places a mini player on the Windows taskbar for Spotify

## Usage

Compile the ahk file. Set the variables in `config.cfg` to the preferred values, then run the compiled `SpotifyAHK.exe` once. Afterward, the player should automatically start when the Spotify shortcut is used

## Explanation of Variables

### Path Variables

- **spotify_exe:** the path to the Spotify executable. The default location is %AppData%/Spotify/Spotify.exe
- **ahk_exe:** the path to compiled AHK (*.exe) file. Must be in the `lib` directory unless the ahk file was edited
- **spotify_link:** if you want to use the app from a pinned taskbar item, this is the path to the pinned taskbar link file, else this is the path to the start menu link file
  - taskbar: `%appdata%\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar\Spotify.lnk`
  - start: `%appdata%\Microsoft\Windows\Start Menu\Programs\Spotify\Spotify.lnk`

### Text Variables

- **initial_spotify_title:** the initial/default window title of Spotify when it first boots up or when nothing is playing. (default: `Spotify Premium`)
- **player_title:** the player's window title. This doesn't show and should only be changed if there's a windows error. (default: `Spotify Taskbar Player`)
- **player_startup_text:** the text to show on the player at startup. (eg. `left text | right text`)
- **player_shutdown_text:** the text to show on the player at shutdown. (eg. `left text | right text`)
- **player_font:** the default font and font size. (eg. `font name, size`)

### Colors

- **transparent:** this color will be made transparent
- **text:** the color to make the text
- **buttons:** the color to make the buttons
- **button_hover:** the color to make the buttons if the mouse is over them

### Size Variables

- **buttons:** the height and width of the buttons, in pixels
- **text_width:** the width of the scrolling text on both sides of the player, in pixels
- **horizontal_offset:** the number of pixels to offset the player by from the right edge of the screen
- **vertical_offset:** the number of pixels to offset the player by from the bottom of the screen

### Button Points

- a list of points for each button that are used to create the button's polygonal shape

### Advanced Variables

- **scroll_break:** the size of the break in text when it marquees
- **scroll_motion:** the number of pixels to move the text by when it marquees
- **scroll_tick:** the pause between movements of the text when it marquees
- **scroll_pause:** the pause before moving the text when it marquees
- **desktop_win:** the window title of the desktop

## Changelog

<table>
    <tbody>
        <tr>
            <th align="center">Version</th>
            <th align="left">Changes</th>
        </tr>
        <tr>
            <td align="center">1.0</td>
            <td>Initial release</td>
        </tr>
        <tr>
            <td align="center">1.1</td>
            <td>
                <dl>
                    <dt>new</dt>
                    <ul>
                        <li>changed automation program</li>
                        <li>added icons</li>
                        <li>added global vars</li>
                    </ul>
                    <dt>bugfixes</dt>
                    <ul>
                        <li>fixed scrolling glitch</li>
                        <li>fixed button stalling</li>
                    </ul>
                </dl>
            </td>
        </tr>
        <tr>
            <td align="center">1.2</td>
            <td>
                <dl>
                    <dt>new</dt>
                    <ul>
                        <li>adjusted sizes</li>
                    </ul>
                    <dt>bugfixes</dt>
                    <ul>
                        <li>fixed buttons</li>
                        <li>fixed info not updating</li>
                    </ul>
                </dl>
            </td>
        </tr>
        <tr>
            <td align="center">1.3</td>
            <td>
                <dl>
                    <dt>new</dt>
                    <ul>
                        <li>changed automation program</li>
                        <li>overhauled ui</li>
                    </ul>
                    <dt>bugfixes</dt>
                    <ul>
                        <li>fixed ui bugs</li>
                    </ul>
                </dl>
            </td>
        </tr>
        <tr>
            <td align="center">2.0</td>
            <td>
                <dl>
                    <dt>new</dt>
                    <ul>
                        <li>majorly consolidated code</li>
                        <li>added trayicon menu</li>
                    </ul>
                    <dt>bugfixes</dt>
                    <ul>
                        <li>fixed marque expiration</li>
                        <li>fixed text updating</li>
                    </ul>
                </dl>
            </td>
        </tr>
        <tr>
            <td align="center">2.1</td>
            <td>
                <dl>
                    <dt>new</dt>
                    <ul>
                        <li>added right-click menu</li>
                    </ul>
                    <dt>bugfixes</dt>
                    <ul>
                        <li>fixed trayicon menu</li>
                    </ul>
                </dl>
            </td>
        </tr>
        <tr>
            <td align="center">2.2</td>
            <td>
                <dl>
                    <dt>new</dt>
                    <ul>
                        <li>consolidated code</li>
                        <li>reconfigured key sending</li>
                        <li>updated right-click menu</li>
                        <li>overhauled player startup</li>
                    </ul>
                    <dt>bugfixes</dt>
                    <ul>
                        <li>fixed traymenu</li>
                        <li>fixed right-click menu</li>
                    </ul>
                </dl>
            </td>
        </tr>
        <tr>
            <td align="center">3.0</td>
            <td>
                <dl>
                    <dt>new</dt>
                    <ul>
                        <li>split the functions for readability</li>
                        <li>added more configurable variables</li>
                        <li>added an errorlog</li>
                        <li>re-configured the ahk</li>
                        <li>changed Spotify behavior when minimizing</li>
                    </ul>
                    <dt>bugfixes</dt>
                    <ul>
                        <li>removed the broken traymenu</li>
                        <li>fixed Thread errors</li>
                    </ul>
                </dl>
            </td>
        </tr>
        <tr>
            <td align="center">3.1</td>
            <td>
                <dl>
                    <dt>new</dt>
                    <ul>
                        <li>consolidated code</li>
                        <li>added more configurable variables</li>
                        <li>moved some functions to different classes</li>
                        <li>added type hinting</li>
                        <li>changed timings</li>
                    </ul>
                    <dt>bugfixes</dt>
                    <ul>
                        <li>fixed issue with program not closing</li>
                        <li>fixed error where Spotify wouldn't become active</li>
                    </ul>
                </dl>
            </td>
        </tr>
        <tr>
            <td align="center">3.2</td>
            <td>
                <dl>
                    <dt>new</dt>
                    <ul>
                        <li>added a config file for ease of use</li>
                        <li>split the classes into individual files for ease of use</li>
                        <li>updated variable descriptions</li>
                    </ul>
                    <dt>bugfixes</dt>
                    <ul>
                        <li>fixed Spotify app recognition when it updates</li>
                        <li>fixed errors not redirecting to file</li>
                        <li>fixed freezing on startup</li>
                    </ul>
                </dl>
            </td>
        </tr>
    </tbody>
</table>
