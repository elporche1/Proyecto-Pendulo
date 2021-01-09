'''
Implementa funciones que permiten hacer representaciones graficas de los estados energeticos que pueden
tomar los pendulos como sistemas que conservan la energia.
'''
# ---Imports---
# numpy (np): manejo de arrays
import numpy as np
# matplotlib.pyplot (plt): impresion grafica 2D
import matplotlib.pyplot as plt
# func_sliders (fs): sliders
import func_sliders as fs

# ---Funciones---
def set_angle_label(ax,pos,nombre):
	'''
	Coloca la label y marcas en grados para un angulo desde -pi hasta pi en un eje coordenado.

	---Parametros---
	* ax: axes en los que colocar el label
	* pos: 'x' o 'y' para distinguir entre ejes
	* nombre: string con el nombre del angulo a escribir
	'''
	# Se diferencia entre eje x o eje y para llamar a las correspondientes funciones.
	# x:
	if pos == 'x':

		# Se coloca el label
		ax.set_xlabel('$'+nombre+'$ ($^o$)')

		# Se establecen las marcas de graduacion en el eje
		ax.set_xticks(np.linspace(-np.pi, np.pi, 5))
		ax.set_xticklabels(('-180', '-90', '0', '90', '180'))

	# y:
	elif pos == 'y':

		# Se coloca el label
		ax.set_ylabel(r'$'+nombre+'$ ($^o$)')

		# Se establecen las marcas de graduacion en el eje
		ax.set_yticks(np.linspace(-np.pi, np.pi, 5))
		ax.set_yticklabels(('-180', '-90', '0', '90', '180'))

def Fases(fig, ax, x, y, z, nivel, label = ''):
	'''
	Realiza una representacion grafica de curvas de nivel con color

	---Parametros---
	* fig: figura de plt
	* ax: axes de plt
	* x: array con la variable x
	* y: array con la variable y
	* z: array con el nivel para cada (x,y)
	* nivel: niveles a considerar en la representacion
	+ label: label a colocar en la colorbar
	'''
	# Se dibujan las curvas de nivel
	cs = plt.contour(x, y, z, levels=nivel, colors='k')

	# Se colorea segun el nivel
	cf = plt.contourf(x, y, z, levels=nivel, cmap = 'rainbow')

	# Se coloca la colorbar y se pone su label
	cbar = fig.colorbar(cf)
	cbar.ax.set_ylabel(label)

def Simple():
	'''
	Proceso que realiza una representacion grafica de niveles energeticos del pendulo simple.
	Permite elegir parametros iniciales con sliders.
	'''
	# Se genera la ventana de sliders para seleccionar los parametros iniciales con func_sliders
	button, reset_func, sliders = fs.sliders_window(np.array(fs.simple)[:-3,:].tolist())
	button.on_clicked(reset_func)
	plt.show()

	# Se toman los valores iniciales desde los sliders
	m, g, L = [slider.val for slider in sliders]

	# Se generan arrays para las variables
	th = np.linspace(-np.pi, np.pi, 100)
	w = np.linspace(-10, 10, 100)

	# Se realiza un np.meshgrid de las variables que nos servira para calcular la energia en cada punto
	TH, W = np.meshgrid(th, w)

	# Energia del pendulo simple
	E = m*L**2*W**2/2-m*g*L*np.cos(TH)+m*g*L

	# Se crean la figura y los axes
	fig, ax = plt.subplots()

	# Se toman los niveles de energia que distinguira la representacion desde 0 hasta la energia maxima posible
	nivel = np.linspace(0, m*L**2*50+2*m*g*L, 40)

	# Se usa Fases para realizar la representacion
	Fases(fig, ax, th, w, E, nivel, 'E (J)')

	# Se detalla informacion sobre la representacion
	set_angle_label(ax, 'x', r'\theta')
	ax.set_ylabel('$\omega$ (rad/s)')

	# Se muestra
	plt.show()

def Doble():
	'''
	Proceso que realiza una representacion grafica de niveles energeticos del pendulo doble.
	Permite elegir parametros iniciales con sliders.
	'''
	# Se genera la ventana de sliders para seleccionar los parametros iniciales con func_sliders
	button, reset_func, sliders = fs.sliders_window(np.array(fs.doble)[:-2,:].tolist())
	button.on_clicked(reset_func)
	plt.show()

	# Se toman los valores iniciales desde los sliders
	g, m1, m2, L1, L2, w1, w2 = [slider.val for slider in sliders]

	# Se generan arrays para las variables
	th1 = np.linspace(-np.pi, np.pi, 1000)
	th2 = np.linspace(-np.pi, np.pi, 1000)

	# Se realiza un np.meshgrid de las variables que nos servira para calcular la energia en cada punto
	TH1, TH2 = np.meshgrid(th1, th2)

	# Energia del pendulo doble
	E = (m1+m2)*L1**2*w1**2/2 + m2*L2**2*w2**2/2 + m2*L1*L2*abs(w1)*abs(w2)*np.cos(TH2-TH1)-g*((m1+m2)*L1*np.cos(TH1)+m2*L2*np.cos(TH2)) + g*((m1+m2)*L1+m2*L2)

	# Se crean la figura y los axes
	fig, ax = plt.subplots()

	# Se toman los niveles de energia que distinguira la representacion desde 0 hasta la energia maxima posible
	nivel = np.linspace(0, (m1+m2)*L1**2*w1**2/2 + m2*L2**2*w2**2/2 + m2*L1*L2*abs(w1)*abs(w2)+2*g*((m1+m2)*L1+m2*L2), 40)

	# Se usa Fases para realizar la representacion
	Fases(fig, ax, th1, th2, E, nivel, 'E (J)')

	# Se detalla informacion sobre la representacion
	set_angle_label(ax, 'x', r'\theta_1')
	set_angle_label(ax, 'y', r'\theta_2')

	# Se muestra
	plt.show()

