#
# License: See LICENSE file
# GitHub: https://github.com/Baekalfen/PyBoy
#

import sys
from pprint import pprint

from pyboy import PyBoy

pyboy = PyBoy(
        "./PokemonRed.gb",
        debugging=False,
        disable_input=True,
        # window_type="headless", # For unattended use, for example machine learning
        hide_window="--quiet" in sys.argv,
    )
pyboy.set_emulation_speed(0)

for n in range(1000): # Move ahead the desired number of frames.
    pyboy.tick()

tile_map = pyboy.get_window_tile_map() # Get the TileView object for the window.

index_map = tile_map.get_tile_matrix()

# For unattended use, the screen buffer can be displayed using the following:
pyboy.get_screen_image().show()
