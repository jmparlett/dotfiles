# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.core.manager import Qtile


#key defs
mod = "mod4"
alt = "mod1"

#my apps used for shortcuts
terminal = "alacritty"
webBrowser = "firefox"
fileManager = "pcmanfm"
screenshotApp = "gnome-screenshot -i"
editor = "vim"


#colors
accentcolor = "#f15800" #used on bars around widgets, battery and currently active window highlight
barBackgroundColor = "#121210"
bordernormal = "#1D2330"
#bright blue #3de2ff
#faded orange #f15800
#custom defs
windowMargin=15
windowBorderSingle=True
borderWidth=4


keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # Spawn applications
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Start Firefox
    Key([mod], "t", lazy.spawn(webBrowser), desc="Start web browser"),
    # Start file manager
    Key([mod], "f", lazy.spawn(fileManager), desc="Start filemanager"),
    # Start spotify
    Key([mod], "s", lazy.spawn("spotify"), desc="Start spotify"),
    # Start Calculator
    Key([mod], "c", lazy.spawn("gnome-calculator"), desc="Start Calculator"),
    # Screenshot
    Key([mod], "p", lazy.spawn(screenshotApp), desc="print screen"),
    Key([mod], "e", lazy.spawn(terminal+ " -e " + editor)),

    # Toggle floating window
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([alt], "F4", lazy.window.kill(), desc="Kill focused window"),


    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "space", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    
    # Move to next and last widows
    Key([alt], "l", lazy.screen.next_group(), desc="Move to previous window"),
    Key([alt], "h", lazy.screen.prev_group(), desc="Move to previous window"),
    Key([alt], "Right", lazy.screen.next_group(), desc="Move to previous window"),
    Key([alt], "Left", lazy.screen.prev_group(), desc="Move to previous window"),

]
groups = [Group("", layout='monadtall'),
        Group("", layout='monadtall'),
        Group("", layout='monadtall'),
        Group("4", layout='monadtall'),
        Group("5", layout='monadtall'),
        Group("6", layout='monadtall'),
        Group("7", layout='monadtall'),
        Group("", layout='monadtall'),
        Group("", layout='floating')]

# Allow MODKEY+[0 through 9] to bind to groups, see https://docs.qtile.org/en/stable/manual/config/groups.html
# MOD4 + index Number : Switch to Group[index]
# MOD4 + shift + index Number : Send active window to another Group
from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder(mod)

layouts = [
    layout.Columns(border_focus_stack=accentcolor,
        border_focus=accentcolor,
        border_normal=bordernormal,
        border_width=borderWidth,
        margin=windowMargin,
        margin_on_single=windowMargin,
        border_on_single=windowBorderSingle),
    layout.Max(border_focus=accentcolor,
        border_normal=bordernormal,
        margin=windowMargin,
        border_width=borderWidth,
        margin_on_single=windowMargin,
        border_on_single=windowBorderSingle
        ),

    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    layout.Bsp(border_focus=accentcolor,
        border_normal=bordernormal,
        margin=windowMargin,
        border_width=borderWidth,
        margin_on_single=windowMargin,
        border_on_single=windowBorderSingle
        ),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

##### COLORS #####
colors = [
    [barBackgroundColor, barBackgroundColor],  # panel background
    ["#24262F", "#24262F"],  # background for current screen tab
    ["#ffffff", "#ffffff"],  # font color for group names
    ["#BD93F9", "#BD93F9"],  # border line color for current tab
    ["#8d62a9", "#8d62a9"],  # border line color for other tab and odd widgets
    ["#44475A", "#44475A"],  # color for the even widgets
    ["#e1acff", "#e1acff"],  # window name
]

##### PROMPT #####
# prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(font="mononoki nerd", fontsize=18, padding=2)
extension_defaults = widget_defaults.copy()

##### WIDGETS #####


def init_widgets_list():
    widgets_list = [
        widget.CurrentLayoutIcon(scale=0.79),
        widget.Sep(linewidth=0, padding=6,
                   foreground=colors[2], background=colors[0]),
        widget.GroupBox(highlight_method="block", inactive="999999"),
        widget.Prompt(
          bell_style="audible",
        ),
        #  widget.Prompt(),
        widget.WindowName(),
        widget.TextBox("Battery:", foreground=accentcolor),
        widget.Battery(padding=6),
        #  widget.TextBox(text=" Vol:", padding=1, foreground=accentcolor),
        #  widget.Volume(padding=5),
        widget.TextBox("|", foreground=accentcolor),
        widget.Systray(),
        widget.TextBox("|", foreground=accentcolor),
        widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
        #  widget.Clock(format="%a %d %b %I:%M %p"),
        widget.Sep(linewidth=0, padding=6,
                   foreground=colors[2], background=colors[0]),
    ]
    return widgets_list


# SCREENS ##### (TRIPLE MONITOR SETUP)
def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1  # Slicing removes unwanted widgets on Monitors 1,3


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2  # Monitor 2 will display all widgets in widgets_list


def init_screens():
    return [
        Screen(
            top=bar.Bar(
                widgets=init_widgets_screen1(),
                size=30,
                background=barBackgroundColor,
                opacity=0.8
            )
        ),
        Screen(
            top=bar.Bar(
                widgets=init_widgets_screen2(),
                size=35,
                background=barBackgroundColor,
                opacity=0.8
            )
        ),
    ]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

auto_fullscreen = True
focus_on_window_activation = "smart"



# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.

#  wmname = "LG3D"

wmname = "tomatos are for ... TOMATOS!!!"
