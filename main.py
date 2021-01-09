'''
Programa que importa el menu y usa sus dos funciones para lanzarlo
'''
# ---Imports---
# menu: menu del programa construido sobre curses
import menu

# Se lanza el menu
menu.curses.wrapper(menu.main, menu.menuprincipal)
