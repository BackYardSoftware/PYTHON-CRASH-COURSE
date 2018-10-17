import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = "E:\\Python\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "E:\\Python\\tcl\\tk8.6"

executables = [cx_Freeze.Executable("alien_invasion.py")]

cx_Freeze.setup(
    name="Alien Invasion",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["alien.py","bullet.py","button.py",
                                            "game_functions.py","game_stats.py",
                                            "scoreboard.py","settings.py","ship.py",
                                            "alien.bmp","ship.bmp"]}},

    executables = executables,
    version='1.0.0'
    
    )
