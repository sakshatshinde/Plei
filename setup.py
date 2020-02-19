from cx_Freeze import setup, Executable
import sys
# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["os","steamfiles","nested_lookup","json","src.gameOps","src.usrOps"], 
    "includes": ["tkinter","os","steamfiles","nested_lookup","json","src.gameOps","src.usrOps"]
}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Plei",
        version = "0.1",
        description = "A bloat free game launcher",
        options = {"build_exe": build_exe_options},
        executables = [Executable(
            "app.py", 
            base=base,
            icon="Plei.ico"
            )
        ]
    )
