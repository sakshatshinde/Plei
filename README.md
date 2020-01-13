
# Plei 
#### A game launcher with no bloat
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![HitCount](http://hits.dwyl.io/sakshatshinde/Plei.svg)](http://hits.dwyl.io/sakshatshinde/Plei) [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)


# Why is this a thing?

As new game launchers came into being it increasingly got annoying to keep track of all the games over different stores/platform. I wanted to make a unified front where users can access all their games, including the one with no launchers. The goal behind this launcher is to be simple, minimilistic and **bloat-free**


## How to use it?

- When asked, the user must point the appropriate path to your game libraries. As in when asked for Steam point it to your Steam library.
- If you have all your libraries in their default position no need to set them up again. Eg: `C:\Program Files(x86)\Origin Games\`
-  The above mentioned process maybe fully automated in the future
- After the initial setup you will be greeted with the installed games, just click on one to play it. Its that simple!


## Future endeavors 

 - Game recommendations based on your current library
 - Statistics about your gaming habbits
 
 
## Why is this launcher dependent on other launchers?

Sadly, Some games need the parent launcher to be running in order to launch them. If you try to launch the game from it's binary `exe` it may refuse to launch. To keep things simple, compatible and working as intended, this design decision had to be made. If anyone finds a workaround I'd be happy to implement it, you may contribute to the project directly as well. 


## Manage file publication

Since one file can be published to multiple locations, you can list and manage publish locations by clicking **File publication** in the **Publish** sub-menu. This allows you to list and remove publication locations that are linked to your file.


## UML diagram
[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggTFJcbkFbUGxlaV0gLS0-IFMoKFN0ZWFtKSlcbkEgLS0-IEUoKEVHUykpXG5BIC0tPiBPKChPcmlnaW4pKVxuQSAtLT4gVSgodVBsYXkpKVxuQSAtLT4gQigoYmF0dGxlTmV0KSlcbkEgLS0-IFAoT2ZmbGluZSBHYW1lcylcblMgLS0-IEx7TGF1bmNoIHRoZSBnYW1lfVxuRSAtLT4gTHtMYXVuY2ggdGhlIGdhbWV9XG5PIC0tPiBMe0xhdW5jaCB0aGUgZ2FtZX1cblUgLS0-IEx7TGF1bmNoIHRoZSBnYW1lfVxuQiAtLT4gTHtMYXVuY2ggdGhlIGdhbWV9XG5QIC0tPiBiaW4oKEJpbmFyeSBFWEUpKVxuYmluIC0tPiBMIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifX0)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggTFJcbkFbUGxlaV0gLS0-IFMoKFN0ZWFtKSlcbkEgLS0-IEUoKEVHUykpXG5BIC0tPiBPKChPcmlnaW4pKVxuQSAtLT4gVSgodVBsYXkpKVxuQSAtLT4gQigoYmF0dGxlTmV0KSlcbkEgLS0-IFAoT2ZmbGluZSBHYW1lcylcblMgLS0-IEx7TGF1bmNoIHRoZSBnYW1lfVxuRSAtLT4gTHtMYXVuY2ggdGhlIGdhbWV9XG5PIC0tPiBMe0xhdW5jaCB0aGUgZ2FtZX1cblUgLS0-IEx7TGF1bmNoIHRoZSBnYW1lfVxuQiAtLT4gTHtMYXVuY2ggdGhlIGdhbWV9XG5QIC0tPiBiaW4oKEJpbmFyeSBFWEUpKVxuYmluIC0tPiBMIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifX0)


