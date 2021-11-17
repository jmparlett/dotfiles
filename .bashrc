# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac

# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# We have color support; assume it's compliant with Ecma-48
	# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
	# a case would tend to support setf rather than setaf.)
	color_prompt=yes
    else
	color_prompt=
    fi
fi
 #Commented copy in case over written by terminal app
 #PS1='${debian_chroot:+($debian_chroot)}\e[38;5;42m\u\e[m\e[38;5;247m@\e[m\e[38;5;202m\H\e[\e[38;5;247m:\W\e[38;5;255m\$ '
if [ "$color_prompt" = yes ]; then
	BRACKET="\[\033[38;5;247m\]"
	AT="\[\033[38;5;247m\]"
	USRNAME="\[\033[38;5;196m\]"
	HOSTNAME="\[\033[38;5;31m\]"
	CURRENTDIR="\[\033[38;5;93m\]"
	PROMPT="\[\033[38;5;255m\]"
  PS1="$USRNAME\u$AT@$HOSTNAME\H$CURRENTDIR\W$BRACKET>\e[0m "
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\W\$ '
fi
unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*|alacritty*)
  BRACKET="\[\033[38;5;247m\]"
	AT="\[\033[38;5;247m\]"
	USRNAME="\[\033[38;5;196m\]"
	HOSTNAME="\[\033[38;5;166m\]"
	CURRENTDIR="\[\033[38;5;93m\]"
	PROMPT="\[\033[38;5;255m\]"
  PS1="$USRNAME\u$AT@$HOSTNAME\H$CURRENTDIR\W$BRACKET>\e[0m "

  #  PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# colored GCC warnings and errors
#export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# Alias definitions.
alias cls='clear'
alias sshtux='ssh jmp586@tux.cs.drexel.edu'
alias python='python3'
alias ipython='ipython3'
alias rscratch='make ; ./scratch'
alias lw='nohup ~/.local/bin/LibreWolf-85.0.2-1.x86_64.AppImage &'
alias pdf='nohup & evince'
alias cXM3Headset='bluetoothctl connect 94:DB:56:54:C5:47'
alias night-light='xrandr --output eDP1 --gamma 1.1:0.6:0.7 --brightness 0.65'
alias day-light='xrandr --output eDP1 --gamma 1:1:1 --brightness 0.8'
alias archcube-sleep='systemctl suspend'
alias archcube-backup='~/.jerryscripts/archcube-backup.sh'
alias monToggle='. ~/.jerryscripts/monitor_toggle.sh'
alias r="fc -s"
alias h="history"
alias rm="rm -i"
alias mv="mv -i"
alias cp="cp -i" 
alias ghc='ghc --make -dynamic'
alias insight='Insight-x86_64-pc-linux-gnu-8180966-x86_64.AppImage'
alias pdftex='pdflatex --shell-escape'
alias start-rpi-dhcp="~/.jerryscripts/start-rpi-dhcp.sh"
alias stop-rpi-dhcp="sudo systemctl stop dhcpd4*"

# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

# Custom Paths
export PATH=$PATH:/usr/local/texlive/2020/bin/x86_64-linux
export PATH=$PATH:/home/jparlett/Myapps/appImages
export PATH=$PATH:/home/jparlett/.local/bin
#custom misc
#export TERM=xterm-256color
cd ~

# use vim keys in terminal
set -o vi
