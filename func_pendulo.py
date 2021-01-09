'''
Implementa funciones que permiten hacer calculos numericos precisos para la trayectoria de pendulos.
'''

# ---Imports---
# numpy (np): manejo de arrays
import numpy as np
# scipy.optimize.odeint: resolucion de ecuaciones diferenciales
from scipy.integrate import odeint
# matplotlib.pyplot (plt): impresion grafica 2D
import matplotlib.pyplot as plt
# mpl_toolkits.mplot3d.Axes3D: impresion grafica 3D
from mpl_toolkits.mplot3d import Axes3D
# ode_pendulo (ode): ecuaciones diferenciales de pendulos
import ode_pendulo as ode
# func_sliders (fs): sliders
import func_sliders as fs
# func_animacion (fa): animaciones en matplotlib
import func_animacion as fa

# ---Funciones---
def Sol_Simple(t, params, argms):
	'''
	Utiliza ode.Simple para calcular la trayectoria

	---Parametros---
	* t: array de tiempos
	* params: tupla con los valores iniciales (th,w)
	* argms: tupla con las constantes del problema (g,L,b)

	---Return---
	* <np.array>: angulo
	* <np.array>: velocidad angular
	* <np.array>: posicion x
	* <np.array>: posicion y
	'''
	# Se soluciona la ODE y se toman los datos del angulo y velocidad angular
	sol = odeint(ode.Simple, params, t, args=argms)
	th = sol[:, 0]
	w = sol[:, 1]

	# Se transforman las coordenadas polares en cartesianas
	_, L, _, _ = argms
	x = L * np.sin(th)
	y = - L * np.cos(th)

	return th, w, x, y

def Sol_Doble(t, params, argms):
	'''
	Utiliza ode.Doble para calcular la trayectoria

	---Parametros---
	* t: array de tiempos
	* params: tupla con los valores (th1,w1,th2,w2)
	* argms: tupla con las constantes del problema (g,L1,L2,m1,m2)

	---Return---
	* <np.array>: angulo 1
	* <np.array>: velocidad angular 1
	* <np.array>: angulo 2
	* <np.array>: velocidad angular 2
	* <np.array>: posicion x 1
	* <np.array>: posicion y 1
	* <np.array>: posicion x 2
	* <np.array>: posicion y 2
	'''
	# Se soluciona la ODE y se toman los datos del angulo y velocidad angular para cada bola
	sol = odeint(ode.Doble, params, t, args=argms)
	th1 = sol[:, 0]
	w1 = sol[:, 1]
	th2 = sol[:, 2]
	w2 = sol[:, 3]

	# Se transforman las coordenadas polares en cartesianas
	_, L1, L2, _, _ = argms
	x1 = L1 * np.sin(th1)
	y1 = - L1 * np.cos(th1)
	x2 = x1 + L2 * np.sin(th2)
	y2 = y1 - L2 * np.cos(th2)

	return th1, w1, th2, w2, x1, y1, x2, y2

def Sol_Triple(t, params, argms):
	'''
	Utiliza ode.Triple para calcular la trayectoria

	---Parametros---
	* t: array de tiempos
	* params: tupla con los valores (th1,w1,th2,w2,th3,w3)
	* argms: tupla con las constantes del problema (g,L1,L2,L3,m1,m2,m3)

	---Return---
	* <np.array>: angulo 1
	* <np.array>: velocidad angular 1
	* <np.array>: angulo 2
	* <np.array>: velocidad angular 2
	* <np.array>: angulo 3
	* <np.array>: velocidad angular 3
	* <np.array>: posicion x 1
	* <np.array>: posicion y 1
	* <np.array>: posicion x 2
	* <np.array>: posicion y 2
	* <np.array>: posicion x 3
	* <np.array>: posicion y 3
	'''
	# Se soluciona la ODE y se toman los datos del angulo y velocidad angular para cada bola
	sol = odeint(ode.Triple, params, t, args=argms)
	th1 = sol[:, 0]
	w1 = sol[:, 1]
	th2 = sol[:, 2]
	w2 = sol[:, 3]
	th3 = sol[:, 4]
	w3 = sol[:, 5]

	# Se transforman las coordenadas polares en cartesianas
	_, L1, L2, L3, _, _, _ = argms
	x1 = L1 * np.sin(th1)
	y1 = - L1 * np.cos(th1)
	x2 = x1 + L2 * np.sin(th2)
	y2 = y1 - L2 * np.cos(th2)
	x3 = x2 + L3 * np.sin(th3)
	y3 = y2 - L3 * np.cos(th3)

	return th1, w1, th2, w2, th3, w3, x1, y1, x2, y2, x3, y3

