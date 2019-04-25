#! /usr/bin/env python3
from __future__ import print_function, unicode_literals
import os
import sys

utilites = [
    "ccleaner",
    "revo.uninstaller",
    "slack",
    "teamviewer"
]

media = [
    "vlc",
    "calibre",
    "rufus",
    "steam"
]

essentials = [
    "google-chrome",
    ""
]

dev_tools = [
    "docker",
    "vscode",
    "anaconda3",
    "cmake",
    "python",
    "MySQL",
    "git"
]


# Install any missing packages
cli_pkgs = ["click", "pyfiglet", "docopt", "PyInquirer", "regex"]
install_pkgs = [pkg for pkg in cli_pkgs if not pkg in sys.modules]
if install_pkgs:
    os.system(f"pip install {' '.join(install_pkgs)}")


import click
import docopt
import regex
from pyfiglet import Figlet
from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError


f = Figlet(font="slant")
print(f.renderText("Welcome!"))


style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})


# Choose os setup
# TODO: windows, linux, macos
select_os = [{
    "type": "list",
    "name": "os",
    "message": "Setting up which operating system?",
    "choices": ["Linux", "Windows", "macOS"]
}]

answers = prompt(select_os, style=style)

# Install linux
if answers["os"] == "Linux":
    
    select_distro = [{
        "type": "list",
        "name": "distro",
        "message": "Which Linux distro?",
        "choices": ["Manjaro"]
    }]

    answers = prompt(select_distro, style=style)
    

# Install macos
elif answers["os"] == "macOS":

    # Install brew
    print("Installing brew...")
    os.system('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
    os.system("brew upgrade")
    os.system("brew update")
    os.system("brew tap caskroom/cask")

    # Install preferences


# Install windows
else:
    pass 
    
    # Install choco

    # Run windows debloater

    # Setup wsl


# Install applications


# Link dotfiles
    
    # Install gnu stow