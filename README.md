 
# Ascii_art_Python

 ![Badge en Desarollo](https://img.shields.io/badge/STATE-SUCESS-green) 
 ![GitHub Org's stars](https://img.shields.io/github/stars/nortigozab?style=social)
 ![GitHub](https://img.shields.io/github/license/nortigozab/ascii_art_python)

Este es un proyecto para la ejución de la libreria ascii-magic en python, para el ascii art image, desde la terminal, el uso de esta proyecto se hace desde una distribución de GNU/Linux Manjaro en su Release 22.0.0.  

## Requisitos 🧱

_Tener Instalado Python_

## Desarrollo 👉

_Instalamos la liberia de [ascii-magic](https://pypi.org/project/ascii-magic/)_

~~~bash
  pip install ascii-magic
~~~
_Siguiendo la Documentacion de [ascci-magic](https://pypi.org/project/ascii-magic/)_

- Importamos la libreria en el archivo de python

![image text](https://github.com/nortigozab/ascii_art_python/blob/main/img/screenshot/screenshot2.png?raw=true "import") 

- creamos la variable, llamando la función e importando la imagen a convertir, tomando la ruta relativa en este caso y dando un tamaño de columna 300

![image text](https://github.com/nortigozab/ascii_art_python/blob/main/img/screenshot/screenshot3.png?raw=true "value") 

- imprimimos en terminal la variable creada anteriormente

![image text](https://github.com/nortigozab/ascii_art_python/blob/main/img/screenshot/screenshot4.png?raw=true "print_terminal") 

- Ejecutamos con el comando 

~~~bash
  python main.py
~~~

## Problemas 🚧🚨
- Si nos sale el error de **Tkinter: "Python may not be configured for Tk"**
    - seguir esta [Solución](https://stackoverflow.com/questions/5459444/tkinter-python-may-not-be-configured-for-tk)
    - En mi caso lo solucione instalando tk desde pacman, al ser derivada de Arch Linux 
        ~~~bash
            sudo pacman -S tk
        ~~~ 
        - Al Hacer esto se agrega automaticamente al main.py dos lineas de codigo que ejecutan el tk
        ![image text](https://github.com/nortigozab/ascii_art_python/blob/main/img/screenshot/screenshot5.png?raw=true "tk") 

## Codigo Completo
![image text](https://github.com/nortigozab/ascii_art_python/blob/main/img/screenshot/screenshot1.png?raw=true "code_complete") 

## Resultado

| ![image text](https://github.com/nortigozab/ascii_art_python/blob/main/img/dibujo.png?raw=true? "image_to_convert")| ![image text](https://github.com/nortigozab/ascii_art_python/blob/main/img/file.gif?raw=true? "result") |
| --- | ---|

## License  

[GPL-3.0](https://choosealicense.com/licenses/agpl-3.0/)
  