def Triple():
	'''
	Proceso que realiza una representacion grafica de niveles energeticos del pendulo triple.
	Permite elegir parametros iniciales con sliders.
	'''
	# Se genera la ventana de sliders para seleccionar los parametros iniciales con func_sliders
	button, reset_func, sliders = fs.sliders_window(np.array(fs.triple)[:-2,:].tolist())
	button.on_clicked(reset_func)
	plt.show()

	# Se toman los valores iniciales desde los sliders
	g, m1, m2, m3, L1, L2, L3, w1, w2, w3, th1 = [slider.val for slider in sliders]

	# Se generan arrays para las variables
	th2 = np.linspace(-np.pi, np.pi, 1000)
	th3 = np.linspace(-np.pi, np.pi, 1000)

	# Se realiza un np.meshgrid de las variables que nos servira para calcular la energia en cada punto
	TH2, TH3 = np.meshgrid(th2, th3)

	# Energia del pendulo triple
	E = (m1+m2+m3)*L1**2*w1**2/2 + (m2+m3)*L2**2*w2**2/2 +m3*L3**2*w3**2/2 + (m2+m3)*L1*L2*abs(w1)*abs(w2)*np.cos(TH2-th1)+m3*L3*abs(w3)*(L1*abs(w1)*np.cos(TH3-th1)+L2*abs(w2)*np.cos(TH3-TH2))-g*((m1+m2+m3)*L1*np.cos(th1)+(m2+m3)*L2*np.cos(TH2)+m3*L3*np.cos(TH3)) + g*((m1+m2+m3)*L1+(m2+m3)*L2+m3*L3)

	# Se crean la figura y los axes
	fig, ax = plt.subplots()

	# Se toman los niveles de energia que distinguira la representacion desde 0 hasta la energia maxima posible
	nivel = np.linspace(0, (m1+m2+m3)*L1**2*w1**2/2 + (m2+m3)*L2**2*w2**2/2 +m3*L3**2*w3**2/2 + (m2+m3)*L1*L2*abs(w1)*abs(w2)+m3*L3*abs(w3)*(L1*abs(w1)+L2*abs(w2))+g*((m1+m2+m3)*L1+(m2+m3)*L2+m3*L3) + g*((m1+m2+m3)*L1+(m2+m3)*L2+m3*L3), 40)

	# Se usa Fases para realizar la representacion
	Fases(fig, ax, th2, th3, E, nivel, 'E (J)')

	# Se detalla informacion sobre la representacion
	set_angle_label(ax, 'x', r'\theta_2')
	set_angle_label(ax, 'y', r'\theta_3')

	# Se muestra
	plt.show()

def Esferico():
	'''
	Proceso que realiza una representacion grafica de niveles energeticos del pendulo esferico.
	Permite elegir parametros iniciales con sliders.
	'''
	# Se genera la ventana de sliders para seleccionar los parametros iniciales con func_sliders
	button, reset_func, sliders = fs.sliders_window(np.array(fs.esferico)[:-2,:].tolist())
	button.on_clicked(reset_func)
	plt.show()

	# Se toman los valores iniciales desde los sliders
	m, g, L, wph, wth = [slider.val for slider in sliders]

	# Se generan arrays para las variables
	ph = np.linspace(-np.pi, np.pi, 1000)
	th = np.linspace(-2*np.pi, 2*np.pi, 1000)

	# Se realiza un np.meshgrid de las variables que nos servira para calcular la energia en cada punto
	PH, TH = np.meshgrid(ph, th)

	# Energia del pendulo esferico
	E = m*L**2/2*(wph**2+wth**2*np.sin(PH)**2)-m*g*L*np.cos(PH) +m*g*L

	# Se crean la figura y los axes
	fig, ax = plt.subplots()

	# Se toman los niveles de energia que distinguira la representacion desde 0 hasta la energia maxima posible
	nivel = np.linspace(0, m*L**2/2*(wph**2+wth**2)+2*m*g*L, 40)

	# Se usa Fases para realizar la representacion
	Fases(fig, ax, ph, th, E, nivel, 'E (J)')

	# Se detalla informacion sobre la representacion
	set_angle_label(ax, 'x', r'\phi')
	set_angle_label(ax, 'y', r'\theta')

	# Se muestra
	plt.show()
