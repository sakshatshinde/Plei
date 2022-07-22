
# Plei 
**A game launcher with no bloat**

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)


**This project is ready for the launchers given below!** 

- [x] Steam
- [x] Origin
- [x] Epic Games Launcher
- [x] Uplay
- [ ] Standalone Games (Not gonna do this anytime soon :c)

---

## Why is this a thing?

As new game launchers came into being it increasingly got annoying to keep track of all the games over different stores/platform. I wanted to make a unified front where users can access all their games, including the one with no launchers. The goal behind this launcher is to be simple, minimilistic and **bloat-free**

---

## How to install? (For Devs)

#### This installation assumed you have python 3.X installed. [Get python here](https://www.python.org/ftp/python/3.8.1/python-3.8.1-amd64.exe)
 - Download [Plei](https://github.com/sakshatshinde/Plei/archive/master.zip) and extract it to your desired location
 - Run the following command
 > pip install -r requirements.txt
 - It might error out on "steamfiles" install. To fix this change your pip version to 9.0.X and run the above command again
 > python -m pip install pip==9.0.3 
 - app.pyw will launch Plei
 - Rename app.pyw to app.py to see the console message for logging/testing
 
---


## How to use it?

- When asked, the user must point the appropriate path to your game libraries. As in when asked for Steam point it to your Steam library (steamapps folder)
- If you have all your libraries in their default position no need to set them up again. Eg: `C:\Program Files(x86)\Origin Games\`
-  The above mentioned process maybe fully automated in the future
- After the initial setup you will be greeted with the installed games, just click on one to play it. Its that simple!

---

## Future endeavors 

 - Game recommendations based on your current library
 - Statistics about your gaming habbits
 
 ---
 
## Why is this launcher dependent on other launchers?

Sadly, Some games need the parent launcher to be running in order to launch them. If you try to launch the game from it's binary `exe` it may refuse to launch. To keep things simple, compatible and working as intended, this design decision had to be made. If anyone finds a workaround I'd be happy to implement it, you may contribute to the project directly as well. 

---

:triangular_ruler: :pencil2: :straight_ruler:
## Diagram 

[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggTFJcblxuQT5QbGVpXSAtLT4gU3t7U3RlYW19fVxuQSAtLT4gRXt7RUdTfX1cbkEgLS0-IE97e09yaWdpbn19XG5BIC0tPiBVe3t1UGxheX19XG5BIC0tPiBCe3tiYXR0bGVOZXR9fVxuQSAtLT4gUFtPZmZsaW5lIEdhbWVzXVxuUyAtLT4gTihTdG9yZSBOZXR3b3JrIFByb3RvY29sKVxuRSAtLT4gTihTdG9yZSBOZXR3b3JrIFByb3RvY29sKVxuTyAtLT4gTihTdG9yZSBOZXR3b3JrIFByb3RvY29sKVxuVSAtLT4gTihTdG9yZSBOZXR3b3JrIFByb3RvY29sKVxuQiAtLT4gTihTdG9yZSBOZXR3b3JrIFByb3RvY29sKVxuUCAtLT4gYmluKEJpbmFyeSBFWEUpXG5OIC0uLT4gTChbTGF1bmNoIHRoZSBnYW1lXSlcbmJpbiAtLi0-IEwiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9fQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggTFJcblxuQT5QbGVpXSAtLT4gU3t7U3RlYW19fVxuQSAtLT4gRXt7RUdTfX1cbkEgLS0-IE97e09yaWdpbn19XG5BIC0tPiBVe3t1UGxheX19XG5BIC0tPiBCe3tiYXR0bGVOZXR9fVxuQSAtLT4gUFtPZmZsaW5lIEdhbWVzXVxuUyAtLT4gTihTdG9yZSBOZXR3b3JrIFByb3RvY29sKVxuRSAtLT4gTihTdG9yZSBOZXR3b3JrIFByb3RvY29sKVxuTyAtLT4gTihTdG9yZSBOZXR3b3JrIFByb3RvY29sKVxuVSAtLT4gTihTdG9yZSBOZXR3b3JrIFByb3RvY29sKVxuQiAtLT4gTihTdG9yZSBOZXR3b3JrIFByb3RvY29sKVxuUCAtLT4gYmluKEJpbmFyeSBFWEUpXG5OIC0uLT4gTChbTGF1bmNoIHRoZSBnYW1lXSlcbmJpbiAtLi0-IEwiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9fQ)

---

## License
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl-3.0.en.html)
