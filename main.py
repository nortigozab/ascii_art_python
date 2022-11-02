from ctypes.wintypes import CHAR
from tkinter.tix import COLUMN
import ascii_magic
my_art = ascii_magic.from_image_file(
    'img/dibujo.png',
    columns=300,
    mode=ascii_magic.Modes.HTML
)
ascii_magic.to_html_file('ascii_art.html', my_art)
