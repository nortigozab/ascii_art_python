import ascii_magic
import imgkit
my_art = ascii_magic.from_image_file(
    'img/dibujo.png',
    columns=200,
    width_ratio=2,
    mode=ascii_magic.Modes.HTML
)
ascii_magic.to_html_file('ascii_art.html', my_art)
options = {
    'format': 'png',
    'quality': '50',
}
imgkit.from_url('ascii_art.html', 'out.png',options=options)