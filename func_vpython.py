'''
Implementa funciones que realizan simulaciones numericas a tiempo real de baja precision
con vpython de diversos pendulos.
'''

# ---Imports---
# numpy (np): manejo de arrays
import numpy as np
# vpython: animaciones en 3D
from vpython import *
# matplotlib.pyplot (plt): impresion grafica 2D
import matplotlib.pyplot as plt
# func_sliders (fs): sliders
import func_sliders as fs
# ode_pendulo (ode): ecuaciones diferenciales de pendulos
import ode_pendulo as ode

# ---Funciones---
def paso(f, dt, x, v, ctes):
	'''
	Actualiza los valores de posicion y velocidad para un numero
	arbitrario de paramentros segun una funcion aceleraciones.

	---Parametros---
	* f: expresion de la aceleracion en funcion de la posicion y la velocidad
	* dt: intervalo temporal en el que se realiza la aproximacion numerica
	* x: lista de valores de posicion
	* v: lista de valores de velocidad
	* ctes: constantes que aparecen en f

	---Return---
	* <lista>: nuevas posiciones
	* <lista>: nuevas velocidades
	'''
	# Se calcula la aceleracion segun la funcion
	a = f(x, v, ctes)

	# Se actualizan los valores de velocidad y posicion a partir de la aceleracion calculada
	for i,ai in enumerate(a):
		v[i] += ai*dt
		x[i] += v[i]*dt

	return x, v

def Simple():
	'''
	Realiza una animacion del pendulo simple.
	Permite elegir parametros iniciales con sliders.
	'''
	# Se genera la ventana de sliders para seleccionar los parametros iniciales con func_sliders
	button, reset_func, sliders = fs.sliders_window(fs.simple)
	button.on_clicked(reset_func)
	plt.show()

	# Se toman los valores iniciales desde los sliders
	m, g, L, w, th, b = [slider.val for slider in sliders]
	th = np.radians(th)
	ctes = g, L, b, m

	# Se crean la barra y la esfera a partir de los datos iniciales
	xy = vector(L * np.sin(th), - L *np.cos(th), 0)
	rb = L/50
	re = L/10
	barra = cylinder(pos=vector(0, 0, 0), axis=xy, radius=rb)
	esfera = sphere(pos=xy, radius=re, color = vector(1,0,0), make_trail = True)

	# Se establece el intervalo temporal
	dt = 1e-3

	# Se realiza un bucle infinito para visualizar la animacion
	while True:

		# Se establece el ratio de frames
		rate(1e3)

		# Se actualizan posicion y velocidad por metodo numerico
		th, w = paso(ode.a_simple, dt, [th], [w], ctes)
		th = th[0]; w = w[0]

		# Se actualiza la posicion de la esfera y la barra
		xy = vector(L * np.sin(th), - L *np.cos(th), 0)
		esfera.pos = xy
		barra.axis = xy

def Doble():
	'''
	Realiza una animacion del pendulo doble.
	Permite elegir parametros iniciales con sliders.
	'''
	# Se genera la ventana de sliders para seleccionar los parametros iniciales con func_sliders
	button, reset_func, sliders = fs.sliders_window(fs.doble)
	button.on_clicked(reset_func)
	plt.show()

	# Se toman los valores iniciales desde los sliders
	g, m1, m2, L1, L2, w1, w2, th1, th2 = [slider.val for slider in sliders]
	th1 = np.radians(th1)
	th2 = np.radians(th2)
	ctes = g, m1, m2, L1, L2

	# Se crean las barras y las esferas a partir de los datos iniciales
	xy1 = vector(L1 * np.sin(th1), - L1 *np.cos(th1), 0)
	xy2 =  vector(L2 * np.sin(th2), - L2 *np.cos(th2), 0)
	rb = L1/50
	re1 = L1 / 10 * np.sqrt(m1)
	re2 = L1 / 10 * np.sqrt(m2)
	barra1 = cylinder(pos=vector(0, 0, 0), axis=xy1, radius=rb)
	esfera1 = sphere(pos=xy1, radius=re1, color = vector(1,0,0), make_trail = True)
	barra2 = cylinder(pos=xy1, axis=xy2, radius=rb)
	esfera2 = sphere(pos=xy1 + xy2, radius=re2, color = vector(0,1,0), make_trail = True)

	# Se establece el intervalo temporal
	dt = 1e-3

	# Se realiza un bucle infinito para visualizar la animacion
	while True:

		# Se establece el ratio de frames
		rate(1e3)

		# Se actualizan posicion y velocidad por metodo numerico
		th, w = paso(ode.a_doble, dt, [th1,th2], [w1,w2], ctes)
		th1, th2 = th; w1, w2 = w

		# Se actualizan la posiciones de las esferas y las barras
		xy1 = vector(L1 * np.sin(th1), - L1 *np.cos(th1), 0)
		xy2 = vector(L2 * np.sin(th2), - L2 *np.cos(th2), 0)
		esfera1.pos = xy1
		esfera2.pos = xy1 + xy2
		barra1.axis = xy1
		barra2.pos = xy1
		barra2.axis = xy2