def Sol_Esferico(t, params, argms):
	'''
	Utiliza ode.Esferico para calcular la trayectoria

	---Parametros---
	* t: array de tiempos
	* params: tupla con los valores (th,wth,ph,wph)
	* argms: tupla con las constantes del problema (g,L)

	---Return---
	* <np.array>: angulo th
	* <np.array>: velocidad angular en th
	* <np.array>: angulo ph
	* <np.array>: velocidad angular en ph
	* <np.array>: posicion x 1
	* <np.array>: posicion y
	* <np.array>: posicion z
	'''
	# Se soluciona la ODE y se toman los datos del angulo y velocidad angular
	sol = odeint(ode.Esferico, params, t, args=argms)
	th = sol[:, 0]
	wth = sol[:, 1]
	ph = sol[:, 2]
	wph = sol[:, 3]

	# Se transforman las coordenadas polares en cartesianas
	_, L = argms
	x = L * np.sin(ph) * np.cos(th)
	y = L * np.sin(ph) * np.sin(th)
	z = - L * np.cos(ph)

	return th, wth, ph, wph, x, y, z

def Simple():
	'''
	Proceso que realiza el experimento del pendulo simple.
	Permite elegir parametros iniciales con sliders, calcula de forma numerica precisa la trayectoria y
	realiza una animacion en 2D.
	'''
	# Se genera la ventana de sliders para seleccionar los parametros iniciales con func_sliders
	button, reset_func, sliders = fs.sliders_window(fs.simple)
	button.on_clicked(reset_func)
	plt.show()

	# Se toman los valores iniciales desde los sliders
	m, g, L, w_0, th_0, b = [slider.val for slider in sliders]
	th_0 = np.radians(th_0)

	# Se establecen los parametros temporales
	t_0, t_f = 0, 20
	dt = 0.02

	# Se crea el array de tiempos y las tuplas de parametros iniciales y constantes
	t = np.arange(t_0, t_f + dt, dt)
	params = (th_0, w_0)
	args = (g, L, b, m)

	# Sol_Simple resuelve numericamente el problema
	th, w, x, y = Sol_Simple(t, params, args)

	# Se reducen los angulos al intervalo (-pi,pi)
	th_red = th%(2*np.pi)
	th_red = np.where(th_red>np.pi,th_red-2*np.pi,th_red)

	# Animacion2D anima los datos obtenidos
	an = fa.Animacion2D(t, 1.1 * L, [x], [y], th_red, w, r'$\theta$ (rad)', r'$\omega$ (rad/s)')

	# Se muestra
	plt.show()

def Doble():
	'''
	Proceso que realiza el experimento del pendulo doble.
	Permite elegir parametros iniciales con sliders, calcula de forma numerica precisa la trayectoria y
	realiza una animacion en 2D.
	'''
	# Se genera la ventana de sliders para seleccionar los parametros iniciales con func_sliders
	button, reset_func, sliders = fs.sliders_window(fs.doble)
	button.on_clicked(reset_func)
	plt.show()

	# Se toman los valores iniciales desde los sliders
	g, m1, m2, L1, L2, w1_0, w2_0, th1_0, th2_0 = [slider.val for slider in sliders]
	th1_0 = np.radians(th1_0)
	th2_0 = np.radians(th2_0)

	# Se establecen los parametros temporales
	t_0, t_f = 0, 20
	dt = 0.02

	# Se crea el array de tiempos y las tuplas de parametros iniciales y constantes
	t = np.arange(t_0, t_f + dt, dt)
	params = (th1_0, w1_0, th2_0, w2_0)
	args = (g, L1, L2, m1, m2)

	# Sol_Doble resuelve numericamente el problema
	th1, w1, th2, w1, x1, y1, x2, y2 = Sol_Doble(t, params, args)

	# Se reducen los angulos al intervalo (-pi,pi)
	th1_red = th1%(2*np.pi)
	th1_red = np.where(th1_red>np.pi,th1_red-2*np.pi,th1_red)
	th2_red = th2%(2*np.pi)
	th2_red = np.where(th2_red>np.pi,th2_red-2*np.pi,th2_red)

	# Animacion2D anima los datos obtenidos
	an = fa.Animacion2D(t, 1.1 * (L1 + L2), [x1,x2], [y1,y2], th2_red, th1_red, r'$\theta_2$ (rad)', r'$\theta_1$ (rad)', [m1,m2])

	# Se muestra
	plt.show()

