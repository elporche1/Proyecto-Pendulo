'''
Implementa funciones que permiten crear una ventana con sliders para manejar variables iniciales.
Trabaja con matrices que guardan informacion sobre las variables para generar los sliders.
Cada fila corresponde a una variable con formato: [nombre, valor inicial, valor minimo, valor maximo]
'''

# ---Imports---
# numpy (np): manejo de arrays
import numpy as np
# matplotlib.pyplot (plt): impresion grafica 2D
import matplotlib.pyplot as plt
# matplotlib.widgets: sliders y botones
from matplotlib.widgets import Slider, Button

# ---Matrices---
simple = [['$m$', 1, .5, 3],
				['$g$', 9.8, .2, 20],
				['$L$', 1, .5, 3],
				[r'$\omega_0$', 0, -10, 10],
				[r'$\theta_0$', 90, 0, 360],
				['$b$', .1, 0, 3]]

doble =   [['$g$', 9.8, .2, 20],
				['$m_1$', 1, .2, 5],
				['$m_2$', 1, .2, 5],
				['$L_1$', 1, .5, 3],
				['$L_2$', 1, .5, 3],
				[r'$\omega_1$', 0, -10, 10],
				[r'$\omega_2$', 0, -10, 10],
				[r'$\theta_1$', 90, 0, 360],
				[r'$\theta_2$', 90, 0, 360]]

triple =	[['$g$', 9.8, .2, 20],
				['$m_1$', 1, .2, 5],
				['$m_2$', 1, .2, 5],
				['$m_3$', 1, .2, 5],
				['$L_1$', 1, .5, 3],
				['$L_2$', 1, .5, 3],
				['$L_3$', 1, .5, 3],
				[r'$\omega_1$', 0, -10, 10],
				[r'$\omega_2$', 0, -10, 10],
				[r'$\omega_3$', 0, -10, 10],
				[r'$\theta_1$', 90, 0, 360],
				[r'$\theta_2$', 90, 0, 360],
				[r'$\theta_3$', 90, 0, 360]]

esferico = [['$m$', 1, .5, 3],
				 ['$g$', 9.8, .2, 20],
				 ['$L$', 1, .2, 5],
				 [r'$\omega_{\phi0}$', 0, -10, 10],
				 [r'$\omega_{\theta0}$', 0, -10, 10],
				 [r'$\phi_0$', 90, 0, 360],
				 [r'$\theta_0$', 90, 0, 360]]

# ---Funciones---
def slider_gen(matriz):
	'''
	Genera sliders a partir de una matriz

	---Parametros---
	* matriz: contiene la informacion sobre los sliders

	---Return---
	* <lista>: contiene los sliders creados
	'''
	# Se definen las posiciones y tamaños que tendran los sliders
	N = len(matriz)
	posx = .1
	posy = np.linspace(.8, .1, N)
	sizex = .8
	sizey = .75/N

	# Se inicializa la lista que contendra los sliders
	sliders = []

	# Se iteran las filas de la matriz
	for i,fila in enumerate(matriz):

		# Se crean los 'ejes' del slider
		ax = plt.axes([posx, posy[i], sizex, sizey])

		# Se crea el slider y se añade a la lista
		slider = Slider(ax, fila[0], valinit=float(fila[1]), valmin=float(fila[2]), valmax=float(fila[3]))
		sliders.append(slider)

	return sliders

def reset_gen(sliders):
	'''
	Genera un boton que reinicia los sliders

	---Parametros---
	* sliders: lista con los sliders a reiniciar

	---Return---
	* <Button>: boton de reset creado
	* <funcion>: funcion reset necesaria fuera
	'''
	# Se crean los 'ejes' del boton
	ax = plt.axes([0.8, .01, .1, .05])

	# Se crea el boton de reset
	button = Button(ax, 'Reset')

	# Se define un proceso que resetea todos los sliders
	def reset(self):
		for slider in sliders:
			slider.reset()

	return button, reset

def sliders_window(matriz):
	'''
	Crea una figura de matplotlib con sliders y boton de reset a partir de una matriz

	---Parametros---
	* matriz: contiene la informacion sobre los sliders

	---Return---
	* <Button>: boton de reset creado
	* <funcion>: funcion reset necesaria fuera
	* <lista>: contiene los sliders creados
	'''
	plt.figure()
	sliders = slider_gen(matriz)
	button, reset_func = reset_gen(sliders)
	return button, reset_func, sliders
