from ctypes.wintypes import CHAR
from tkinter.tix import COLUMN
import ascii_magic
my_art = ascii_magic.from_image_file(
    'img/dibujo.png',
    columns=300
)
ascii_magic.to_terminal(my_art)