def Triple():
	'''
	Realiza una animacion del pendulo triple.
	Permite elegir parametros iniciales con sliders.
	'''
	# Se genera la ventana de sliders para seleccionar los parametros iniciales con func_sliders
	button, reset_func, sliders = fs.sliders_window(fs.triple)
	button.on_clicked(reset_func)
	plt.show()

	# Se toman los valores iniciales desde los sliders
	g, m1, m2, m3, L1, L2, L3, w1, w2, w3, th1, th2, th3 = [slider.val for slider in sliders]
	th1 = np.radians(th1)
	th2 = np.radians(th2)
	th3 = np.radians(th3)
	ctes = g, m1, m2, m3, L1, L2, L3

	# Se crean las barras y las esferas a partir de los datos iniciales
	xy1 = vector(L1 * np.sin(th1), - L1 *np.cos(th1), 0)
	xy2 =  vector(L2 * np.sin(th2), - L2 *np.cos(th2), 0)
	xy3 =  vector(L3 * np.sin(th3), - L3 *np.cos(th3), 0)
	rb = L1/50
	re1 = L1 / 10 * np.sqrt(m1)
	re2 = L1 / 10 * np.sqrt(m2)
	re3 = L1 / 10 * np.sqrt(m3)
	barra1 = cylinder(pos=vector(0, 0, 0), axis=xy1, radius=rb)
	esfera1 = sphere(pos=xy1, radius=re1, color = vector(1,0,0), make_trail = True)
	barra2 = cylinder(pos=xy1, axis=xy2, radius=rb)
	esfera2 = sphere(pos=xy1 + xy2, radius=re2, color = vector(0,1,0), make_trail = True)
	barra3 = cylinder(pos=xy1 + xy2, axis=xy3, radius=rb)
	esfera3 = sphere(pos=xy1 + xy2 + xy3, radius=re3, color = vector(0,0,1), make_trail = True)

# Se establece el intervalo temporal
	dt = 1e-3

	# Se realiza un bucle infinito para visualizar la animacion
	while True:

		# Se establece el ratio de frames
		rate(1e3)

		# Se actualizan posicion y velocidad por metodo numerico
		th, w = paso(ode.a_triple, dt, [th1,th2,th3], [w1,w2,w3], ctes)
		th1, th2, th3 = th; w1, w2, w3 = w

		# Se actualizan la posiciones de las esferas y las barras
		xy1 = vector(L1 * np.sin(th1), - L1 *np.cos(th1), 0)
		xy2 = vector(L2 * np.sin(th2), - L2 *np.cos(th2), 0)
		xy3 =  vector(L3 * np.sin(th3), - L3 *np.cos(th3), 0)
		esfera1.pos = xy1
		esfera2.pos = xy1 + xy2
		esfera3.pos = xy1 + xy2 + xy3
		barra1.axis = xy1
		barra2.pos = xy1
		barra2.axis = xy2
		barra3.pos = xy1 + xy2
		barra3.axis = xy3

def Esferico():
	'''
	Realiza una animacion del pendulo esferico.
	Permite elegir parametros iniciales con sliders.
	'''
	# Se genera la ventana de sliders para seleccionar los parametros iniciales con func_sliders
	button, reset_func, sliders = fs.sliders_window(fs.esferico)
	button.on_clicked(reset_func)
	plt.show()

	# Se toman los valores iniciales desde los sliders
	m, g, L, wph, wth, ph, th  = [slider.val for slider in sliders]
	th = np.radians(th)
	ph = np.radians(ph)
	ctes = g, L

	# Se crea la barra y la esfera a partir de los datos iniciales
	xyz = vector(L * np.sin(ph) * np.sin(th), -L * np.cos(ph) ,L * np.sin(ph) * np.cos(th))
	rb = L/50
	re = L/10
	barra = cylinder(pos=vector(0, 0, 0), axis=xyz, radius=rb)
	esfera = sphere(pos=xyz, radius=re, color = vector(1,0,0), make_trail = True)

# Se establece el intervalo temporal
	dt = 1e-4

	# Se realiza un bucle infinito para visualizar la animacion
	while True:

		# Se establece el ratio de frames
		rate(1e4)

		# Se actualizan posicion y velocidad por metodo numerico
		ang, w = paso(ode.a_esferico, dt, [th,ph], [wth,wph], ctes)
		th, ph = ang; wth, wph = w

		# Se actualizan la posiciones de las esferas y las barras
		xyz = vector(L * np.sin(ph) * np.sin(th), -L * np.cos(ph) ,L * np.sin(ph) * np.cos(th))
		esfera.pos = xyz
		barra.axis = xyz
