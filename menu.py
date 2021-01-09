'''
Permite navegar por las distintas secciones del programa de manera comoda
'''

# ---Imports---
# curses: funciones de menu
import curses
# func_pendulo (fp): funciones para trabajar con pendulos
import func_pendulo as fp
# func_vpython (vp): funciones para realizar las animaciones de pendulos con vpython
import func_vpython as vp
# func_energias (fe): funciones para mostrar graficas con regimenes energeticos
import func_energias as fe

# ---Menus---
# Principal
menuprincipal = ['Péndulo simple', 'Péndulo doble', 'Péndulo triple', 'Péndulo esférico', 'Salir']

# Submenus orden 1
submenu_simple = ['Animación péndulo simple', 'Representación con vpython péndulo simple', 'Regímenes de energía', 'Volver al menú principal', 'Salir']
submenu_doble = ['Animación péndulo doble', 'Representación con vpython péndulo doble', 'Regímenes de energía', 'Volver al menú principal', 'Salir']
submenu_triple = ['Animación péndulo triple', 'Representación con vpython péndulo triple', 'Regímenes de energía', 'Volver al menú principal', 'Salir']
submenu_esferico = ['Animación péndulo esférico', 'Representación con vpython péndulo esférico', 'Regímenes de energía', 'Volver al menú principal', 'Salir']

# ---Funciones---
def print_menu(stdscr, indice, menu):
	'''
	Imprime el menu en su situacion actual

	---Parametros---
	* stdscr: objeto pantalla
	* fila_seleccionada_indice: indice del elemento seleccionado por el usuario
	* menu: menu actual
	'''
	# Se limpia la pantalla y se obtienen su altura y anchura
	stdscr.clear()
	h, w = stdscr.getmaxyx()

	# Se itera los elementos del menu
	for i, e in enumerate(menu):

		# Se obtienen posicion x, y en la pantalla adecuadas en funcion de la longitud del texto y la seleccion
		x = w//2 - len(e)//2
		y = h//2 - len(menu)//2 + i

		# Si el elemento es el seleccionado se marca
		if i == indice:

			# Activa el fondo blanco, añade el elemento y quita el fondo blanco
			stdscr.attron(curses.color_pair(1))
			stdscr.addstr(y, x, e)
			stdscr.attroff(curses.color_pair(1))

		# Si no es el seleccionado no se marca
		else: stdscr.addstr(y, x, e)

def main(stdscr, menu):
	'''
	Funcion de lanzamiento del menu

	---Parametros---
	* stdscr: objeto pantalla
	* menu: menu actual
	'''
	# Se configuran las opciones del menu
	curses.curs_set(0)
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

	# fila_seleccionada_indice nos permite navegar por el menu
	indice = 0

	# Iniciamos el menu
	print_menu(stdscr, indice, menu)

	# Empleamos un bucle infinito para permitir moverse por el menu
	while True:
		# Se toma input de teclado en key
		key = stdscr.getch()

		# Se limpia la pantalla y se procede a actuar en funcion de key
		stdscr.clear()

		# Flecha hacia arriba: se sube el indice
		if key == curses.KEY_UP: indice = (indice-1)%len(menu)

		# Flecha hacia abajo: se baja el indice
		elif key == curses.KEY_DOWN: indice = (indice+1)%len(menu)

		# Tecla enter: se analiza el indice para actuar
		elif key in [10, 13]:

			# Ultima opcion: salir
			if indice == len(menu)-1: break

			# Penultima opcion en un submenu: vuelta al menu pruncipal
			elif indice == len(menu)-2 and menu != menuprincipal: curses.wrapper(main, menuprincipal); break

			# Si no es ninguno de los casos superiores se actua en funcion del menu

			# ---Menu principal---
			if menu == menuprincipal:

				if indice == 0: curses.wrapper(main, submenu_simple); break 		# Pendulo simple
				elif indice == 1: curses.wrapper(main, submenu_doble); break 		# Pendulo doble
				elif indice == 2: curses.wrapper(main, submenu_triple); break 		# Pendulo triple
				elif indice == 3: curses.wrapper(main, submenu_esferico); break 	# Pendulo esferico

			# ---Submenu simple---
			elif menu == submenu_simple:

				if indice == 0: 		# Animacion matplotlib
					curses.endwin(); fp.Simple()
					curses.wrapper(main, menuprincipal); break
				elif indice == 1: 	# Animacion vpython
					curses.endwin(); vp.Simple()
					curses.wrapper(main, menuprincipal); break
				elif indice == 2: 	# Regimenes de energia
					curses.endwin(); fe.Simple()
					curses.wrapper(main, menuprincipal); break

			# ---Submenu doble---
			elif menu == submenu_doble:

				if indice == 0:		# Animacion matplotlib
					curses.endwin(); fp.Doble()
					curses.wrapper(main, menuprincipal); break
				elif indice == 1:	# Animacion vpython
					curses.endwin(); vp.Doble()
					curses.wrapper(main, menuprincipal); break
				elif indice == 2: 	# Regimenes de energia
					curses.endwin(); fe.Doble()
					curses.wrapper(main, menuprincipal); break

			# ---Submenu triple---
			elif menu == submenu_triple:

				if indice == 0:		# Animacion matplotlib
					curses.endwin(); fp.Triple()
					curses.wrapper(main, menuprincipal); break
				elif indice == 1:	# Animacion vpython
					curses.endwin(); vp.Triple()
					curses.wrapper(main, menuprincipal); break
				elif indice == 2: 	# Regimenes de energia
					curses.endwin(); fe.Triple()
					curses.wrapper(main, menuprincipal); break

			# ---Submenu esferico---
			elif menu == submenu_esferico:

				if indice == 0:		# Animacion matplotlib
					curses.endwin(); fp.Esferico()
					curses.wrapper(main, menuprincipal); break
				elif indice == 1:	# Animacion vpython
					curses.endwin(); vp.Esferico()
					curses.wrapper(main, menuprincipal); break
				elif indice == 2: 	# Regimenes de energia
					curses.endwin(); fe.Esferico()
					curses.wrapper(main, menuprincipal); break

		# Otra tecla: no actua
		else: pass

		# Se imprime el menu con las nuevas selecciones
		print_menu(stdscr, indice, menu)