def Triple():
	'''
	Proceso que realiza el experimento del pendulo triple.
	Permite elegir parametros iniciales con sliders, calcula de forma numerica precisa la trayectoria y
	realiza una animacion en 2D.
	'''
	# Se genera la ventana de sliders para seleccionar los parametros iniciales con func_sliders
	button, reset_func, sliders = fs.sliders_window(fs.triple)
	button.on_clicked(reset_func)
	plt.show()

	# Se toman los valores iniciales desde los sliders
	g, m1, m2, m3, L1, L2, L3, w1_0, w2_0, w3_0, th1_0, th2_0, th3_0 = [slider.val for slider in sliders]
	th1_0 = np.radians(th1_0)
	th2_0 = np.radians(th2_0)
	th3_0 = np.radians(th3_0)

	# Se establecen los parametros temporales
	t_0, t_f = 0, 20
	dt = 0.02

	# Se crea el array de tiempos y las tuplas de parametros iniciales y constantes
	t = np.arange(t_0, t_f + dt, dt)
	params = (th1_0, w1_0, th2_0, w2_0, th3_0, w3_0)
	args = (g, L1, L2, L3, m1, m2, m3)

	# Sol_Triple resuelve numericamente el problema
	th1, w1, th2, w2, th3, w3, x1, y1, x2, y2, x3, y3 = Sol_Triple(t, params, args)

	# Se reducen los angulos al intervalo (-pi,pi)
	th2_red = th2%(2*np.pi)
	th2_red = np.where(th2_red>np.pi,th2_red-2*np.pi,th2_red)
	th3_red = th3%(2*np.pi)
	th3_red = np.where(th3_red>np.pi,th3_red-2*np.pi,th3_red)

	# Animacion2D anima los datos obtenidos
	an = fa.Animacion2D(t, 1.1 * (L1 + L2 + L3), [x1,x2,x3], [y1,y2,y3], th2_red, th3_red, r'$\theta_2$ (rad)', r'$\theta_3$ (rad)', [m1,m2,m3])

	# Se muestra
	plt.show()

def Esferico():
	'''
	Proceso que realiza el experimento del pendulo esferico.
	Permite elegir parametros iniciales con sliders, calcula de forma numerica precisa la trayectoria y
	realiza una animacion en 3D.
	'''
	# Se genera la ventana de sliders para seleccionar los parametros iniciales con func_sliders
	button, reset_func, sliders = fs.sliders_window(fs.esferico)
	button.on_clicked(reset_func)
	plt.show()

	# Se toman los valores iniciales desde los sliders
	m, g, L, wph_0, wth_0, ph_0, th_0  = [slider.val for slider in sliders]
	th_0 = np.radians(th_0)
	ph_0 = np.radians(ph_0)

	# Se establecen los parametros temporales
	t_0, t_f = 0, 20
	dt = 0.02

	# Se crea el array de tiempos y las tuplas de parametros iniciales y constantes
	t = np.arange(t_0, t_f + dt, dt)
	params = (th_0, wth_0, ph_0, wph_0)
	args = (g, L)

	# Sol_Esferico resuelve numericamente el problema
	th, wth, ph, wph, x, y, z = Sol_Esferico(t, params, args)

	# Se reducen los angulos al intervalo (-pi,pi)
	th_red = th%(2*np.pi)
	th_red = np.where(th_red>np.pi,th_red-2*np.pi,th_red)
	ph_red = ph%(2*np.pi)
	ph_red = np.where(ph_red>np.pi,ph_red-2*np.pi,ph_red)

	# Animacion3D anima los datos obtenidos
	an = fa.Animacion3D(t, 1.1 * L, [x], [y], [z], th_red, ph_red, r'$\theta$ (rad)', r'$\phi$ (rad)')

	# Se muestra
	plt.show()
